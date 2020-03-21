num = 1
den = 4
frac = num/den
for i in range(100):
    den *= 4    
    new = num/den
    frac += new
frac *= 18
print(int(frac))
