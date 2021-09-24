def main():
    # Lists with dictionaries inside 😋
    super_list = [
        {'firstname':'Missael', 'lastname':'Barco'},
        {'firstname':'Gabriel', 'lastname':'Torres'},
        {'firstname':'David', 'lastname':'Mendoza'},
        {'firstname':'María', 'lastname':'García'}
    ]

    # Dictionaries with lists inside 👀
    super_dict = {
        'natural_nums':[1, 2, 3, 4, 5],
        'integer_nums':[-1, -2, 0, 1, 2],
        'floating_nums':[1.1, 4.5, 6.43]
    }

    # Check the content of the super_dict 🤔
    for key, value in super_dict.items():
        print(key, '=', value)

    # Check the content of the super_list 🔍
    for dictionarie in super_list:
        print(dictionarie)

if __name__=='__main__':
    main()