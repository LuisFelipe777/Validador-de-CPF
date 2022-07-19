cpf_digitado_usuario = input("Digite seu CPF: ")
cpf_array = []
cpf_str = []


def separa_digitos():
    i = 0
    while i < 9:
        cpf_array.append(int(cpf_digitado_usuario[i]))
        i += 1
    funcao_cria_decimo()


def funcao_cria_decimo():
    numeros = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    digitos_cpf_multiplicados = []
    soma_digitos_cpf_multiplicados = 0

    for i in range(0, 9):
        digitos_cpf_multiplicados.append(cpf_array[i] * numeros[i])

    for i in digitos_cpf_multiplicados:
        soma_digitos_cpf_multiplicados += i

    decimo_digito = 11 - (soma_digitos_cpf_multiplicados % 11)

    if decimo_digito >= 10:
        decimo_digito = 0

    cpf_array.append(decimo_digito)
    funcao_cria_decimo_primeiro()


def funcao_cria_decimo_primeiro():
    numeros = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    digitos_cpf_multiplicados = []
    soma_digitos_cpf_multiplicados = 0

    for i in range(0, 10):
        digitos_cpf_multiplicados.append(cpf_array[i] * numeros[i])
    for i in digitos_cpf_multiplicados:
        soma_digitos_cpf_multiplicados += i
    decimo_primeiro_digito = 11 - (soma_digitos_cpf_multiplicados % 11)

    if decimo_primeiro_digito >= 10:
        decimo_primeiro_digito = 0

    cpf_array.append(decimo_primeiro_digito)

    valida_cpf()


def valida_cpf():
    for i in cpf_array:
        cpf_str.append(str(i))
    cpf_gerado = "".join(cpf_str)

    if cpf_gerado == cpf_digitado_usuario:
        print(f"CPF: {cpf_digitado_usuario} válido")
    else:
        print(f"CPF: {cpf_digitado_usuario} inválido")


separa_digitos()
