import turtle as t, time, gzip, saveImageAsText
f = gzip.open('imageBytes.txt', 'r')
content = f.read().decode('utf-8')
rows = content.split('        ')
t.setup(len(rows), len(rows[0].split('  ')), 0, 0)
for y in range(len(rows) - 1):
    