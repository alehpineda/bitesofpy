"""
Get the top 10 blog tags of PyBites (e.g. python, flask, django, learning).

Our tests suppose you will use a collections.Counter - best practice and less code.

What are the PyBites guys most passionate about? See the tests and you'll know the answer, then code your solution to make them pass

Keep calm and code in Python! :)
"""

import os
from collections import Counter
import urllib.request

# prep
tempfile = os.path.join('/tmp', 'feed')
urllib.request.urlretrieve('http://bit.ly/2zD8d8b', tempfile)

with open(tempfile) as f:
    content = f.read().lower()


# start coding
import xml.etree.ElementTree as ET

def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    root = ET.fromstring(content)
    c = Counter()
    for tag in root.iter('category'):
        c[tag.text] += 1

    return c.most_common(n)

# My solution using feedparser
# Need fix
import feedparser

def get_pybites_top_tags_1(n=10):
    rss = feedparser.parse(content)
    c = Counter(tag.term for entry in rss.entries for tag in entry.tags)

    return c.most_common(n)

# pybites solution using regex
import re

TAG_HTML = re.compile(r'<category>([^<]+)</category>')

def get_pybites_top_tags_2(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    tags = TAG_HTML.findall(content)
    return Counter(tags).most_common(n)

# pybites forum 
def get_pybites_top_tags_3(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    tree = ET.fromstring(content)
    return Counter(c.text for c in tree.iter('category')).most_common(n)
