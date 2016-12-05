hours = dict()
fname = raw_input("Enter file name: ")
try:
    if len(fname) == 0: fname = 'mbox-short.txt'
    fhand = open('../data/'+fname)
except:
    print 'File cannot be opened: ', fname
    exit()
    
for line in fhand:
    words = line.split()
    if len(words) > 6 and words[0] == 'From':
        time = words[5]
        temp = time.split(':')
        hour = temp[0]
        # print 'time>> ', time, 'hour', hour
        hours[hour] = hours.get(hour,0) + 1

# print hours

table = list()
for hour, count in hours.items():
    table.append( (hour, count) )

table.sort()

for hour, count in table:
    print hour, count