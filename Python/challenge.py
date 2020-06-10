subjects = list(range(100))
verbs = list(range(100))
nouns = list(range(100))
for i in subjects:
    for k in verbs:
        for l in nouns:
            print(str(i) +' ' + str(k) + ' ' + str(l))
