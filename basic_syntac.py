#!/usr/bin/python
import sys
# contoh list
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print list
print list[0]
print list[1:3]
print list[2:]
print tinylist * 2
print list + tinylist # Prints concatenated lists

# contoh tuples
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')
print tuple
print tuple[0]
print tuple[1:3]
print tuple[2:]
print tinytuple * 2
print tuple + tinytuple # Prints concatenated lists


userName = 'Peter'
userSpouseName = "Janet"
userAge = '30'
print userName.upper()

a = 21
b = 10
c = 0
c=a+b
print "Line 1 - Value of c is ", c
c += a
print "Line 2 - Value of c is ", c
c *= a
print "Line 3 - Value of c is ", c
c /= a
print "Line 4 - Value of c is ", c
c=2
c %= a
print "Line 5 - Value of c is ", c
c **= a
print "Line 6 - Value of c is ", c
c //= a
print "Line 7 - Value of c is ", c
