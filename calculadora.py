#!/usr/bin/env python3

while True:
    print("\n=== CALCULADORA ===")
    print("0 - Sair")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    operacao = input("Escolha a operação: ")

    if operacao == '0':
        print("Encerrando a calculadora...")
        break

    try:
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
    except ValueError:
        print("Erro: você precisa digitar números válidos.")
        continue  # volta para o início do loop

    if operacao == '1':
        resultado = num1 + num2
        print(f'O resultado da soma é: {resultado}')
    elif operacao == '2':
        resultado = num1 - num2
        print(f'O resultado da subtração é: {resultado}')
    elif operacao == '3':
        resultado = num1 * num2
        print(f'O resultado da multiplicação é: {resultado}')
    elif operacao == '4':
        if num2 != 0:
            resultado = num1 / num2
            print(f'O resultado da divisão é: {resultado:.2f}')
        else:
            print('Erro: Não é possível dividir por zero.')
    else:
