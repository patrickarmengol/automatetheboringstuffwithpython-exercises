# as usual, google has changed its shit, so i'll have to modify some of the steps

import pyautogui, time

form_data = [
    {'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand',
    'robocop': 4, 'comments': 'Tell Bob I said hi.'},
    {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 
    'robocop': 4, 'comments': 'n/a'},
    {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball',
    'robocop': 1, 'comments': 'Please take the puppets out of the break room.'},
    {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money',
    'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'}
]

pyautogui.PAUSE = 0.5
print('ensure that the browser window is active and the form is loaded')

for person in form_data:
    print('>>> 5 second pause to let user press ctrl+c <<<')
    time.sleep(5)
    
    print(f'entering {person["name"]} info')
    pyautogui.write(['\t', '\t', '\t', '\t'])
    
    pyautogui.write(person['name'] + '\t')
    
    pyautogui.write(person['fear'] + '\t')

    if person['source'] == 'wand':
        pyautogui.write(['down', ' ', '\t'], 0.5)
    elif person['source'] == 'amulet':
        pyautogui.write(['down', 'down', ' ', '\t'], 0.5)
    elif person['source'] == 'crystal ball':
        pyautogui.write(['down', 'down', 'down', ' ', '\t'], 0.5)
    elif person['source'] == 'money':
        pyautogui.write(['down', 'down', 'down', 'down', ' ', '\t'], 0.5)
    
    if person['robocop'] == 1:
        pyautogui.write([' ', '\t', '\t'], 0.5)
    elif person['robocop'] == 2:
        pyautogui.write(['right', '\t', '\t'], 0.5)
    elif person['robocop'] == 3:
        pyautogui.write(['right', 'right', '\t', '\t'], 0.5)
    elif person['robocop'] == 4:
        pyautogui.write(['right', 'right', 'right', '\t', '\t'], 0.5)
    elif person['robocop'] == 5:
        pyautogui.write(['right', 'right', 'right', 'right', '\t', '\t'], 0.5)

    pyautogui.write(person['comments'] + '\t')

    time.sleep(0.5)
    pyautogui.press('enter')

    print('submitted form')
    time.sleep(5)

    # book example is fucked
    # "You stored the coordinates of this link as a tuple in submitAnotherLink in step 2, so pass these coordinates to pyautogui.click() to click this link."
    # no i fucking didn't; it's not in the book
    # the title of the step is "Step 2: Set Up Coordinates" but does not talk about coordinates at all?
    pyautogui.click(2667, 305)
