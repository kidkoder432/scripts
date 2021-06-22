rows = input('How many rows? > ')
columns = input('How many columns? > ')
MAX_DIGITS = len(str(int(columns) * int(rows)))
f = open('table.txt', 'w')
for column in range(int(columns) + 1):
    f.write(str(column) + ' ' * MAX_DIGITS)
f.write('\n')
for row in range(1, int(rows) + 1):
    f.write(str(row) + ' ' * (MAX_DIGITS + 1 - len(str(row))))
    for column in range(1, int(columns) + 1):
        res = row * column
        f.write(str(res) + ' ' * ((MAX_DIGITS + 1 - len(str(res)))))
    f.write('\n')
f.close()
