#READ ME :- wherever path "/path/of/file/file.c" is given change it with your own file.c path
# This script extract functions from .c file and print it on the terminal
# You can redirect it to the file for example -> python3 file.c > all_fun_def.c
# The [extract] function gets the 'start' and 'end' of function line number , you can do with whatever you like
# you can contact me at sajjads26@gmail.com  

import re
import linecache


def extract(start,end ):
    #print("function found at",start,end)
    for i in range(start,end+1):
        print(linecache.getline("/path/of/file/file.c",i),end='')

		

def count( line,start ):

	f = open("/path/of/file/file.c","r")
	end=0
	counter = 0

	for line in f:
		end=end+1
		if(end > start):
			if ('{' in line):
				counter = counter + 1
			if ('}' in line):
				counter = counter - 1
				
			if ( counter == 0):
				extract(start,end )
				return


f = open("/path/of/file/file.c","r+")
start=0
flag1=0


for line in f:
    start=start+1
    if ('(' in line) and line.endswith(')\n') :
        if linecache.getline("/path/of/file/file.c",start+1) == '{\n':
            count(line,start)
