import pyautogui as p, time, os
os.chdir('c:\\users\\findp\\3d objects\\book')
input('Press Enter when ready to start. > ')
for i in range(18):
    p.click(960, 340)
    for j in range(75):
        p.screenshot('Page %s-%s.png' %(i + 1, j + 1))
        for k in range(7):
            p.press('down')
    p.click((1855, 109))
    time.sleep(1)

