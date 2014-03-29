#FUNCIONES

def fibonacci_iterativo(n):
	if n<=1:
		return n
	res = 0
	prev_res = 1
	prev_prev = 0
	for range(2,n)
		res=prev_res+prev_prev
		prev_prev = prev_res
		prev = res
	return res

# Recursividad
def fibonacci_recursivo(n):
	if n<=1:
		return n
	else:
		return fibonacci_recursivo(n-1)+fibonacci_recursivo(n-2)

fibo_5 = fibonacci_iterativo(5)
fibo_4 = fibonacci_recursivo(4)

print fibo_5
print fibo_4
print fibonacci_iterativo(3)
print fibonacci_recursivo(2)
print fibonacci_iterativo(1)

