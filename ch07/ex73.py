count = 0 
total = 0.0

filename = raw_input("Enter file name: ")
if filename == "na na boo boo":
    print "NA NA BOO BOO TO YOU - You have been punk'd!"    
    exit()
    
try:
    mbox = open('../data/' + filename)
except:
    print "File cannot be opened: "+filename
    exit()

for line in mbox:
    loc = line.find('Subject:')
    if loc == -1:
        continue
    count = count + 1
 
print 'There were ' + str(count) + " subject lines in " + filename