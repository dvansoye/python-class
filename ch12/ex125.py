import socket
import re

url = raw_input("Please enter URL to open (don't include the HTTP://): ")
url = url.split('/',1)

# print url
uhost =  url[0]
udoc = url[1]
# print uhost
# print udoc

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysock.connect((uhost, 80))
    mysock.send('GET http://' + uhost + '/' + udoc + ' HTTP/1.0\n\n')
except:
    print 'Could not open URL. Please try again'
    quit()

chars = 0
while True:
    data = mysock.recv(5000)
    if ( len(data) < 1 ) :
        break

    # start here. problem: .* stops at the end of the line
    # and does not continue processing.
    # I'm looking for \n\n but it never gets that far
    
    data = re.findall('^HTTP/1.1 200 OK.*\n(.*)', data)
    print data
    quit()
    
    chars = chars + len(data)
    if chars <= 3000:
        print '***BEG***', data;

mysock.close()
print 'File size:',chars