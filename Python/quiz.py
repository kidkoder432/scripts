import time, platform
if platform.system() == 'Windows':
	f = 'python\\errata.txt'
else:
	f = 'Python/errata.txt'
score = 0
content = str(open('errata.txt', 'r').read()).split('\n\n\n')
questions = content[0].split('\n')
answers = content[1].split('\n')
print('WELCOME TO THE QUIZ!\nMade by Prajwal Agrawal')
print('''

Instructions:
All dates must be in the format m/d/yyyy. For example: 7/4/1975 or 11/4/1773
Answers can be of any case. For example, apple and APPLe are both valid.


''')
time.sleep(1)
for i in range(1, len(questions) + 1):
	ans = input('Question %s: %s > ' %(i, questions[i - 1]))
	if ans.lower() == answers[i - 1]:
		print('You got it!')
		score += 1
	else:
		print('Nope. The answer was %s.' %(answers[i - 1]))
print('Your score was %s/%s.' %(score, len(questions)))


