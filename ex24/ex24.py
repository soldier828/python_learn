print "Let's practice everything."
print 'You\'d need to know \'bout esacepes with \\ that do \n newlines and \t tabs.'

poem = '''
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
\n\t\twhere there is none.
'''

five = 10 -2 +3 -6
print "This should be five: %s" % five

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula
