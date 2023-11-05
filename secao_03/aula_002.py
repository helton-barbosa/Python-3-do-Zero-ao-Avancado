# Função print()
# Argumentos nomeados utilizados nessa função: (sep='', end='', file=, flush=)

# sep
print('Helton', 'Barbosa', sep=' - ')

# end
print('Rose', 'Barbosa', end=' ...\n')

# file
with open('arquivo.txt', 'w') as arquivo:
    print('Helton', 'Rose', sep=' + ', end='.', file=arquivo)

# flush
print('Aguarde...', flush=True)
