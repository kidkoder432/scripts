import myai
feeling = input('Hello, %s. How are you today? > ' %(input('Hello. What is your name? > '))).lower()
yn = myai.happyOrSad(feeling)
if yn == 0 and len(feeling.split(' ')) > 1:
    print('''I'm sorry you feel that way. Is there anything I can do to help?''')
elif len(feeling) == 0:
    feeling = input('Oops. I didn\'t get that. Could you say it again? > ').lower()    
else:
    print('I think we\'ll make good friends.')