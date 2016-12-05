domains = dict()
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
        domain = email[email.find('@'):]
        # print domain
        domains[domain] = domains.get(domain,0) + 1

print domains