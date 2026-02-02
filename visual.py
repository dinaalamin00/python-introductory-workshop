import turtle

# =========================================================
# 👉 STUDENT INSTRUCTIONS 👈
# You only need to change the VALUES passed to the 3 functions below.
# Do NOT change anything else in the code.
#
# 1) set_ball_speed(speed)
#    - choose a suitable value to control how fast the ball moves
#
# 2) set_paddle_speed(speed)
#    - choose a suitable value to control how fast the paddle moves 
#
# 3) set_colors(background, paddles, ball)
#    - use color names like: "black", "white", "red", "blue", "green"
#    "lightblue" "darkgreen" "navy" "gold" "violet" "turquoise" "salmon" "coral" "skyblue" "lime"
# make sure to inform the mentor of your chosen changes and what values you used!
# =========================================================

def set_ball_speed(speed):
    global ball_dx, ball_dy
    ball_dx = speed
    ball_dy = speed

def set_paddle_speed(speed):
    global paddle_speed
    paddle_speed = speed

def set_colors(background_color, paddle_color, ball_color):
    global background_color_global, paddle_color_global, ball_color_global
    background_color_global = background_color
    paddle_color_global = paddle_color
    ball_color_global = ball_color


# ================= CHANGE VALUES HERE ====================
set_ball_speed(0.2)
set_paddle_speed(20)
set_colors("black", "blue", "white")
# =========================================================


window = turtle.Screen()
window.title("Pong Game")
window.bgcolor(background_color_global)
window.setup(width=800, height=600)
window.tracer(0)

player_a_score = 0
player_b_score = 0

left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color(paddle_color_global)
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)

right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color(paddle_color_global)
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color(ball_color_global)
ball.penup()
ball.goto(0, 0)

pen = turtle.Turtle()
pen.speed(0)
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0    Player B: 0", align="center", font=('Arial', 24, 'normal'))

def left_paddle_up():
    y = left_paddle.ycor()
    y += paddle_speed
    if y > 250:
        y = 250
    left_paddle.sety(y)

def left_paddle_down():
    y = left_paddle.ycor()
    y -= paddle_speed
    if y < -250:
        y = -250
    left_paddle.sety(y)

def right_paddle_up():
    y = right_paddle.ycor()
    y += paddle_speed
    if y > 250:
        y = 250
    right_paddle.sety(y)

def right_paddle_down():
    y = right_paddle.ycor()
    y -= paddle_speed
    if y < -250:
        y = -250
    right_paddle.sety(y)

window.listen()
window.onkeypress(left_paddle_up, 'w')
window.onkeypress(left_paddle_down, 's')
window.onkeypress(right_paddle_up, 'Up')
window.onkeypress(right_paddle_down, 'Down')

def increase_ball_speed(factor):
    global ball_dx, ball_dy
    ball_dx *= factor
    ball_dy *= factor

while True:
    window.update()

    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball_dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball_dx *= -1
        player_a_score += 1
        pen.clear()
        pen.write(f"Player A: {player_a_score}    Player B: {player_b_score}", align="center", font=('Arial', 24, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball_dx *= -1
        player_b_score += 1
        pen.clear()
        pen.write(f"Player A: {player_a_score}    Player B: {player_b_score}", align="center", font=('Arial', 24, 'normal'))

    if (340 < ball.xcor() < 350) and (right_paddle.ycor() - 50 < ball.ycor() < right_paddle.ycor() + 50):
        ball.setx(340)
        ball_dx *= -1
        increase_ball_speed(1.05)

    if (-350 < ball.xcor() < -340) and (left_paddle.ycor() - 50 < ball.ycor() < left_paddle.ycor() + 50):
        ball.setx(-340)
        ball_dx *= -1
        increase_ball_speed(1.05)
