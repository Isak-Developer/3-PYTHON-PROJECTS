print("Welcome to PYTHON Quiz!")
person=input("Do you want to start quiz?" ).lower()
if person != "yes":
    quit()
else:
    print("Okay! let's play")


print('What is a correct syntax to output "Hello World" in Python?:' )
print('A. print("Hello World")')
print('B. echo("Hello World");')
print('C. p("Hello World")')
print('D. echo "Hello World"')

answer=input("Choose the answer" ).lower()
scrore=0
if answer=="a":
    print("correct")
    scrore +=1
else:
    print("incorrect")


print('''How do you insert COMMENTS in Python code?''' )
print('A. #This is a comment')
print('B. //This is a comment')
print('C. /*This is a comment*/')

answer=input("Choose the answer" ).lower()
if answer=="a":
    print("correct")
    scrore +=1
else:
    print("incorrect")


print('''Which one is NOT a legal variable name?''' )
print('A. _myvar ')
print('B. my-var')
print('C. Myvar')
print('C. my_var')

answer=input("Choose the answer" ).lower()
if answer=="b":
    print("correct")
    scrore +=1
else:
    print("incorrect")


print('''How do you create a variable with the numeric value 5?''' )
print('A. x = int(5) ')
print('B. x = 5')
print('C. Both the other answers are correct')

answer=input("Choose the answer" ).lower()
if answer=="c":
    print("correct")
    scrore +=1
else:
    print("incorrect")


print('''What is the correct file extension for Python files?''' )
print('A. .py ')
print('B. .pt')
print('C. .pyth')
print('C. .pyt ')

answer=input("Choose the answer" ).lower()
if answer=="a":
    print("correct")
    scrore +=1
else:
    print("incorrect")


print('''How do you create a variable with the floating number 2.8?''' )
print('A. Both the other answers are correct')
print('B. x = float(2.8)')
print('C. x = 2.8')

answer=input("Choose the answer" ).lower()
if answer=="a":
    print("correct")
    scrore +=1
else:
    print("incorrect")


print('''What is the correct syntax to output the type of a variable or object in Python?''' )
print('A. print(type(x))')
print('B. print(typeof(x))')
print('C. print(typeOf(x))')
print('D. print(typeof x)')

answer=input("Choose the answer" ).lower()
if answer=="a":
    print("correct")
    scrore +=1
else:
    print("incorrect")


print('''What is the correct way to create a function in Python?''' )
print('A. function myfunction(): ')
print('B. def myFunction():')
print('C. create myFunction():')

answer=input("Choose the answer" ).lower()
if answer=="b":
    print("correct")
    scrore +=1
else:
    print("incorrect")


print('''In Python, 'Hello', is the same as "Hello"?''' )
print('A. True')
print('B. False')

answer=input("Choose the answer" ).lower()
if answer=="a":
    print("correct")
    scrore +=1
else:
    print("incorrect")


print('''What is a correct syntax to return the first character in a string?''' )
print('A. x = "Hello".sub(0, 1)')
print('B. x = sub("Hello", 0, 1)')
print('C. x = "Hello"[0] ')

answer=input("Choose the answer" ).lower()
if answer=="a":
    print("correct")
    scrore +=1
else:
    print("incorrect")


print('''Which method can be used to remove any whitespace from both the beginning and the end of a string?''' )
print('A. trim()')
print('B. ptrim()')
print('C. len()')
print('D. strip()')

answer=input("Choose the answer" ).lower()
if answer=="d":
    print("correct")
    scrore +=1
else:
    print("incorrect")


print('''Which method can be used to return a string in upper case letters?''' )
print('A. uppercase()')
print('B. upper()')
print('C. upperCase()')
print('D. toUpperCase()')

answer=input("Choose the answer" ).lower()
if answer=="b":
    print("correct")
    scrore +=1
else:
    print("incorrect")


print('''Which method can be used to replace parts of a string?''' )
print('A. replaceString()')
print('B. repl()')
print('C. replace()')
print('D. switch()')

answer=input("Choose the answer" ).lower()
if answer=="c":
    print("correct")
    scrore +=1
else:
    print("incorrect")


print('''Which operator is used to multiply numbers?''' )
print('A. * ')
print('B. %')
print('C. x')
print('D. #')

answer=input("Choose the answer" ).lower()
if answer=="a":
    print("correct")
    scrore +=1
else:
    print("incorrect")


print('''Which operator can be used to compare two values?''' )
print('A. <>')
print('B. ><')
print('C. ==')
print('D. =')

answer=input("Choose the answer" ).lower()
if answer=="c":
    print("correct")
    scrore +=1
else:
    print("incorrect")


 
print("You got " + str(scrore) + " Questions correct")