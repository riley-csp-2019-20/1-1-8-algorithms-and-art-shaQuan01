import turtle as trtl

drawer = trtl.Turtle()
drawer. speed(50)
drawer.circle(100,360,6)
drawer.penup()
drawer.color("black")

spiral_space = 0

while (spiral_space < 4): 
  drawer.goto(0,100)
  drawer.right(20)
  drawer.forward(12+(spiral_space*1))
  drawer.pendown()
  drawer.circle(100,180,60)
  drawer.penup()
  spiral_space = spiral_space - 1
  if (spiral_space % 6 == 0):
    drawer.color("black")
  if (spiral_space % 5 == 0):
    drawer.color("black")




wn = trtl.Screen()
wn.mainloop()