n1 = input('digite um numero: ')
n2 = input('digite um numero: ')
print()
op1 = input('gostaria de somar, subtrair, multiplicar ou dividir? : ')
print()
if(op1 == 'somar'):
    print(int(n1)+int(n2))
elif(op1 == 'subtrair'):
    print(int(n1)-int(n2))
elif(op1 == 'multiplicar'):
    print(int(n1)*int(n2))
elif(op1 == 'dividir'):
    print(int(n1)/int(n2))
else:
    print('tente novamente')
