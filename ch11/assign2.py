# print sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] )

import re
fname = raw_input('Enter filename: ')
if len(fname) == 0: fname = 'regex_sum_42.txt'
try:
    fhand = open(fname)
except:
    print "Can't open file. Please try again."
    exit()

print sum( [int(i) for i in re.findall('[0-9]+', fhand.read())] )