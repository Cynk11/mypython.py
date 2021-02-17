# Simple "Ping Pong Game"!

# Turtle is module, it is a drawing board for Python.
import turtle
# Winsound, an object or file with a set of attributes or functions, specific to the task of generating or playing sound or a sound file.
import winsound

# These are variables on creating a Game Window using the Turtle module.
win = turtle.Screen()
# This is the Screen/Window title or the name of the Turtle module.
win.title('Ping Pong Game')
# This change the screen/window color.
win.bgcolor('black')
# This set up the window size.
win.setup(width=800, height=600)
win.tracer(0)

# This is the Score board.
score_a = 0
score_b = 0

# Paddle A
# This is Paddle A.
paddle_a = turtle.Turtle()
# This create/modify the speed.
paddle_a.speed(0)
# This creates the shape of paddle_a.
paddle_a.shape('square')
# This changes the color of paddle_a.
paddle_a.color('white')
# This create/modify the shape.
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
# This the coordinate of where the paddle is placed.
paddle_a.goto(-350, 0)

# Paddle B
# This is Paddle B.
paddle_b = turtle.Turtle()
# This create/modify the speed.
paddle_b.speed(0)
# This creates the shape of paddle_b.
paddle_b.shape('square')
# This create/modify the shape.
paddle_b.color('white')
# This changes the color of paddle_b
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
# This the coordinate of where the paddle is placed.
paddle_b.goto(350, 0)

# Ball
# This is the Ball.
ball = turtle.Turtle()
# This is the ball animation speed.
ball.speed(0)
# This is the shape of the ball.
ball.shape('square')
# This is the color of the ball.
ball.color('white')
ball.penup()
# This the coordinate of the ball.
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

# Pen
#This is for the score board.
turtle.pen = turtle.Turtle()
turtle.pen.speed(0)
turtle.pen.color('white')
turtle.pen.penup()
turtle.pen.hideturtle()
turtle.pen.goto(0, 260)
turtle.pen.write('Player A: 0 Player B: 0', align='center', font=('Courier', 24, 'normal'))

# Functions
#This is the board functions.
def paddle_a_up():
    y = paddle_a.ycor()
    y +=20
    paddle_a.sety(y)
    
def paddle_a_down():
    y = paddle_a.ycor()
    y -=20
    paddle_a.sety(y)
    
def paddle_b_up():
    y = paddle_b.ycor()
    y +=20
    paddle_b.sety(y)
    
def paddle_b_down():
    y = paddle_a.ycor()
    y -=20
    paddle_b.sety(y)
    
# Keyboard binding
# This is the keyboard control functions. This is use to control the movement of the Paddle.
# Animations could be found here.
win.listen()
win.onkeypress(paddle_a_up, 'w')
win.onkeypress(paddle_a_down, 's')

win.onkeypress(paddle_b_up, 'o')
win.onkeypress(paddle_b_down, 'l')             
# Main game loop
while True:
    win.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
        
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        turtle.pen.clear()
        turtle.pen.write('Player A: {} Player B: {}'.format(score_a,score_b), align='center', font=('Courier', 24, 'normal'))
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
        
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        turtle.pen.clear()
        turtle.pen.write('Player A: {} Player B: {}'.format(score_a,score_b), align='center', font=('Courier', 24, 'normal'))
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
        
    # Paddle and ball collision 
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() < -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        