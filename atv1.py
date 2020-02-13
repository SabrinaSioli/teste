a = int(input('a:')
b = int(input('b:')
c = int(input('c:')

print('Equação digitada: ',a,'x²+',b,'x+',c)

delta = b*b - 4*a*c

if delta>0:
	r1 = (-b+a**0.5)/2
	r2 = (-b-a**0.5)/2
	print('R1: ',r1,'R2: ',r2)

