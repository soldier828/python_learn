from sys import argv
script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Typethe filename again"
file_again = raw_input("> ")

txt_agian = open(file_again)

print txt_agian.read()