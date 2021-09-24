def main():

    # First, with a for loop 😋
    dict_1 = {}
    for i in range(1, 1001):
        dict_1[i] = i**0.5

    # Print 5 elements of the dict
    five_keys1 = list(dict_1.keys())[0:5]
    print('With a for loop: ', [(i, dict_1[i]) for i in five_keys1])

    # Now, with dictionary comprehension 🔥
    dict_2 = {i: i**0.5 for i in range(1, 1001)}

    five_keys2 = list(dict_1.keys())[0:5]
    print('With dict comprehension: ', [(i, dict_2[i]) for i in five_keys2])

    # Check if the dicts are aqual
    if dict_1 == dict_2:
        print('They are equal 🎉')
    else:
        print('They are different 😟')


if __name__ == '__main__':
    main()
