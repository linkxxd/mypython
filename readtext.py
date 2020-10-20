openfile=input("输入需要整理的文件名:")
f=open(openfile)
n=open('new.txt','w')

for line in f.readlines():
    line = line.strip()
    line = line.strip('\n')
    if not line == "":
        newinfo = line.split("：")[-1]
        print(newinfo)
        n.write(newinfo + ":")
    else:
        n.write("\n")

n.close()
