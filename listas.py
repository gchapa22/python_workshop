#LISTAS

a = [1,2,3,4,5]

for x in a:
	print x

a = [x**2 for x in range(10)]

a.append(6)
print a
a.pop()
print a
a.pop(0)
print a
