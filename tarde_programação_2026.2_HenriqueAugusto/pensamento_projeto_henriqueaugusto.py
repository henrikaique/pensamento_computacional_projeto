'''
>>projeto industria de automoveis
'''



# Ufa, quebrei a maldição
# print('Olá, Mundo!')

print('-' * 48 + '\n')
print('Bem-vindo ao Sistema de vendas - industria de automoveis!\n')
print('1 - Cadastrar produto')
print('2 - Listar produtos')
print('3 - Realizar vendas')
print('4 - Buscar veiculos')
print('5 - Buscar por Ano')
print('6 - Financiamento ')
print('7 - Estoque')
print('8 - Agenda de visitas')
print('9 - Sobre')
print('0 - Sair do Sistema')
print('\n------------------------------------------\n')

opcao_definida = int(input('Digite a opção desejada: '))

if opcao_definida == 1:
    print('Cadastrando produto...')

elif opcao_definida == 2:
    print('Listando produtos...')

elif opcao_definida == 3:
    print('Realizando venda...')

elif opcao_definida == 4:
    print('Buscando veiculo...')

elif opcao_definida == 5:
    print('Buscando pelo ano...')

elif opcao_definida == 6:
    print('Listando financiamentos...')

elif opcao_definida == 7:
    print('Revisando no estoque...')

elif opcao_definida == 8:
    print('Buscando na agenda...')

elif opcao_definida == 9:
    print('Listando informações...')

else:
    print('Opção inválida, escolha novamente!')