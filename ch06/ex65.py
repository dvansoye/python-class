str = 'X-DSPAM-Confidence: 0.8475'
strpos = str.find(" ")
con = float(str[strpos+1:])
print "Confidence %g " % con