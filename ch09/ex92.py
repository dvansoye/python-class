filename = raw_input("Enter a file name: ")
fhand = open('../data/'+filename)
days = dict()
for line in fhand:
    words = line.split()
    if len(words) > 3 and words[0]=="From":
        day = words[2]
        days[day] = days.get(day,0) + 1
print days