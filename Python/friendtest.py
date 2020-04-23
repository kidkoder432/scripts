#friendliness test - how friendly are two people?
ci = 0
person1 = input('What is your name? > ')
person2 = input('What is your friend\'s name? > ')
print('Now we look at your interests. Enter these as words followed by spaces. For example, "reading math science"')
p1interests = input('What are your interests? > ').split()
p2interests = input('What are your friend\'s interests? >').split()
if len(p1interests) > len(p2interests)



