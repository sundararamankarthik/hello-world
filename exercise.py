#https://www.practicepython.org/

def getUserInput():
    return int(raw_input('Enter your number'))

#Exercise 2
#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

def exercise_2():
    number = raw_input("Enter your number: ")
    your_number = int(number)

    if your_number % 2 == 0:
        print 'Number is even'
    else:
        print 'Number is odd'
    
#End of Exercise 2


#Exercise 3
#Take a list, say for example this one:

#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less than 5.
def exercise_3():

    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = []
    ip = raw_input('provide your input')
    user_input = int(ip)

    for element in a:
        if element < user_input:
            print element
            b.append(element)

    print 'New list is',b


#Exercise 4
def exercise_4():
    user_input = getUserInput()
    divisor = []
    i = 1
    while i <= user_input:
        if user_input % i == 0:
            print i
            divisor.append(i)
        i = i +1
    print 'Divisors are', divisor
            

#Exercise 5


#Take two listsand write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
def exercise_5():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 1, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c=[]

    
    for b_element in b:
        for a_element in a:
            if b_element == a_element:
                c.append(b_element)


    c.sort()

    for item in c:
        count = c.count(item)
        c = c[count-1:]

    

    print 'Common elements are',c




















#Call the exercise number that you want to run

exercise_5()
