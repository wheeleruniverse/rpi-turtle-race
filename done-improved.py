
import random
import turtle


colors=[
  'blue',
  'green',
  'khaki',
  'maroon',
  'orange',
  'peru',
  'pink',
  'purple',
  'red',
  'salmon',
  'yellow'
]
players=[]
players_start=220
players_step=40


def create_turtle(color, start):
  instance = turtle.Turtle()
  instance.color(color)
  instance.shape('turtle')
  instance.penup()
  instance.goto(-230, start)
  instance.pendown()
  
  if random.randint(0, 1) == 1:
    instance.left(360)
  else:
    instance.right(360)

  players.append(instance)


turtle.speed(10)
turtle.penup()
turtle.goto(-200, 250)

for step in range(20):
  turtle.write(step + 1, align='center')
  turtle.right(90)
  turtle.forward(10)
  turtle.pendown()

  for dash in range(30):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(5)
    turtle.pendown()

  turtle.penup()
  turtle.forward(20)

  turtle.pendown()
  turtle.write(step + 1, align='center')
  turtle.penup()

  turtle.backward(480)
  turtle.left(90)
  turtle.forward(20)

random.shuffle(colors)

for c in colors:
  create_turtle(c, players_start - len(players) * players_step)

for turn in range(50):
  for p in players:
    p.forward(random.randint(1, 15))
 
max=0
winner=None
for p in players:
  cur=p.pos()[0]
  if cur > max:
    max=cur
    winner=p

winner.right(1710)

input('press enter to quit')

