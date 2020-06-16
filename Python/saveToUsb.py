import os, shutil, send2trash, time
if os.path.exists('e:\\backup_files'):
    send2trash.send2trash('e:\\backup_files')
    print('Backup removed.')

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
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        print(item, get_size(s), 'B')
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)
backup = input('Which folder should I back up? Note: can only be up to %s GB in size. > ' %(shutil.disk_usage(os.path.realpath('E:\\'))[2] / 1000000000))
if os.path.exists('E:\\'):
    print('Copying...')
    start = int(time.time())
    copytree(backup, 'e:\\backup_files')
    end = int(time.time())
    speed = (get_size(backup) / 1000000) / (end - start)
    print('''Summary:
    Copied %s files
    Total size: %s MB
    Speed: %s MB/s''' %(len([name for name in os.listdir(backup) if os.path.isfile(name)]), get_size(backup) / 1000000, speed))
    print('Done.')
else:
    print('No drive found.')