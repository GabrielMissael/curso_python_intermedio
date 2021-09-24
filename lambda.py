def main():
    # With normal function
    def palindrome(string):
        return string == string[::-1]
    print('With normal function', palindrome('ana'))

    # With lambda function
    palindrome_lambda = lambda string: string == string[::-1]
    print('With lambda variable:', palindrome_lambda('ana'))

    # Check type of variable
    print('Type of variable:', type(palindrome_lambda))

if __name__ == '__main__':
    main()