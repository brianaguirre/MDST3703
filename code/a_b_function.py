__author__ = 'BrianAguirre'

"""
Given a list, which contains n number of digits, assign all the odd position numbers 'a' and even 'b'
If for any sequence in the list an a number is greater than the following b number, return false
Else return true

Assumption:
If the list is empty return False
If there are n numbers in the list and n is odd then return true if true for all values n-1, thus
Base case if n == 1, return True
"""

def a_b_pattern(list1):
    length  = len(list1)
    result = True
    if length == 0:
        return False
    elif length == 1:
        return True
    elif length > 1:
        for i in range (0, length-1):
            if (list1[i] > list1[i+1]):
                result = False
        return result
    else:
        return False


list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
list3 = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
list4 = [1,2,3,4,5,6,7,8,9,10,12,4]
list5 = []
list6 = [1]
list7 = [-10,-9,-8,-7]
list8 = [-10,-11,-12,-13]
list9 = [-1,0,3]


print(a_b_pattern(list1))
print(a_b_pattern(list2))
print(a_b_pattern(list3))
print(a_b_pattern(list4))
print(a_b_pattern(list5))
print(a_b_pattern(list6))
print(a_b_pattern(list7))
print(a_b_pattern(list8))
print(a_b_pattern(list9))
