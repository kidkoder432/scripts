import os, time
def mlinput(prompt):
    ui = None
    print(prompt)
    totalui = []
    while ui != '':
        ui = input()
        totalui.append(ui)
    return '\n'.join(totalui)  
SCALE = {'S': 208 	
'r': 220
'R': 233 	
'g': 247 	
'G': 262 	
'M': 277 
'm': 294 	
'P': 311 	
'd': 330 	
'D': 349 	
'n': 370 	
'N': 392}
def play(f, d):
    '''f: frequency in Hz\n
    d: duration in milliseconds'''
    os.system('play -n --no-show-progress synth %s sin %s' % (d / 1000, f))

def musicMaker():
    print('''Welcome to MusicMaker!
             Syntax:
                 " " used to indicate the next group of notes
                 "" used to indicate a fast note delay''')

    for n in (list(SCALE.keys())):
        if n.isupper():
            print(n)
            play(SCALE.get(n), 1000)
    while True:
        seq = mlinput('Please enter a sequence of notes. >>> ')
        for note in seq.split('  '):
            
            for n in note.split(' '):
                try:
                    if len(note) > 1:
                        play(SCALE.get(n), 150)
                    elif seq[seq.index(note) + 1] == '-': 
                        play(SCALE.get(n), 600)
                    else:
                        play(SCALE.get(n), 300)
                except (TypeError, IndexError):
                    pass
musicMaker()        
    
    
