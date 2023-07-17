def fibonacci(n):
  fib = [0,1]
  if n <= 0:
    return[]
  elif n == 1:
    return[0]
  elif n == 2:
    return[0,1]
  else:
    for i in range(2,n):
      fib.append(fib[-1] + fib[-2])
    return fib
num_terms = int(input("Enter the number of terms: "))
fib_seq = fibonacci(num_terms)
print("Fibonacci sequence: ", fib_seq)
