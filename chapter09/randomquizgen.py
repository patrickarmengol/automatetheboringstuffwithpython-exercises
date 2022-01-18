#! python3
# randomquizgen.py - creates quizzes with questions and answers in random order, along with answer keys

'''
requirements:
1. create 35 different quizes
2. create 50 multiple choice questions for each quiz in random order
3. provide correct answer and generate 3 random wrong answers; randomize order
4. write the quizes to 35 text files
5. write the answer keys to 35 text files
'''

import random
from pathlib import Path

capitals = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Pheonix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Deleware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansig',
    'Minnesota': 'Saint Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismark',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'
}

for quiz_num in range(1,36):
    quiz_file = open(Path.cwd()/f'chapter09/quizes/capitalsquiz{quiz_num}.txt', 'w')
    answer_file = open(Path.cwd()/f'chapter09/quizes/capitalsanswers{quiz_num}.txt', 'w')

    quiz_file.write('Name:\nDate:\nPeriod:\n\n')
    quiz_file.write((' ' * 20) + f'State Capitals Quiz (Form {quiz_num})\n\n')

    states = list(capitals.keys())
    random.shuffle(states)

    for i, state in enumerate(states):
        question_num = i + 1
        correct_answer = capitals[state]
        wrong_answers = list(capitals.values())
        wrong_answers.remove(correct_answer)
        wrong_answers = random.sample(wrong_answers, 3)
        answer_options = wrong_answers + [correct_answer]
        random.shuffle(answer_options)

        quiz_file.write(f'{question_num}. What is the capital of {state}?\n')
        for j, option in enumerate(answer_options):
            quiz_file.write(f'  {"ABCD"[j]}. {answer_options[j]}\n')
        quiz_file.write('\n')

        answer_file.write(f'{question_num}. {"ABCD"[answer_options.index(correct_answer)]}\n')
    quiz_file.close()
    answer_file.close()
            

