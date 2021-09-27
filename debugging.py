def divisors(num):
    divisors = []
    for x in range(1, num+1):
        if num%x == 0:
            divisors.append(x)

    return divisors

def main():
    num = int(input('Ingresa un número: '))
    print(divisors(num))
    print('Terminó mi programa')

if __name__=='__main__':
    main()