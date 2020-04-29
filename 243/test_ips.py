import os
from pathlib import Path
from ipaddress import IPv4Network
from urllib.request import urlretrieve
from tempfile import gettempdir

import pytest

from ips import (
    ServiceIPRange,
    parse_ipv4_service_ranges,
    get_aws_service_range,
)

URL = "https://bites-data.s3.us-east-2.amazonaws.com/ip-ranges.json"
TMP = os.getenv("TMP", gettempdir())
PATH = Path(TMP, "ip-ranges.json")
IP = IPv4Network("192.0.2.8/29")


@pytest.fixture(scope="module")
def json_file():
    """Import data into tmp folder"""
    urlretrieve(URL, PATH)
    return PATH


def test_service_ip_range():
    service_ip_range = ServiceIPRange("Microsoft", "us-east-1", IP)
    assert service_ip_range.service == "Microsoft"
    assert service_ip_range.region == "us-east-1"
    assert service_ip_range.cidr == IP
    assert str(service_ip_range) == (
        f"{service_ip_range.cidr} is allocated to the {service_ip_range.service} "
        f"service in the {service_ip_range.region} region"
    )


def test_parse_ipv4_service_ranges_success(json_file):
    assert isinstance(parse_ipv4_service_ranges(json_file), list)


def test_get_aws_service_range_success(json_file):
    assert isinstance(
        get_aws_service_range(
            "13.248.118.0", parse_ipv4_service_ranges(json_file)
        ),
        list,
    )
    assert (
        get_aws_service_range("0.0.0.0", parse_ipv4_service_ranges(json_file))
        == []
    )


def test_get_aws_service_range_failure(json_file):
    with pytest.raises(ValueError) as excinfo:
        get_aws_service_range(
            "13.248.118.0/24", parse_ipv4_service_ranges(json_file)
        )
    assert "Address must be a valid IPv4 address" in str(excinfo.value)


def test_dataclass():
    expected = (
        "192.0.2.8/29 is allocated to the pybites service " "in the US region"
    )
    assert str(ServiceIPRange("pybites", "US", IP)) == expected


def test_parse_ranges(json_file):
    out = parse_ipv4_service_ranges(json_file)
    assert len(out) == 1886

    assert type(out) == list
    assert all(type(element) == ServiceIPRange for element in out)
    assert str(out[0]) == (
        "13.248.118.0/24 is allocated to the AMAZON "
        "service in the eu-west-1 region"
    )


def test_get_aws_service_range_zero_hits():
    assert get_aws_service_range("13.248.118.0", []) == []


def test_get_aws_service_range_two_hits(json_file):
    service_range = parse_ipv4_service_ranges(json_file)
    expected = [
        ServiceIPRange(
            service="AMAZON",
            region="eu-west-1",
            cidr=IPv4Network("13.248.118.0/24"),
        ),
        ServiceIPRange(
            service="GLOBALACCELERATOR",
            region="eu-west-1",
            cidr=IPv4Network("13.248.118.0/24"),
        ),
    ]
    assert get_aws_service_range("13.248.118.0", service_range) == expected


def test_get_aws_service_range_exception():
    with pytest.raises(ValueError) as exc:
        get_aws_service_range("nonsense", {})
    assert str(exc.value) == "Address must be a valid IPv4 address"
