string = '   X-DSPAM-Confidence: 0.8475   '
stripped = string.strip()
print "stripped>"+stripped+"<"

replaced = string.replace("DSPAM","XXXXX")
print "replaced>"+replaced+"<"