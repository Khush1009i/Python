# Creating emoji's using VS Code:
import turtle

emo = turtle.Turtle()

# to make center of circle (Face )

emo.up()
emo.goto(0, -100)
emo.down()

#fill the yellow clr 
emo.begin_fill()
emo.pendown() # use to fill pixel basically it traced points like circle
emo.fillcolor('yellow')
emo.circle(100)
emo.end_fill()

#semicircle emoji:
emo.up()
emo.goto(-67, -40)
emo.setheading(-60)
emo.width(5)
emo.down()
emo.circle(80, 120)
emo.fillcolor("black")

#to make eyes:
for i in range (-35, 105, 70):
    emo.up()
    emo.goto(i, 35)
    emo.setheading(0)
    emo.down()
    emo.begin_fill()
    emo.circle(10)
    emo.end_fill()
emo.penup() # take pen as up so after it goes to end point it will no affect our emoji
emo.goto(0, -150)# - for downside & + for upside

# not use turtle becoz it will destroy screen as soon as it will complete drwang part 
# to remain screen on we will use loop

turtle.mainloop()
