def sum_n(inicio: float, fin: float, incremento: float = 1.0) -> None:
    '''
    Muestra la sumatoria de un rango dado un incremento.

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
    '''
    Regresa el número mínimo y máximo en un grupo de 3.
    '''
    print(f'> Los datos que usted ingresó son:\n\n    Primer número: {num_1}\n    Segundo número: {num_2}\n    Tercer número: {num_3}\n')

    if num_1 <= num_2:
        minimo = num_1
        maximo = num_2
    else:
        minimo = num_2
        maximo = num_1

    if num_3 <= minimo:
        minimo = num_3
    elif num_3 >= maximo:
        maximo = num_3

    return minimo, maximo

def captura_n(lim: int) -> list:
    '''
    Captura n elementos y los retorna en forma de lista.
    '''
    elementos = []
    for i in range(lim):
        elemento = input(f'    Elemento {i+1}: ')
        elementos.append(elemento)
    return elementos

def max_min_n(test: bool = False, datos: list = ['-1','0','1','Fin']) -> list:
    '''
    Retorna el número mínimo y máximo dentro de un grupo de números.
    '''
    if test:
        i = 0
    print('> Ingrese un número a la vez.')
    minimo = float('inf')
    maximo = -float('inf')
    loop = True
    while loop:
        print('> Para terminar la captura, ingrese la letra f en lugar del número.')
        if test:
            number = datos[i]
            i += 1
        else:
            number = input('Ingrese el número: ')
        os.system("cls")
        if number.lower()[0] == 'f':
            loop = False
        else:
            try:
                number = float(number)
                if number <= minimo:
                    minimo = number
                if number >= maximo:
                    maximo = number
            except Exception as e:
                print(e)
    return minimo, maximo


if __name__ == '__main__':
    import os
    
    os.system('cls')
    run = [0, 0, 1]

    # Primer algoritmo
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
    
    # Segundo algoritmo
    while run[1]:
        resp = input('\n> Desea encontrar el número menor y mayor en un grupo de 3 números? (y/n):').lower()[0]
        if resp == 'y':
            os.system('cls')
            print('-'*50)
            print('>> Ejemplo de funcionalidad:\n\n')
            results = max_min_3(1.6, 22, 3)
            print(f'> Número mínimo: {results[0]}\n> Número máximo: {results[1]}')
            print('-'*50)
            # Datos
            datos = captura_n(3)
            os.system('cls')
            results = max_min_3(int(datos[0]), int(datos[1]), int(datos[2]))
            print(f'> Número mínimo: {results[0]}\n> Número máximo: {results[1]}')
        elif resp == 'n':
            run[1] = False
        else:
            print('> Opción no válida, escriba la letra Y si desea hacer una sumatoria o la letra N si no es así.')
    
    # Tercer algoritmo
    while run[2]:
        resp = input('\n> Desea encontrar el número menor y mayor en un grupo de números? (y/n):').lower()[0]
        if resp == 'y':
            os.system('cls')
            datos = ['-2','34','2','12','-67','45','89','72','f']
            results = max_min_n(True, datos)
            print('-'*50)
            print('>> Ejemplo de funcionalidad:\n\n')
            print('> Con los datos:', datos)
            print(f'> Número mínimo: {results[0]}\n> Número máximo: {results[1]}')
            print('-'*50)
            # Datos
            
            results = max_min_n()
            print(f'> Número mínimo: {results[0]}\n> Número máximo: {results[1]}')
        elif resp == 'n':
            run[2] = False
        else:
            print('> Opción no válida, escriba la letra Y si desea hacer una sumatoria o la letra N si no es así.')

