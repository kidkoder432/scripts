import winsound, time
NOTES = {
'S': 220
}
print('''WELCOME TO TAGTUNE!


HOW TO PLAY:
The computer will select a random note from P lower to P higher. You must
figure out what the note is and add one more note to create a melody. 
Note: seperate notes with spaces. For example: S n" D" P" d" N"
The computer will then beep the melody you have typed out and add 
its own note to the existing melody. Repeat.

KEY:
S r R g G M m P d D n N: These are the notes that TagTune can play.
' ": These are modifiers that tell TagTune which scale to play the note in. 
For high scale (Taar saptak) the modifier is ' (apostrophe). 
For low scale (Mandra saptak) it is " (quote).




''')
time.sleep(2)
print('The following beep will be of Sa (kharaj).')
winsound.Beep(220, 1000)



