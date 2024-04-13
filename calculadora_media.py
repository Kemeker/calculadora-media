# Calculadora de Media da Thais
print('***************** BEM VINDO ******************** \n')
print('*********** CALCULADORA DE MEDIA DA THAIS *********** \n')      

 # entrando com nome do aluno
aluno_1 = str(input('Digite nome do aluno(a) '))

# Entrada das notas 
n1 = float(input(f'Digite a nota do aluno(a) {aluno_1}: '))
n2 = float(input(f'Digite a nota do aluno(a) {aluno_1}: '))
n3 = float(input(f'Digite a nota do aluno(a) {aluno_1}: '))
n4 = float(input(f'Digite a nota do aluno(a) {aluno_1}: '))


# Soma da media dos alunos
soma = (n1 + n2 + n3 + n4) / 4

#armazendo a soma em uma variavel resultado
resultado = soma 

#apresentando o resultado da media
print(f'\n A media do aluno(a) {aluno_1}, foi de {resultado} ')