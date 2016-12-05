count = 0 
total = 0.0
filename = raw_input("Enter file name: ")
try:
    mbox = open('../data/'+filename)
except:
    print "Could not open file"
    exit()

for line in mbox:
    loc = line.find('X-DSPAM-Confidence:')
    if loc == -1:
        continue
    count = count + 1
    total = total + float(line[loc+20:].rstrip())

print 'Average spam confidence: ' + str(total/count)
    