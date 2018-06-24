file = open("copy.txt","w")
file.write("hello everyone \n my name is shagun \n from \n MCA")

file.close()
with open("copy1.txt","w") as file:
    file.write("HELLO \nI AM SHAGUN \nFROM MCA \nIN \nLPU")
file.close()
with open('copy.txt') as fh1, open('copy1.txt') as fh2:
    for line1, line2 in zip(fh1, fh2):
        print(line1+line2)