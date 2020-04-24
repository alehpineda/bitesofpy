import re

PYBITES_LINK = "http://www.amazon.com{}/?tag=pyb0f-20"


def generate_affiliation_link(url):
    try:
        aff = re.search(r"(\/dp\/\d+\w)", url).group(1)
        return PYBITES_LINK.format(aff)
    except AttributeError:
        raise


# Pybites solution


PYBITES_LINK1 = "http://www.amazon.com/dp/{}/?tag=pyb0f-20"


def generate_affiliation_link1(url):
    asin = url.split("dp/")[-1].split("/")[0]
    return PYBITES_LINK1.format(asin)
