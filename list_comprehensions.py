def filter_num(x):
    # Function to check if the number follow the rules
    return (x % 4 == 0 and x % 6 == 0 and x % 9 == 0 and x < 10**5)


def main():

    # First, with a for loop 😀
    number_list1 = []
    for x in range(1, 10**5):
        if filter_num(x):
            number_list1.append(x)

    # Look at the first 10 terms
    print('With a for loop: ', number_list1[0:10])

    # Now, with list comprehension 🔥
    number_list2 = [x for x in range(1, 10**5) if filter_num(x)]
    print('With list comprehensions', number_list2[0:10])

    # Check if the lists are aqual
    if number_list1 == number_list2:
        print('They are equal 🎉')
    else:
        print('They are different 😟')


if __name__ == '__main__':
    main()
