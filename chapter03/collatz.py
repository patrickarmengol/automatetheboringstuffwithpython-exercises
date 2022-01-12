


def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    print(result)
    return result

if __name__ == '__main__':
    print('enter number:')
    while True:
        try:
            collatz(int(input()))
        except ValueError:
            print('you must enter an integer')
    