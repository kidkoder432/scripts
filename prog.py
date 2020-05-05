import os
prog = input('Which program should I run? > ')
os.chdir('home/runner/scripts/Python')
execfile(prog)

