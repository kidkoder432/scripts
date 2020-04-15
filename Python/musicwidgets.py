import winsound as w, re
def mlinput(prompt):
    ui = None
    print(prompt)
    totalui = []
    while ui != '':
        ui = input()
        totalui.append(ui)
    return '\n'.join(totalui)


     
def tabla():
    print('''Welcome to Tabla!''')
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
    
    
