# -*- coding: utf-8 -*-
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said : %r." % x
print "I also said: '%s'." % y
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r" # 还能在字符串中内嵌格式符号

print joke_evaluation % hilarious  # 格式符号在这里才插入

w = "This is the left side of..."
e = "a string with a right side."

print w + e

# What is the difference between %r and %s?
# Use the %r for debugging, since it displays the "raw" data of the variable, 
# but the others are used for displaying to users.
# 就是说r(raw)显示的是这个变量的原始信息，如果你定义的时候带引号，就带。
# 定义的是啥，显示就是什么