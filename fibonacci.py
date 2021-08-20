num = int(input())

fib_sequence = [0,1]
def fibonacci(n):
 
 if n <= 2 :
	 return 1
 
 else:
	 sum = fib_sequence[-2] + fib_sequence[-1] 
	 fib_sequence.append(sum)
	 print(sum)
	 fibonacci(n-1)


print(fib_sequence[0])
print(fib_sequence[1])
fibonacci(num)
