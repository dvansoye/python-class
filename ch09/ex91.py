import re
xdict = dict()
fhand = open('../data/words.txt')
for line in fhand:
    # words = line.split(' {}')
    words = re.findall(r"[\w]+", line)
    for word in words:
        word = word.lower()
        xdict[word] = 'foo'

print len(xdict)
print 'Writing: ', 'Writing' in xdict
print 'programs: ', 'program' in xdict
print 'monty: ', 'monty' in xdict
print xdict