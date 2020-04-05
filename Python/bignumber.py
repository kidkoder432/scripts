import pyperclip
bignumber = ["1"]
for i in range(100000):
    bignumber.append(", ")
    bignumber.append("000")
bignmber = "".join(bignumber)
pyperclip.copy(bignumber)
