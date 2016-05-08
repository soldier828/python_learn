# -*- coding: utf-8 -*-
formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ('one','two','three','four')
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
		"I had this thing.",
		"THat you could type up right.",
		"But it didn't sing.",
		"I said goodnight."
		
)
# 显示汉字 可以直接 print "傻逼"
# 如果想用格式，用%s 因为%r显示的是raw，若用来显示汉字，会变成utf-8中的汉字代号