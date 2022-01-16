import pyinputplus as pyip
import re




bread_type = pyip.inputMenu(['wheat', 'white', 'sourdough'], 'choose a type of bread:\n')
protein_type = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], 'choose a type of protein\n')
cheese_bool = pyip.inputYesNo('do you want cheese?\n')
if cheese_bool == 'yes':
    cheese_type = pyip.inputMenu(['cheddar', 'swiss', 'mozzarella'], 'choose a type of cheese\n')
mayo_bool = pyip.inputYesNo('do you want mayo?\n')
mustard_bool = pyip.inputYesNo('do you want mustard?\n')
lettuce_bool = pyip.inputYesNo('do you want lettuce?\n')
tomato_bool = pyip.inputYesNo('do you want tomato?\n')
num_sandwiches = pyip.inputInt('how many sandwiches do you want?\n', min=1)

price = 2
for extra in [cheese_bool, mayo_bool, mustard_bool, lettuce_bool, tomato_bool]:
    if extra == 'yes':
        price += 0.2

print(f'cost of sandwich: {price:.2f}')
print(f'total cost: {(price * num_sandwiches):.2f}')