classes = []
assignments = {}
cn = ''

def newassign():
    cn = input('Enter class name: ')
    while cn not in classes:
        cn = input('Invalid class. Enter class name: ')
    ag = input('Enter assignment name: ')
    assignments[cn].append(ag)
def add():
    classname = input('Enter class name: ')
    classes.append(classname)

def done():
    cn = input('Enter class name: ')
    while cn not in classes:
        cn = input('Invalid class. Enter class name:')
    ag = input('Enter assignment name: ')
    assignments[cn].remove(ag)
def show():
    print('Classes: ')
    print('\n'.join(classes))
def todo():
    print('Assignments: ')
    print('  '.join(assignments))
def info():
    print('''
    Info about commands:
    info - Shows this page
    show - Shows all classes
    add - Adds a new class
    done - Removes an assignment
    newassign - Make a new assignment
    remove <classname> - Removes the class that matches classname.
    exit - Exit Classroom.
    todo - Shows unfinished assignments.''')
print('Text-based Google Classroom. Press CTRL-C + Enter to exit.')
while True:
    for c in classes:
        if c not in list(assignments.keys()):
            assignments[c] = []
    f = input('classroom> ')
    if f == 'exit':
        break
    # try:
    eval(f + '()')
    # except:
    #     print(f + ': failed')
f = open('classes.txt', 'w')
f.write('  '.join(classes))
f.write('\n\n\n\n')
f.write('  '.join(assignments))
f.close()