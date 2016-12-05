import re
exp = raw_input('Enter a regular expression: ')
fname = 'mbox.txt'
fhand = open('../data/'+fname)
count = 0
for line in fhand: 
    if re.search(exp,line):
        # print 'Found!'
        count += 1
print fname+' had '+str(count)+ ' lines that matched '+exp