
#modules = modules.split()
#This program gathers all the modules in python and gets help on them using
#the help() function.

import sys

module = 'print'
try:
    print('Writing to ' + module + '.txt.')
    
    filename =  'HELP_' + module + '.txt'
    f = open(filename, 'a+')
    help(module)
    f.write(str(sys.stdout))
    f.close()
    
    
except:
    print('Error on module ' + module)
##        import winsound
##        winsound.Beep(1000, 1000)
f = open(filename)
content = f.read()
f.close()
#if content == doc:
 #   print('Success!')
#else:
#    raise Exception('The text in ' + module + ' did not copy correctly. [Errno 3]')



print('Done')
raise Exception('Program end.')


