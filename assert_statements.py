def divisors(num):
    divisors = []
    for x in range(1, num+1):
        if num%x == 0:
            divisors.append(x)

    return divisors

def main():

    num = input('Ingresa un número entero positivo: ')
    assert num.isnumeric(), "Debes ingresar un número entero positivo 👀"

    num = int(num)
    print(divisors(num))
    print('Terminó el programa 💓')

if __name__=='__main__':
    main()