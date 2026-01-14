"""
This program asks user to guess secret number.
"""

speed(0)
secret_number=15

#This draws an up arrow
def draw_up_arrow():
  color("green")
  pensize(5)
  left(90)
  forward(100)
  right(135)
  forward(30)
  backward(30)
  right(90)
  forward(30)

#Thiss draws down arrow
def draw_down_arrow():
  color("red")
  pensize(5)
  right(90)
  forward(80)
  right(135)
  forward(30)
  backward(30)
  right(90)
  forward(30)

#This draws a checkmark
def draw_checkmark():
  color("green")
  pensize(5)
  penup()
  backward(50)
  right(90)
  pendown()
  left(45)
  forward(50)
  left(90)
  forward(100)


#This asks user to guess secret number.
guess= int(input(Guess secret number (1-20):))

#If the user guesses lower than secret number than tracy draws a up arrow.
if guess < secret_number:
  draw_up_arrow()
#If the user guesses higher than the seret number than tracy draws a down arrow.
elif guess > secret_number:
  draw_down_arrow()
#If the user guesses the secret number correctly tracy draws a checkmark and prints Congrants You Did it!
else:
  print("Congrats! YOU DID IT!")
  draw_checkmark()
