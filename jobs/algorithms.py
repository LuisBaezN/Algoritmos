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
    elif inicio == fin:
        print('\n> Su sumatoria es:', inicio)
    else:
        suma = inicio
        siguiente = inicio + incremento
        working = True
        while working:
            suma += siguiente
            siguiente += incremento
            if (incremento > 0) and (siguiente >= fin):
                if siguiente == fin:
                    suma += siguiente
                print('\n> Su sumatoria es:', suma)
                working = False
            elif (incremento < 0) and (siguiente <= fin):
                if siguiente == fin:
                    suma += siguiente
                print('\n> Su sumatoria es:', suma)
                working = False

def max_min_3(num_1: float, num_2: float, num_3: float) -> list:
    if num_1 == num_2 and num_2 == num_3:
        return num_1, num_1
    elif num_1 < num_2 and num_2 < num_3:
        return num_1, num_3
    

if __name__ == '__main__':
    import os
    
    os.system('cls')
    run = [False, True]
    while run[0]:
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
            run[0] = False
        else:
            print('> Opción no válida, escriba la letra Y si desea hacer una sumatoria o la letra N si no es así.')
    
    while run[1]:
        resp = input('\n> Desea encontrar el número menor y mayor en un grupo de 3 números? (y/n):').lower()[0]
        if resp == 'y':
            os.system('cls')
            print('-'*50)
            print('>> Ejemplo de funcionalidad:\n\n')
            #sum_n(50.0, 70.0, 5.0)
            print('-'*50)
            # Datos
            os.system('cls')
            #sum_n(inicio, fin, incremento)
        elif resp == 'n':
            run[1] = False
        else:
            print('> Opción no válida, escriba la letra Y si desea hacer una sumatoria o la letra N si no es así.')