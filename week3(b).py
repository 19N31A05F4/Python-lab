#check whether the entered string is palindrome or not
string=input(("Enter the string:"))  
if(string==string[::-1]):  
      print("The entered string is palindrome")  
else:  
      print("The entered string is not palindrome")  
