# This script goes through all the functions in a file and put Debug statement just after curley braces of function is detected printf("%s%d\\n",__FILE__,__LINE__); 
# How to use -> wherever /path/of/file.c is given change it with your own file path , it prints new content on terminal ,you can redirect it to a file
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


