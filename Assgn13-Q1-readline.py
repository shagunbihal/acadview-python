f=open("read.txt","r")
line_read=f.readline()
while(line_read!=""):
    print(line_read)
    line_read=f.readline()
f.close()