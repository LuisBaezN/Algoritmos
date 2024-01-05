def ciclo_func(func: function, param: list = [], name: str = '') -> None:
    run = True
    while run:
        resp = input(f'\n> Desea calcular la función {name}? (y/n):').lower()[0]
        if resp == 'y':
            os.system('cls')
            print('-'*50)
            print('>> Ejemplo de funcionalidad:\n\n')
            func()
            print('-'*50)
            inicio = float(input('\n> Ingrese los siguientes datos:\n\n> Número inicial: '))
            fin = float(input('> Número final: '))
            incremento = float(input('> Incremento: '))
            os.system('cls')
            sum_n(inicio, fin, incremento)
        elif resp == 'n':
            run = False
        else:
            print('> Opción no válida, escriba la letra Y si desea hacer una sumatoria o la letra N si no es así.')

def sum_n(inicio: float, fin: float, incremento: float) -> None:
    '''
    Muestra la sumatoria dado un rango con su respectivo incremento.

    El algoritmmo tiene una presición de seis dígitos. Si, dentro del incremento, el último número
    de la secuencia sobrepasa la cota final, este número no se agrega a la sumatoria.
    '''
    from decimal import Decimal, getcontext

    getcontext().prec = 6

    inicio = Decimal(inicio)
    fin = Decimal(fin)
    incremento = Decimal(incremento)

    print(f'> Los datos que usted ingresó son:\n\n    Inicio: {inicio}\n    Fin: {fin}\n    Incremento: {incremento}')
    if incremento == 0:
        print('> Su sumatoria es imposible de realizar, dado que el incremento es nulo.')
    elif inicio < fin and incremento < 0:
        print('> Su sumatoria es imposible de realizar, dado que el número inicial se aleja del número final.')
    elif inicio > fin and incremento > 0:
        print('> Su sumatoria es imposible de realizar, dado que el número final se aleja del número inicial.')
    else:
        secuencia = [inicio]
        siguiente = inicio + incremento
        working = True
        while working:
            secuencia.append(siguiente)
            siguiente = siguiente + incremento
            if incremento > 0 and siguiente >= fin:
                if siguiente == fin:
                    secuencia.append(siguiente)
                print('\n> Su sumatoria es:', sum(secuencia))
                working = False
            elif siguiente <= fin:
                if siguiente == fin:
                    secuencia.append(siguiente)
                print('\n> Su sumatoria es:', sum(secuencia))
                working = False

if __name__ == '__main__':
    import os
    
    os.system('cls')
    run = True
    while run:
        resp = input('\n> Desea calcular una sumatoria? (y/n):').lower()[0]
        if resp == 'y':
            os.system('cls')
            print('-'*50)
            print('>> Ejemplo de funcionalidad:\n\n')
            sum_n(50.0, 70.0, 5.0)
            print('-'*50)
            inicio = float(input('\n> Ingrese los siguientes datos:\n\n> Número inicial: '))
            fin = float(input('> Número final: '))
            incremento = float(input('> Incremento: '))
            os.system('cls')
            sum_n(inicio, fin, incremento)
        elif resp == 'n':
            run = False
        else:
            print('> Opción no válida, escriba la letra Y si desea hacer una sumatoria o la letra N si no es así.')