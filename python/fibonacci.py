def fibonacci(num):
  if num == 0:
    return 0
  elif num == 1:
    return 1
  else:
    prevResult = 0
    result = 1
    for i in range(2, num + 1):
      tempResult = result	
      result = result + prevResult	
      prevResult = tempResult
  return result

# print(fibonacci(7))

# def fibonacci(n):
#      if n in {0, 1}:  # Base case
#          return n
#      return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case