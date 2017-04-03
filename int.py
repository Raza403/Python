# Take inputs
import cs50

x = cs50.get_int()
y = cs50.get_int()
print ("{} plus {} is {}".format(x,y,x+y))
print ("{} minus {} is {}".format (x,y,x - y))
print ("{} mult {} is {}".format(x,y,x*y))
print ("{} divided by {} is {}".format (x,y,x/y))
print ("{} divided by and floored {} is {}".format (x,y,x // y))
print ("{} modulus {} is {}".format (x,y,x%y))