import re
import linecache

f = open("/path/of/file.c","r+")
start=0
flag=0
for line in f:
    start=start+1
    if ('(' in line) and line.endswith(')\n') :
        if linecache.getline("/path/of/file.c",start+1) == '{\n':
            flag = 2
    print(line,end='')
    flag = flag-1
    if flag == 0:
        print('printf("%s%d\\n",__FILE__,__LINE__);')  
        flag =-1


