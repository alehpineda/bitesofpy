def common_languages(programmers):
   """Receive a dict of keys -> names and values -> a sequence of
      of programming languages, return the common languages"""
   # create a list of sets with the languages.
   languages = [set(language) for language in programmers.values()]

   # return the intersection unpacking all the languages
   return set.intersection(*languages)
