#!/usr/bin/python
"""var = 1
while var == 1 :# This constructs an infinite loop
    num = raw_input("Enter a number :")
    print "You entered: ", num
print "Good bye!"
"""

import time

print "========================================="
fruits = ['banana', 'apple',  'mango', 'a']
print range(len(fruits))
for index in range(len(fruits)):
    print 'Current fruit :', fruits[index]
print "Good bye!"
print "========================================="
print "My name is %s and weight is %E kg!" % ('Zara', 21)

dict = {'Name': 'Zara', 'Age': 7};
print "Variable Type : %s" % type (dict)
print "========================================="
dict = {'Name': 'Zara', 'Age': 7};
print "Start Len : %d" %  len(dict)
dict.clear()
print "End Len : %d" %  len(dict)
print "========================================="
dict = {'Name': 'Zabra', 'Age': 7}
print "Value : %s" % dict.get('Age')
print "Value : %s" % dict.get('Education', "Never")
print "========================================="

t = time.localtime()
print "time.asctime(t): %s " % time.asctime(t)
t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
t = time.mktime(t)
print time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t))

