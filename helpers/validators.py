import validators

def check_url(string):
  if (validators.url(string)):
    return True
  else:
    return False