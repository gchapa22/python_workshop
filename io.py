
# OUTPUT
# ---------------
print "Spam"
print 1
print None
x = 100
print x
print 'We are the {} who say "{}!"'.format('knights', 'Ni')
print '{0} and {1}'.format('spam', 'eggs')
print '{1} and {0}'.format('spam', 'eggs')
print 'This {food} is {adjective}.'.format(
		food='spam', adjective='absolutely horrible')

# INPUT
# ---------------
x = raw_input()
import getpass
x = getpass.getpass()

# Archivos
f = open('file','w')
f.read()
f.readline()
f.write("Spam\n")

