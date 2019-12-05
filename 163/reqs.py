from pkg_resources import parse_version

def changed_dependencies(old_reqs: str, new_reqs: str) -> list:
   """Compare old vs new requirement multiline strings
      and return a list of dependencies that have been upgraded
      (have a newer version)
   """
   #pass
   #old_reqs = {key:value for version in old_reqs.splitlines()[1:] for key, value in version.split('==')}
   old = {}
   new = {}
   for version in old_reqs.splitlines()[1:]:
      key, value = version.split('==')
      old[key] = value
   
   for version in new_reqs.splitlines()[1:]:
      key, value = version.split('==')
      new[key] = value
   
   return [key for key in old.keys() if parse_version(old[key]) < parse_version(new[key])]
