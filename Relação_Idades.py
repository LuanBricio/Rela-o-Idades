nomes_geral = []
idades_geral = []
nomes_mais18 = []
idades_mais18 = []

while True:
    nome = input('Digite o nome da pessoa (para sair digite "1"):')
    if nome == '1':
        break
    else:
        nomes_geral.append(nome)
        idade = int(input('Digite a idade da pessoa, em anos:'))
        idades_geral.append(idade)
for idx, num in enumerate(idades_geral):
    if num >= 18:
        idades_mais18.append(idades_geral[idx])
        nomes_mais18.append(nomes_geral[idx])


arquivo = open('Relação_das_idades.txt', 'a',)

arquivo.write("Relação das pessoas com mais de 18 anos \n")

for a,b in zip(nomes_mais18, idades_mais18):
    print(f'{a}: {b}')
    
    arquivo.writelines(f'{a}: {b} anos\n')
