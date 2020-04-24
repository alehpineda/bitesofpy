from pkg_resources import parse_version


def changed_dependencies(old_reqs: str, new_reqs: str) -> list:
    """Compare old vs new requirement multiline strings
      and return a list of dependencies that have been upgraded
      (have a newer version)
   """
    # pass
    # old_reqs = {key:value for version in old_reqs.splitlines()[1:] for key, value in version.split('==')}
    old = {}
    new = {}
    for version in old_reqs.splitlines()[1:]:
        key, value = version.split("==")
        old[key] = value

    for version in new_reqs.splitlines()[1:]:
        key, value = version.split("==")
        new[key] = value

    return [
        key for key in old.keys() if parse_version(old[key]) < parse_version(new[key])
    ]


# Pybites solution

from distutils.version import StrictVersion


def _get_package_dict1(reqs: str) -> dict:
    """Helper to parse requirements str into a dict of
       (package,  version) k, v pairs
    """
    return dict(line.split("==") for line in reqs.strip().splitlines())


def changed_dependencies1(old_reqs: str, new_reqs: str) -> list:
    """Compare old vs new requirement multiline strings
       and return a list of dependencies that have been upgraded
       (have a newer version)
    """
    old = _get_package_dict1(old_reqs)
    new = _get_package_dict1(new_reqs)

    for package, old_version in old.items():
        new_version = new.get(package)
        if StrictVersion(new_version) > StrictVersion(old_version):
            yield package
