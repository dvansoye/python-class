emails = dict()
fname = raw_input("Enter file name: ")
try:
    fhand = open('../data/'+fname)
except:
    print 'File cannot be opened: ', fname
    exit()
    
for line in fhand:
    words = line.split()
    if len(words) > 3 and words[0] == 'From':
        email = words[1]
        emails[email] = emails.get(email,0) + 1

print emails