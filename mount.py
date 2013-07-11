#!/usr/bin/env python
f = open("/proc/mounts")
s = f.readlines()# reads the file line by line.
for i in s[1:]:# for loop which controls the position in the file.
    ns = i.split(" ")#spliting the file line by line according to spaces.
    del ns[-2]#The required manipulations are done.
    del ns[-1]
    ns.insert(2,"type ")
    ns.insert(1,"on")
    ns.insert(5,"(")
    ns.insert(7,")")
    str = " ".join(ns)#joining the splitted string using the join() function
    print str #printing the desired output.
f.close()#lastly, the file is closed.
