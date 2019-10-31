import re

def generate_affiliation_link(url):
    try:
        aff = re.search(r'(\/dp\/\d+\w)', url).group(1)
        return 'http://www.amazon.com'+ aff +'/?tag=pyb0f-20'
    except AttributeError:
        raise
