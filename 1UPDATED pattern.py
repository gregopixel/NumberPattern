import random
a = 1
correct = 0
wrong = 0
def correcto():
  print("Correct! Correct answers:", correct + 1, "Wrong answers:", wrong)


def incorrect():
  print("No, the correct answer was", r, "Correct answers:", correct, "Wrong answers:", wrong + 1)
while a != 0:
  for x in range(1):
    y = random.randint(1, 101)
    z = random.randint(1, 10)
    r = random.randint(1, 10)
    f = random.randint(1, 10)
    #f = 1
  if f == 1:
    print(r, y - z, r, y + z, r, y + 3*z)
    a = int(input("What number comes next? "))
    if a == r:
      correcto()
      correct = correct + 1
    elif a == 0:
      print("Final scores:", correct, "correct and", wrong, "wrong")
      break
    else:
      incorrect()
      wrong = wrong + 1
  if f == 2:
    print(r, y - z, y, y + z, r, y + 3 * z)
    a = int(input("What number comes next? "))
    if a == y + 4*z:
      correcto()
      correct = correct + 1
    elif a == 0:
      print("Final scores:", correct, "correct and", wrong, "wrong")
      break
    else:
      print("No, the correct answer was", y + 4*z, "Correct answers:", correct, "Wrong answers:", wrong + 1)
      wrong = wrong + 1
  if f == 3:
    print(y + 7*z, y + 6*z, r, y + 4*z, y + 3*z, r, y + z)
    a = int(input("What number comes next? "))
    if a == y:
      print("Correct! Correct answers:", correct + 1, "Wrong answers:", wrong)
      correct = correct + 1
    elif a == 0:
      print("Final scores:", correct, "correct and", wrong, "wrong")
      break
    else:
      print("No, the correct answer was", y, "Correct answers:", correct, "Wrong answers:", wrong + 1)
      wrong = wrong + 1
  if f == 4:
    print(y - 3*z, y - 2*z, y - z, y, y + z, y + 2*z)
    a = int(input("What number comes next? "))
    if a == y + 3*z:
      print("Correct! Correct answers:", correct + 1, "Wrong answers:", wrong)
      correct = correct + 1
    elif a == 0:
      print("Final scores:", correct, "correct and", wrong, "wrong")
      break
    else:
      print("No, the correct answer was", y + 3*z, "Correct answers:", correct, "Wrong answers:", wrong + 1)
      wrong = wrong + 1
  if f == 5:
    for x in range(1):
      n = random.randint(1, 101)
      m = random.randint(1, 10)
      o = n + m
      p = m + o
      q = o + p
      r = p + q
      s = q + r
    print(n, m, o, p, q, r,)
    a = int(input("What number comes next? "))
    if a == s:
      print("Correct! Correct answers:", correct + 1, "Wrong answers:", wrong)
      correct = correct + 1
    elif a == 0:
      print("Final scores:", correct, "correct and", wrong, "wrong")
      break
    else:
      print("No, the correct answer was", s, "Correct answers:", correct, "Wrong answers:", wrong + 1)
      wrong = wrong + 1
  if f == 6:
    print(y, y + 1, y - 1, y + 2, y - 2)
    a = int(input("What number comes next? "))
    if a == y + 3:
      print("Correct! Correct answers:", correct + 1, "Wrong answers:", wrong)
      correct = correct + 1
    elif a == 0:
      print("Final scores:", correct, "correct and", wrong, "wrong")
      break
    else:
      print("No, the correct answer was", y + 3 * z, "Correct answers:", correct, "Wrong answers:", wrong + 1)
      wrong = wrong + 1
  if f == 7:
    print(y, z, y + z, 2*z, y + 3*z, 3*z,)
    a = int(input("What number comes next? "))
    if a == y + 6*z:
      print("Correct! Correct answers:", correct + 1, "Wrong answers:", wrong)
      correct = correct + 1
    elif a == 0:
      print("Final scores:", correct, "correct and", wrong, "wrong")
      break
    else:
      print("No, the correct answer was", y + 6*z, "Correct answers:", correct, "Wrong answers:", wrong + 1)
      wrong = wrong + 1
  if f == 8:
    print(y, z, y + 1, z - 1, y + 2, z - 2,)
    a = int(input("What number comes next? "))
    if a == y + 3:
      print("Correct! Correct answers:", correct + 1, "Wrong answers:", wrong)
      correct = correct + 1
    elif a == 0:
      print("Final scores:", correct, "correct and", wrong, "wrong")
      break
    else:
      print("No, the correct answer was", y + 3, "Correct answers:", correct, "Wrong answers:", wrong + 1)
      wrong = wrong + 1
  if f == 9:
    print(r, z, r + z, z - r, r + 2*z, z - 2*r)
    a = int(input("What number comes next? "))
    if a == r + 3*z:
      print("Correct! Correct answers:", correct + 1, "Wrong answers:", wrong)
      correct = correct + 1
    elif a == 0:
      print("Final scores:", correct, "correct and", wrong, "wrong")
      break
    else:
      print("No, the correct answer was", r + 3*z, "Correct answers:", correct, "Wrong answers:", wrong + 1)
      wrong = wrong + 1
  if f == 10:
    print(y, z, y + 10, z + 10, y + 20, z + 20,)
    a = int(input("What number comes next? "))
    if a == y + 30:
      print("Correct! Correct answers:", correct + 1, "Wrong answers:", wrong)
      correct = correct + 1
    elif a == 0:
      print("Final scores:", correct, "correct and", wrong, "wrong")
      break
    else:
      print("No, the correct answer was", y + 30, "Correct answers:", correct, "Wrong answers:", wrong + 1)
      wrong = wrong + 1








