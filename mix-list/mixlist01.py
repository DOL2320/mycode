#!/usr/bin/env python3

# create a list containing three items
my_list = ["192.168.0.5", 5060, "UP" ]

# display the first item in the list
print("The first item in the list (IP): " + my_list[0] )

# display the second item in the list
print("The second item in the list (port): " + str(my_list[1]) )

# display the third item in the list
print("The last item in the list (state): " + my_list[2] + "\n"  )

# create a new list
iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

#print only the ip addresses
print("The ip address from iplist:", iplist[3], iplist[4])

# create a word bank list
wordbank= ["indentation", "spaces"]

# append 4 to wordbank
wordbank.append(4)
spaces = wordbank[1]
four = wordbank[2]

# create a tlg students list
tlgstudents= ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory", "Ebrima", "Franco", "Greg", "Hoon", "Joey", "Jordan", "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]
tlgstudents_size = str(tlgstudents.__len__())

# include an input asking for a number between 0 and 18
num = int(input("Enter a number between 1 and " + tlgstudents_size + ": "))

# using num return the name of the student at that position
student_name = tlgstudents[num - 1]

print(f"{student_name} always uses {four} {spaces} to indent.")
