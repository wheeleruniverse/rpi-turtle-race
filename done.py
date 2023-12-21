
import turtle
from random import randint

turtle.speed(10)
turtle.penup()
turtle.goto(-140, 140)

for step in range(15):
  turtle.write(step, align='center')
  turtle.right(90)
  turtle.forward(10)
  turtle.pendown()

  for dash in range(15):
    turtle.forward(7)
    turtle.penup()
    turtle.forward(3)
    turtle.pendown()

  turtle.penup()
  turtle.backward(160)
  turtle.left(90)
  turtle.forward(20)

red = turtle.Turtle()
red.color('red')
red.shape('turtle')
red.penup()
red.goto(-160, 100)
red.pendown()
red.right(360)

blue = turtle.Turtle()
blue.color('blue')
blue.shape('turtle')
blue.penup()
blue.goto(-160, 80)
blue.pendown()
blue.left(360)

green = turtle.Turtle()
green.color('green')
green.shape('turtle')
green.penup()
green.goto(-160, 60)
green.pendown()
green.right(360)

yellow = turtle.Turtle()
yellow.color('yellow')
yellow.shape('turtle')
yellow.penup()
yellow.goto(-160, 40)
yellow.pendown()
yellow.left(360)

for turn in range(100):
  red.forward(randint(1, 5))
  blue.forward(randint(1, 5))
  green.forward(randint(1, 5))
  yellow.forward(randint(1, 5))


input('press enter to quit')

