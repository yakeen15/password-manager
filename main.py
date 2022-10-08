import random as rng
import string

def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

def stripIDpass(line):
    idpass = []
    i = line.find(',')
    idpass.append(line[0:i])
    idpass.append(line[i+1:len(line)-1])
    return idpass

def gen(pwc):
    str1 = ""
    for ele in pwc:
        str1 += ele
    return str1


def fileFunction(psd):
    f = open("datafile.csv","r+")
    print("Enter a id to store with the pass")
    alltext = f.readlines()
    #print(alltext)
    idVal = str(input())
    lineNum = 0
    flag = 1
    for line in alltext:
        idpassval = stripIDpass(line)
        #print(line[0])
        if idpassval[0] == idVal:
            print("The id already exists\n1. Overwrite\n2. Terminate")
            choice = int(input())
            if choice == 1:
                replace_line(f,lineNum,idVal+','+psd+'\n')
            flag = 0
            break
        lineNum = lineNum + 1
    if flag == 1:
        f.write(idVal+','+psd+'\n')
    f.close()

def genPass():
    pwc = []

    print("Length of password?")
    n = int(input())

    for i in range(0,n):
        pwc.append(rng.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits))


    pwd = gen(pwc)
    print(pwd)
    print("Would you like to store this password? (1 for yes)")
    choice = int(input())
    if choice == 1:
        fileFunction(pwd)

def managePass():
    f = open("datafile.csv","r")
    print("1. List all id-pass pairs\n")
    choice = int(input())
    if choice == 1:
        alltext = f.readlines()
        for line in alltext:
            print(stripIDpass(line))


print("1. Generate random password\n2. Manage password")

choice = int(input())
if choice == 1 :
    genPass()
elif choice == 2 :
    managePass()
 