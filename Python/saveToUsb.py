import os, shutil, send2trash, time
if os.path.exists('e:\\files'):
    print('The program cannot proceed because a backup already exists. Please delete the backup and press Enter when done.')
    input()

def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size


def copytree(src, dst, symlinks=False, ignore=None):
    os.mkdir(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        print(item, get_size(s), 'B')
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)
backup = 'c:\\users\\findp\\onedrive\\documents\\prajwal_files'#input('Which folder should I back up? Note: can only be up to %s GB in size. > ' %(shutil.disk_usage(os.path.realpath('E:\\'))[2] / 1000000000))
while True:
    if os.path.exists('E:\\') and get_size(backup) < shutil.disk_usage(os.path.realpath('E:\\'))[2]:
        print('Copying...')
        start = int(time.time())
        copytree(backup, 'e:\\files')
        end = int(time.time())
        speed = (get_size(backup) / 1000000) / (end - start)
        numFiles = 0
        for r,d,f in os.walk(backup):
            for file in f:
                numFiles += 1
        print('''Summary:
        Copied %s files
        Total size: %s MB
        Speed: %s MB/s''' %(numFiles, get_size(backup) / 1000000, speed))
        print('Done.')
        break
    else:
        print('The drive has not been plugged in, or its capacity is too small to store the backup. Please resolve these issues and press Enter when done.')
        input()