counter = { }
infile = open("poverbs.txt", "r")
for line in infile:
    line = line.rstrip()
    word_list = line.split()
    for word in word_list:
        '''print(word)'''
        word = word.replace(".","")
        if word in counter:
            counter[word] = counter[word] + 1
        else:
            counter[word] = 1

for key in sorted(counter.keys()):
    print(key, counter[key])
infile.close()
