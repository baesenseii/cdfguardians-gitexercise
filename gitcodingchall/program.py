#!/usr/bin/python3

def problem1():
  print("Type your code here")

def problem2():
    total = 1
    randomlist = []
    userinput = input("Enter your number of items in each group (each group seperated by commas): ")

    randomlist= userinput.split(",")

    for x in randomlist:
        total = total*x
    return total

def problem3():
  print("Type your code here")

  original_text = input("Key in your input: ")
  shifted_text= []
  shift_value = int(input("key in key shift: "))

  for i in range(len(original_text)):
      shifted_text.append(chr(ord(original_text[i]) + shift_value))

  print ("".join(shifted_text))
def problem4():
  #print("Type your stuff here")
  import re
  p = input("Input your password: ")
  x = True

  while x:
      if not(len(p)>12):
          break
      elif not re.search("[a-z]", p):
            break
      elif not re.search("[A-Z]", p):
            break
      elif not re.search("[0-9]", p):
            break
      elif not re.search("[$#@!%^&*?]"):
            break
      else:
        print("Function result: PASS")
        x = False
        break

        if x:
            print("Function result: FAIL")



def problem5():
  print("Type your code here")

def problem6():
    usr = input("Please submit your user input here: ")
    encode = b64encode(hash(usr))
  print("Your hashed + base64 encoded value is: " + encode)

def main():
    banner = """
 ____  ____  _     _     ____  ____    ____  ____  ____  _  _      _____
/   _\/  _ \/ \   / \   /  _ \/  __\  /   _\/  _ \/  _ \/ \/ \  /|/  __/
|  /  | / \|| |   | |   | / \|| | //  |  /  | / \|| | \|| || |\ ||| |  _
|  \__| \_/|| |_/\| |_/\| |-||| |_\\  |  \__| \_/|| |_/|| || | \||| |_//
\____/\____/\____/\____/\_/ \|\____/  \____/\____/\____/\_/\_/  \|\____\
  """
    print(banner)
    print ("""
  Main Menu Options:
    1. Problem 1
    2. Problem 2
    3. Problem 3
    4. Problem 4
    5. Problem 5
    6. Problem 6
 """)
    choice = input("Enter your choice here: ")

    if int(choice) == 1:
        problem1()
    elif int(choice) == 2:
        problem2()
    elif int(choice) == 3:
        problem3()
    elif int(choice) == 4:
        problem4()
    elif int(choice) == 5:
        problem5()
    elif int(choice) == 6:
        problem6()
    else:
        print("Invalid choice. Exiting application")


main()
