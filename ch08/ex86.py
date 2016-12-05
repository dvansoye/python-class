numbers = list()
number = raw_input("Enter a number: ")
while number != "done" :
    numbers.append(float(number))
    number = raw_input("Enter a number: ")
print numbers
minnum = min(numbers)
maxnum = max(numbers)
print "Maximum: ", maxnum
print "Minimum: ", minnum