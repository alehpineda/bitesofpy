def get_users(passwd: str) -> dict:
    """Split password output by newline,
      extract user and name (1st and 5th columns),
      strip trailing commas from name,
      replace multiple commas in name with a single space
      return dict of keys = user, values = name.
    """
    output = {}
    for line in passwd.strip().splitlines():
        user, name = line.split(':')[0], line.split(':')[4]
        name = name.rstrip(',').replace(',,,,', ' ') if name else 'unknown'
        output[user] = name

    return output


if __name__ == "__main__":
    pw4 = """
mysql:x:106:107:MySQL Server,,,:/var/lib/mysql:/bin/false
avar:x:1000:1000::/home/avar:/bin/bash
chad:x:1001:1001::/home/chad:/bin/bash
git-svn-mirror:x:1002:1002:Git mirror,,,:/home/git-svn-mirror:/bin/bash
gerrit2:x:1003:1003:Gerrit User,,,:/home/gerrit2:/bin/bash
avahi:x:107:108:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/bin/false
postfix:x:108:112::/var/spool/postfix:/bin/false
ssh-rsa:x:1004:1004::/home/ssh-rsa:/bin/bash
artagnon:x:1005:1005:Ramkumar R,,,,Git GSOC:/home/artagnon:/bin/bash
"""

    print(get_users(pw4))
