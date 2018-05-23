#challenge was to modify the function to include a default step value of 1
#highlighting difference between positional parameters and and default parameter values

ask_number(question, low, high, step = 1):
  """Ask for a number within a range."""
  response = None
  while response not in range(low, high, step):
    response = int(input(question))
    return response
