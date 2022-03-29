print('-=' * 20)
print('ANALISADOR DE TRIÂNGULO 1.0') # Para formar um triângulo, cada segmento deve ser menor que a soma dos outros 2
print('-=' * 20)
# O usuário informa o comprimento de cada segmento
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
print('-=' * 20)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo!')
else:
    print('Os segmentos acima NÃO podem formar um triângulo.')