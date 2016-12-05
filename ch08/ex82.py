fhand = open('../data/mbox-mod.txt')
count = 0
for line in fhand:
    words = line.split()
    if len(words) < 2 : continue
    if words[0] != 'From' : continue
    # print len(words), line
    print words[2]