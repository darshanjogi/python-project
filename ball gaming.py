while True:
    #Updating the screen everytime with the new changes
    screen.update()
    
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    # Checking if ball hits the left, right, and top walls of the screen  
    if ball.xcor() > 480:
        ball.setx(480)
        ball.dx *= -1 #Bouncing the ball 
 
    if ball.xcor() < -480:
        ball.setx(-480)
        ball.dx *= -1#Bouncing the ball 
    
    if ball.ycor() >280:
        ball.setx(280)
        ball.dy *= -1#Bouncing the ball 
    
    #Checking if the ball hits bottom and ending the game
    if ball.ycor() < -260:
        scoreBoard.clear()
        scoreBoard1 = turtle.Turtle()
        scoreBoard1.speed(0)
        scoreBoard1.penup()
        #Hiding the turtle to show text
        scoreBoard1.hideturtle()
        #Locating the score board on top of the screen
        scoreBoard1.goto(0, 0)
        scoreBoard1.color('black')
        #Showing the score
        scoreBoard1.write("Score : {} ".format(score),    align="center", font=("Courier", 30, "bold"))
       break
    
    #Checking if paddle hits the ball, updating score, increasing speed and bouncing the ball
    if (paddle.ycor() + 30 > ball.ycor() > paddle.ycor() - 30 and 
       paddle.xcor() + 50 > ball.xcor() > paddle.xcor() - 50 ):
        #Increasing score of left player and updating score board
        score += 1 
        scoreBoard.clear()
        scoreBoard.write("Score: {}".format(score), align="center", font=("Courier", 20, "bold"))
        
        #Increasing speed of the ball with the limit 7
        if(ball.dy>0 and ball.dy<5): #If dy is positive increasing dy
            ball.dy+=0.5
        elif(ball.dy<0 and ball.dy>-5): #else if dy is negative decreasing dy
            ball.dy-=0.5
            
        if(ball.dx>0 and ball.dx<5):#If dx is positive increasing dx
            ball.dx+=0.5
        elif(ball.dx<0 and ball.dx>-5): #else if dx is negative decreasing dx
            ball.dx-=0.5
        
        #Changing the direction of ball towards the right player
        ball.dy *=-1 
while (True):
    screen.update()
