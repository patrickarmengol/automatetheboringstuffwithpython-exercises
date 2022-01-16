import pyinputplus as pyip
import random, time

number_of_questions = 10
correct_answers = 0

for question_num in range(number_of_questions):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    prompt = f'#{question_num}: {num1} x {num2} = '

    try:
        pyip.inputStr(prompt, allowRegexes=[f'^{num1 * num2}$'], blockRegexes=['.*', 'incorrect'], timeout=8, limit=3)
    except pyip.TimeoutException:
        print('out of time')
    except pyip.RetryLimitException:
        print('out of tries')
    else:
        print('correct')
        correct_answers += 1
    
    time.sleep(1)
print(f'score: {correct_answers} / {number_of_questions}')

# why the HECK did the author start using the old python2 % string formatting here?