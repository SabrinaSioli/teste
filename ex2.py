num = int(input('Digite um número: '))

incremento = 1

while(num < 100):
	if(num%7)==0:
		print(num)
		num += 1
		num += incremento
	num += incremento
