import os, shutil
if os.path.exists('e:\\backup files'):
    print('Backup already exists. Please delete the backup folder and re-run the program.')
    exit(0)
def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        print(item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)
if os.path.exists('E:\\'):
    print('Copying...')
    copytree('c:\\users\\findp\\onedrive\\documents\\prajwal_files', 'e:\\backup files')
    print('Done.')
else:
    print('No drive found.')