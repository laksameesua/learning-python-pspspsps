def main():
    number = int(input('What is x? '))
    print(f'{number} is', 'even' if is_even(number) else 'odd')
    main()

def is_even(n):
    return n % 2 == 0

main()
