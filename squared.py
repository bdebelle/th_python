
# squared(5) would return 25
# squared("2") would return 4
# squared("tim") would return "timtimtim"
def squared (num):
  try:
    test = int(num)
    return (test ** 2)
  except ValueError:
    return (num * len(num))