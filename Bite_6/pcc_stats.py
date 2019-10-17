""" Checks community branch dir structure to see who submitted most
    and what challenge is more popular by number of PRs

    Given a listing of files of our community branch determine who 
    PR'd (= submitted pull request) the most (excluding PyBites) 
    and what challenge is the most popular (PR'd) as per snapshot 
    of today (8th of Dec 2017).

    See preparation done in the code template below. Replace pass 
    with your code to make the test pass. Good luck and have fun!
"""
from collections import Counter, namedtuple
import os
import urllib.request
from tempfile import gettempdir

# prep
TMP = gettempdir()
tempfile = os.path.join(TMP, 'dirnames')
urllib.request.urlretrieve('http://bit.ly/2ABUTjv', tempfile)

IGNORE = 'static templates data pybites bbelderbos hobojoe1848'.split()

users, popular_challenges = Counter(), Counter()

Stats = namedtuple('Stats', 'user challenge')


# code

def gen_files():
    """Return a generator of dir names reading in tempfile

       tempfile has this format:

       challenge<int>/file_or_dir<str>,is_dir<bool>
       03/rss.xml,False
       03/tags.html,False
       ...
       03/mridubhatnagar,True
       03/aleksandarknezevic,True

       -> use last column to filter out directories (= True)
    """
    with open(tempfile) as f:
        for line in f.read().splitlines():
            if line.split(',')[1] == 'True':
                if line.split(',')[0].split('/')[1] in IGNORE:
                    continue
                yield (line.split(',')[0].split('/'))



def diehard_pybites():
    """Return a Stats namedtuple (defined above) that contains the user that
       made the most PRs (ignoring the users in IGNORE) and a challenge tuple
       of most popular challenge and the amount of PRs for that challenge.
       Calling this function on the dataset (held tempfile) should return:
       Stats(user='clamytoe', challenge=('01', 7))
    """
    for challenge, user in gen_files():
        users.update((user,challenge)) 
        popular_challenges.update((challenge,))

    return Stats(users.most_common(1)[0][0], popular_challenges.most_common(1)[0])

# code from pybites

def gen_files1():
    """Return a generator of dir names reading in tempfile

       tempfile has this format:

       challenge<int>/file_or_dir<str>,is_dir<bool>
       03/rss.xml,False
       03/tags.html,False
       ...
       03/mridubhatnagar,True
       03/aleksandarknezevic,True

       -> use last column to filter out directories (= True)
    """
    with open(tempfile) as f:
        return (line.split(',')[0].lower()
                for line in f.readlines()
                if line.strip().endswith('True'))


def diehard_pybites1():
    """Return a Stats namedtuple (defined above) that contains the user that
       made the most PRs (ignoring the users in IGNORE) and a challenge tuple
       of most popular challenge and the amount of PRs for that challenge.
       Calling this function on the dataset (held tempfile) should return:
       Stats(user='clamytoe', challenge=('01', 7))
    """
    for dir_ in gen_files():
        ch, user = dir_.split('/')

        if user in IGNORE:
            continue

        users[user] += 1
        popular_challenges[ch] += 1

    user = users.most_common(1)[0][0]
    challenge = popular_challenges.most_common(1)[0]
    return Stats(user=user, challenge=challenge)
