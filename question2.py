# find if the given number is a palindrome or not?
a=int(input("enter num:"))
if(str(a)==str(a)[::-1]):
   print("a is palindrome")
else:
    print("it is not a palindrome:")   
