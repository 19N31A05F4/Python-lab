#python program to given string and numis palindrome or not and return the value
input_string=input("Enter any string:")
if input_string==input_string[::-1]:
  print("Palindrome",input_string)
else:
  print("not a Palindrome",input_string)