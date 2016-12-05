fname = raw_input("Enter file: ")
fhand = open("../data/"+fname)
ledger = list()
for line in fhand :
    line = line.rstrip()
    words = line.split(' ')
    print line
    print words
    for word in words :
        if not (word in ledger) :
            ledger.append(word)
            print "Added: " + word
            print "Ledger: ", ledger
ledger.sort()
print ledger