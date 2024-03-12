#LIST PROGRAMS

#1.Find the largest and the smallest numbers in a list.
l=eval(input("Enter a list of integers: "))
print("Largest number in the list: ",max(l))
print("Smallest number in the list: ",min(l))


#2. Find the third largest number in a list.
#l=eval(input("Enter a list of integers: "))
l.sort()
print("Third largest number in the list: ",l[-3])

#3.Write a python program to take a list of integers.
#Create another list with those numbers in the master list that are less than
#a number entered by the user.Print the new list contents.

lnew=[]
#l=eval(input("Enter a list of integers: "))
x=int(input("Enter limit: "))

for i in l:
    if(i<x):
        lnew.append(i)
print("New list:", lnew)

#4. Write a python program to take a list of integers.Create another list to store all the
#even numbers from the master list and print the new list contents in ascending order.

#l=eval(input("Enter a list of integers: "))
evenl=[]
for i in l:
    if(i%2==0):
        evenl.append(i)
print("list of even no: ",evenl)

#5.Write a python program to take two lists of inegers and return a list containging
#the elements that are common in both the list. Also print the contents of the new list.

l1=eval(input("Enter 1st integer list: "))
l2=eval(input("Enter 2nd integer list: "))
common_l=[]
s1=len(l1)
s2=len(l2)
for i in range(0,s1):
    if (l1[i] in l2):
        common_l.append(l1[i])
print("List containg common elements:", common_l)


    
