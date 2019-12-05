def common_languages(programmers):
   """Receive a dict of keys -> names and values -> a sequence of
      of programming languages, return the common languages"""
   
   languages = [values for _, values in programmers.items()]
   
   return _common_elements(languages)

def _common_elements(arr):
   
   result = set(arr[0]) 

   for currSet in arr[1:]: 
      result.intersection_update(currSet) 
  
   return list(result)
