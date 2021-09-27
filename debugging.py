def divisors(num):
    divisors = []
    for x in range(1, num+1):
        if num%x == 0:
            divisors.append(x)

    return divisors

def main():

    try:
        num = int(input('Ingresa un número entero positivo: '))
        if num < 0 or num%1 != 0:
            raise Exception('Debes ingresar un número entero positivo 🙄')
        print(divisors(num))

    except ValueError:
        print('Debes ingresar un número 👀')

    except Exception as ve:
        print(ve)
        exit()

    else:
        print('Ningun error en el camino 😁')

    finally:
        print('Terminó mi programa 💓')

if __name__=='__main__':
    main()