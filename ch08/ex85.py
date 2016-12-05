fhand = open ("../data/mbox-short.txt")
count = 0
for line in fhand :
    line = line.rstrip()
    # print line
    words = line.split(" ")
    if words[0] == 'From' :
        print words[1]
        count = count + 1
print "There were " + str(count) + " lines in the file wor From as the first word"