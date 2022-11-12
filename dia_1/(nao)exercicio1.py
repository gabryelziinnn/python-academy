l1 = '123456789123456789123456789123456789123456789'
l2 = []
l2.append(l1)



print()



test_list = [1, 4, 5, 6, 7, 3]

# printing original list
print ("The original list is : " + str(test_list))

# using list comprehension
# to assign variables from list element
var1 = [test_list[i] for i in (1, 3, 5)]

# printing result
print ("The variables are : " + str(var1) )
#						" " + str(var2) +
#							" " + str(var3))
