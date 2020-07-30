import os, pyautogui

sep = ['backup files\\', 'prajwal_files\\']
for i in range(2):
    ext = input('Which file extension would you like to search for? > ')
    folder = input('Which directory should I search? > ')
    save = input('Where should I save the file? > ')
    fl = open(os.path.join(save, 'files.txt'), 'w')
    # fl.write('Files ending with %s in %s\n\n' %(ext, folder))
    for r, d, f in os.walk(folder):
        for file in f:
            # if file.endswith('.txt') or file.endswith('.py'):
            print(os.path.join(r, file))
            text = list(os.path.join(r, file).partition(sep[i]))
            del text[:2]
            text = ''.join(text)
            fl.write(text + '\n')
    fl.close()





# f = open('c:\\users\\findp\\files.txt')
# for file in f.read().split(' '):
#     try:
#         fl = open(file)
#         print(file + '\n\n')
#         print('-' * 100)
#         print(fl.read())
#         print('-' * 100)
#         input('Next? ')
#         #pyautogui.press('enter')
#     except:
#         print('Error on file %s' %(file)) 
#         continue