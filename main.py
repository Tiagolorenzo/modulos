# importa modulo
import modulos

# programa principal
if __name__ == '__main__':
   import math

def calcular_quadrilatero(base, altura):
    return base * altura

def calcular_triangulo(base, altura):
    return (base * altura) / 2

def calcular_circulo(raio):
    return math.pi * (raio ** 2)

def exibir_menu():
    print('Escolha a figura geométrica para calcular a área: ')
    print('1. Quadrilátero')
    print('2. Triângulo')
    print('3. Círculo')
    print('4. Sair')

if __name__ == '__main__':
    while True:
        exibir_menu()
        opcao = input('Opção desejada: ')

        match opcao:
            case '1':
                b = float(input('Base do quadrilátero: '))
                h = float(input('Altura do quadrilátero: '))
                print(f'Área: {calcular_quadrilatero(b, h)}')
            case '2':
                b = float(input('Base do triângulo: '))
                h = float(input('Altura do triângulo: '))
                print(f'Área: {calcular_triangulo(b, h)}')
            case '3':
                r = float(input('Raio do círculo: '))
                print(f'Área: {calcular_circulo(r)}')
            case '4':
                print('Saindo do programa.')
                break
            case _:
                print('Opção inválida.')

