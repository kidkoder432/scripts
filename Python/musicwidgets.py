import winsound as w, re
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
        How to Use:
            syntax:
                - = pause for {rest} seconds
                set = notation set. Pick from piano(CDEFGABC), solfege(DRMFSLTD), or Indian(SRGMPDNS)
                note = a note in the chosen set. 
                    If lowercase, note willl be flatter(except for F, Fa, or M, where note will be sharper). 
                    Default play time is {play} seconds 
                    ex. S---, n, f, M 
                ' = Used to indicate the scale. Use none for medium scale, one apostrophe for high scale, and two for low scale
                tempo = The tempo at which to play the music. Value from 1 to 500
                {play} = How long to play a note.''')
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
                w.Beep(SCALE.get(note), 300)
            except TypeError:
                pass    
musicMaker()        
    
    