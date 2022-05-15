


import sys
import time
n1 = int(input("f: "))
method = str(input("method:  "))
n2 = int(input("s: "))
yn = str(input("Y/N:   "))
n3 = 0
if yn == "Y":
  n3 = float(input("t:   "))
if n1 == 0:
  if n2 == 0:
    if method == "/":
      sys.exit("why")

if method == "/":
  if n1 == 0:
    print("why")
    time.sleep(1)
    sys.exit("why")
  if n2 == 0:
    print("why")
    time.sleep(1)
    sys.exit("why")

if type(n1) == int:
    print("")
else:
  time.sleep(1)
  sys.exit("why")

if method.isdigit():
  time.sleep(1)
  sys.exit("why")
else:
    print("")
if yn == "N":
  if method == "x":
    print(n1 * n2)
  if method == "/":
    print(n1 / n2)
  if method == "+":
    print(n1 + n2)
  if method == "-":
    print(n1 - n2)


if n3 != 0:
  
  if method == "x":
    print(n1 * n2 * n3)
  if method == "*":
    print(n1 * n2 * n3)
  if method == "+":
    print(n1 + n2 + n3)
  if method == "-":
    print(n1 - n2 - n3)






