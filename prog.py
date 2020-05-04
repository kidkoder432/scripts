import os, subprocess
prog = str(input('Which program should i run? > '))
subprocess.call("python3 " + prog + '.py')