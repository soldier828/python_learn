# -*- coding:utf-8 -*-
from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C"
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file ...."
target = open(filename, 'w+') # w only write;r only read
							 # w+ r+ a+  write & read

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "%r" % line1
print "I'm going to write these to the file."

#write
target.write(line1) #不能把\n加在这里，虽然line1的%r 带引号，
target.write("\n")  #但是line1毕竟是一个变量，所以要在这行换行
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

#read
target.readline()   
print "And finally, we close it."
target.close()