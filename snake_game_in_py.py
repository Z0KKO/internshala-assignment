import turtle
import time
import random

delay =0.1

# Score
score =0
high_score =0

# set up the screen
wn= turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("green")
wn.setup(width = 600 , height = 600)
wn.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("blue")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 HighScore:0", align="center",font=("Courier",24,"normal"))


# Functon
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"



def move():
    if head.direction == "up":
        y= head.ycor()
        head.sety(y+20)
    
    if head.direction == "down":
        y= head.ycor()
        head.sety(y-20)

    if head.direction == "left":
        x= head.xcor()
        head.setx(x-20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keybpard binding
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")

# Main game loop
while True:
    wn.update()
    
    # check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # hide the segment
        for segment in segments:
            segment.goto(1000,1000)
        
        # clear the segment
        segments.clear()

        # reset the score
        score=0

        # reset the delay
        delay =0.1

        pen.clear()
        pen.write("Score: {} HighScore: {}".format(score,high_score), align="center",font=("Courier",24,"normal"))


    # check for collision
    if head.distance(food)<20:
        x= random.randint(-290,290)
        y= random.randint(-290,290)
        food.goto(x,y)

        # add segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("gray")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001


        # increase the score
        score +=1

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {} HighScore: {}".format(score,high_score), align="center",font=("Courier",24,"normal"))


# move the end segn=ments first
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

# move segment to head
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)

    move()

    # check for head body collision
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

        # hide the segment
            for segment in segments:
                segment.goto(1000,1000)
        
        # clear the segment
            segments.clear()

             # reset the score
            score=0

            # reset the delay
            delay =0.1

            pen.clear()
            pen.write("Score: {} HighScore: {}".format(score,high_score), align="center",font=("Courier",24,"normal"))


    time.sleep(delay)

wn.mainloop()