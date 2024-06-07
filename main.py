# faz as importações
import os
from modulos import *

# programa principal
if __name__ == '__main__':
    while True:
        exibir_menu()
        opcao = input('Opção desejada: ')
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela, compatível com Windows e Unix

        match opcao:
            case '1':
                b = float(input('Base do quadrilátero: '))
                h = float(input('Altura do quadrilátero: '))
                print(f'Área: {calcular_quadrilatero(b, h)}')
                continue
            case '2':
                r = float(input('Raio do círculo: '))
                print(f'Área: {calcular_circulo(r)}')
                continue
            case '3':
                b = float(input('Base do triângulo: '))
                h = float(input('Altura do triângulo: '))
                print(f'Área: {calcular_triangulo(b, h)}')
                continue
            case '4':
                b_menor = float(input('Base menor do trapézio: '))
                b_maior = float(input('Base maior do trapézio: '))
                h = float(input('Altura do trapézio: '))
                print(f'Área: {calcular_trapezio(b_menor, b_maior, h)}')
                continue
            case '5':
                print('Programa encerrado!')
                break
            case _:
                print('Opção inválida.')

                

