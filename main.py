pessoa = {
    'Nome':'Alex Machado',
    'Idade':'39',
    'Profissão':'Programador',
    'Empresa':'SENAI',
    'Genero':'Masculino',
    'cidade':'Taguatinga',
}

#remover chave
del pessoa[input{'informe o nome da chave a ser deletada: '}]

    #exibe os dados
for chave in pessoa:
    print(f'{chave}: {pessoa.get(chave)}')