import winsound as w, time
def mlinput(prompt):
    ui = None
    print(prompt)
    totalui = []
    while ui != '':
        ui = input()
        totalui.append(ui)
    return '\n'.join(totalui)  
def musicMaker():
    print('''Welcome to MusicMaker!
             Syntax:
                 " " used to indicate the next group of notes
                 "" used to indicate a fast note delay''')

    for n in (list(SCALE.keys())):
        if n.isupper():
            print(n)
            w.Beep(SCALE.get(n), 1000)
    while True:
        seq = mlinput('Please enter a sequence of notes. >>> ')
        for note in seq.split('  '):
            
            for n in note.split(' '):
                try:
                    if len(note) > 1:
                        w.Beep(SCALE.get(n), 150)
                    elif seq[seq.index(note) + 1] == '-': 
                        w.Beep(SCALE.get(n), 600)
                    else:
                        w.Beep(SCALE.get(n), 300)
                except (TypeError, IndexError):
                    pass
musicMaker()        
    
    
