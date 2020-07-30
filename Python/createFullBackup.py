import os, shutil
if os.path.exists('e:\\backup_files'):
    #send2trash.send2trash('e:\\backup_files')
    print('''Program cannot proceed because backup_files already exists. Please remove the 
    backup_files folder and press Enter when finished''')
    input()


def copytree(src, dst, symlinks=False, ignore=None):
    os.mkdir(dst, exist_ok = True)
    for r, d, f in os.walk(src):
        for file in f:
            shutil.copy2(os.path.join(r, file), dst)
while True:            
    if os.path.exists('E:\\') and shutil.disk_usage(os.path.realpath('e:\\'))[2] > 300000000000:  #check for a backup drive instead of a thumb drive
        print('Copying...')
        copytree('c:\\', 'e:\\backup_files')
        print('Done.')
        break
    else:
        print('No drive found. Connect a backup drive with at least 300 GB of free storage and press Enter.')
        input()
        continue