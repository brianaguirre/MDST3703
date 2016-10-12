__author__ = 'BrianAguirre'

def generate_list(x):
    list = []
    for i in range(0,x):
        list.append(i)
    return list

def add_lists(x,y):
    total = []
    carry_out = 0
    list1 = backwards(x)
    list2 = backwards(y)
    addition = 0
    counter = 0

    if len(list1) > len(list2):
        counter = len(list2)
        for i in range(0, counter):
            addition = list1[i] + list2[i] + carry_out
            if addition > 9:
                addition -= 10
                total.append(addition)
                carry_out = 1
            else:
                total.append(addition)
                carry_out = 0
        counter = len(list2)
        for j in range(counter, len(list1)):
            addition = list1[j] + carry_out
            if addition > 9:
                addition -= 10
                total.append(addition)
                carry_out = 1
            else:
                total.append(addition)
                carry_out = 0


    #IF LIST 1 IS SHORTER THAN LIST 2:
    elif len(list1) < len(list2):
        counter = len(list1)
        for i in range(0, counter):
            addition = list1[i] + list2[i] + carry_out
            if addition > 9:
                addition -= 10
                total.append(addition)
                carry_out = 1
            else:
                total.append(addition)
                carry_out = 0
        #CONTINUE ADDING THE REST OF THE REMAINING NUMBERS:
        counter = len(list1)
        for j in range(counter, len(list2)):
            addition = list2[j] + carry_out
            if addition > 9:
                addition -= 10
                total.append(addition)
                carry_out = 1
            else:
                total.append(addition)
                carry_out = 0
    else:
        #LENGTHS ARE THE SAME:
        counter = len(list1)
        for i in range(0, counter):
            addition = list1[i] + list2[i] + carry_out
            if addition > 9:
                addition -= 10
                total.append(addition)
                carry_out = 1
            else:
                total.append(addition)
                carry_out = 0
        #CONTINUE ADDING THE REST OF THE REMAINING NUMBERS:
        counter = len(list1)
        for j in range(counter, len(list2)):
            addition = list2[j] + carry_out
            if addition > 9:
                addition -= 10
                total.append(addition)
                carry_out = 1
            else:
                total.append(addition)
                carry_out = 0
        if (carry_out == 1):
            total.append(1)
    return backwards(total)

def backwards(x):
    list = []
    for i in reversed(x):
        list.append(i)
    return list

def pandigital(x):
    panset = set([1,2,3,4,5,6,7,8,9])
    first_nine = set(x[:9])
    last_nine = set(x[len(x)-9:])
    if (panset.issubset(first_nine)) and (panset.issubset(last_nine)):
        return True
    else:
        return False

def pandigital_first(x):
    panset = set([1,2,3,4,5,6,7,8,9])
    first_nine = set(x[:9])
    if (panset.issubset(first_nine)):
        return True
    else:
        return False

def pandigital_last(x):
    panset = set([1,2,3,4,5,6,7,8,9])
    last_nine = set(x[len(x)-9:])
    if (panset.issubset(last_nine)):
        return True
    else:
        return False

def fib1():
    list1 = [1]
    list2 = [1]
    is_pandigital = False
    i = 3

    while (is_pandigital == False):
        list3 = add_lists(list1,list2)
        if pandigital(list3):
            print (str(i) + " is pandigital 1-9")
            is_pandigital = True
        i+=1
        print (i)
        list1 = list2
        list2 = list3


fib1()
