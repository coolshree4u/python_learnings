read = open("/home/qa_shree/python_programs/python_learnings/python_begainer_s/file_io/sample.txt")

for line in read:
    print(line)

read.close()

# with readline()
with open("sample.txt","r") as read:
    line = read.readline()
    while line:
        print(line, end='')
        line=read.readline()

read.close()


#with readlines()
with open("sample.txt","r") as read:
    line = read.readlines()
print(line)
read.close()

with open("dummy.txt","r") as read:
    line = read.readlines()
print(line)
read.close()
