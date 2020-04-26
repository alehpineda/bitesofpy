import csv
import random
import re
import string
import sys

import pytest

from cls import get_classes

csv_classes = [
    "Dialect",
    "DictReader",
    "DictWriter",
    "Error",
    "OrderedDict",
    "Sniffer",
    "StringIO",
]
random_classes = ["Random", "SystemRandom"]
re_classes = ["Match", "Pattern", "RegexFlag", "Scanner"]
string_classes = ["Formatter", "Template"]


@pytest.mark.skipif(
    sys.version_info > (3, 7),
    reason="In python 3.8, OrderedDict was moved out from csv",
)
@pytest.mark.parametrize(
    "mod, expected",
    [
        (csv, csv_classes),
        (random, random_classes),
        (re, re_classes),
        (string, string_classes),
    ],
)
def test_cls(mod, expected):
    actual = get_classes(mod)
    assert sorted(actual) == sorted(expected)
