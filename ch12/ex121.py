import socket

url = raw_input("Please enter URL to open (don't include the HTTP://): ")
url = url.split('/',1)

print url
uhost =  url[0]
udoc = url[1]
print uhost
print udoc

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysock.connect((uhost, 80))
    mysock.send('GET http://' + uhost + '/' + udoc + ' HTTP/1.0\n\n')
except:
    print 'Could not open URL. Please try again'
    quit()

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print data;

mysock.close()