emails = dict()
fname = raw_input("Enter file name: ")
try:
    if len(fname) == 0: fname = 'mbox-short.txt'
    fhand = open('../data/'+fname)
except:
    print 'File cannot be opened: ', fname
    exit()
    
for line in fhand:
    words = line.split()
    if len(words) > 3 and words[0] == 'From':
        email = words[1]
        emails[email] = emails.get(email,0) + 1

table = list()
for email, count in emails.items():
    table.append( (count, email) )

table.sort(reverse=True)
count, email = table[0]
print email, count