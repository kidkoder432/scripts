import func as f, time
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
''')
    SCALE = {'S': 208, 
             'r': 221,
             'R': 234,
             'g': 249, 
             'G': 261,
             'M': 278, 
             'm': 296, 
             'P': 311, 
             'd': 331, 
             'D': 350,
             'n': 371,
             'N': 394,
             "S'": 416}
    for n in (list(SCALE.keys())):
        if n.isupper():
            print(n)
            w.Beep(SCALE.get(n), 1000)
    while True:
        seq = mlinput('Please enter a sequence of notes. >>> ')
        for note in seq:
            try: 
                if note == '-':
					f.playtone(SCALE.get(note), 300)
            except TypeError:
                pass
			    
musicMaker()        
    
    