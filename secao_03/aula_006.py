# Conversão de tipos (casting)

# Conversão implícita:
inteiro = 5
flutuante = 2.5
soma = inteiro + flutuante
print(soma, type(soma))

# Funções de conversão de tipos:
# int()
texto = '85'
inteiro = int(texto)
print(texto, type(texto))
print(inteiro, type(inteiro))

# float()
inteiro = 10
flutuante = float(inteiro)
print(inteiro, type(inteiro))
print(flutuante, type(flutuante))

# str()
numero = 45
texto = str(numero)
print(numero, type(numero))
print(texto, type(texto))
