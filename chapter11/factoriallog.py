import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('start of program')

def factorial(n):
    logging.debug(f'start of factorial({n})')
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug(f'i is {i}, total is {total}')
    logging.debug(f'end of factorial({n})')
    return total

print(factorial(5))

logging.debug('end of program')