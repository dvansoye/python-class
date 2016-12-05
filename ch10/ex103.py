import string
letters = dict()
fname = raw_input("Enter file name: ")
try:
    if len(fname) == 0: fname = 'mbox-short.txt'
    fhand = open('../data/'+fname)
except:
    print 'File cannot be opened: ', fname
    exit()

total = 0    
for line in fhand:
    # print "before: ", line
    # line = line.rstrip()
    line = line.translate(None, string.punctuation+' 0123456789\t\n')
    line = line.lower()
    # print "after: ", line
    if len(line) > 0:
        for character in line:
            # print character
            letters[character] = letters.get(character,0) + 1
            total = total + 1
    # print letters
    # quit()

# print letters

table = list()
for letter, count in letters.items():
    table.append( (letter,count) )
    
table.sort()

for letter, count in table:
    print letter, count, float(count)/float(total)*100

print total