import turtle

# Fikir : Belli bie sayıya kadar oyun devam eder ve sonra biter. Kafan esince yaparsın

def Up1():

 #   y = Playerone.ycor()
#    Playerone.sety(y + 20)

    if Playerone.direction != 'Up':
        Playerone.direction = 'Up'


def Down1():

    #y = Playerone.ycor()
    #Playerone.sety(y - 20)

    if Playerone.direction != 'Down':
        Playerone.direction = 'Down'


def Up2():

    #y = Playertwo.ycor()
    #Playertwo.sety(y + 20)

    if Playertwo.direction != 'Up':
        Playertwo.direction = 'Up'


def Down2():

    #y = Playertwo.ycor()
    #Playertwo.sety(y - 20)

    if Playertwo.direction != 'Down':
        Playertwo.direction = 'Down'



def Move():

    if Playerone.direction == 'Up':
        y = Playerone.ycor()
        Playerone.sety(y + 0.17)
        #Ball.goto(Ball.xcor() + Ball.dx, Ball.ycor() + Ball.dy)

    if Playerone.direction == 'Down':
        y = Playerone.ycor()
        Playerone.sety(y - 0.17)
        #Ball.goto(Ball.xcor() + Ball.dx, Ball.ycor() + Ball.dy)

    if Playertwo.direction == 'Up':
        y = Playertwo.ycor()
        Playertwo.sety(y + 0.17)
        #Ball.goto(Ball.xcor() + Ball.dx, Ball.ycor() + Ball.dy)

    if Playertwo.direction == 'Down':
        y = Playertwo.ycor()
        Playertwo.sety(y - 0.17)
        #Ball.goto(Ball.xcor() + Ball.dx, Ball.ycor() + Ball.dy)

print("Mümkünse en fazla 5 karakter kullanınız.")
a1 = input("Lütfen birinci oyuncunun ismini giriniz : ")
a2 = input("Lütfen ikinci oyuncunun ismini giriniz : ")

Screen = turtle.Screen()
Screen.screensize(700, 600)
#Screen.setup(width=600, height=600)
Screen.title('Pinpon Game')
Screen.bgcolor('black')
Screen.tracer(0)


Puan1 = 0

Sounc1 = turtle.Turtle()
Sounc1.shape('square')
Sounc1.color('white')
Sounc1.penup()
Sounc1.speed(0)
Sounc1.goto(196, 250)
Sounc1.hideturtle()
Sounc1.write(a1 + ' Adlı Oyuncu: {}'.format(Puan1), align='center', font=('courier', 24, 'bold'))


Puan2 = 0

Sounc2 = turtle.Turtle()
Sounc2.shape('square')
Sounc2.color('white')
Sounc2.penup()
Sounc2.speed(0)
Sounc2.goto(-199, 250)
Sounc2.hideturtle()
Sounc2.write(a2 + ' Adlı Oyuncu: {}'.format(Puan2), align='center', font=('courier', 24, 'bold'))
#                                                    ortala        yazı'nın tipi, büyüklüğü, kalınlığı
puan_a = 0
puan_b = 0

#Yazi = turtle.Turtle()
#Yazi.shape('square')
#Yazi.speed(0)
#Yazi.color('white')
#Yazi.penup()
#Yazi.goto(0, 260)
#Yazi.write("Oyuncu A:{}   Oyuncu B:{}".format(puan_a, puan_b), align='center', font=('Courier', 24, 'bold'))
#Yazi.hideturtle()
# Daha mantıklı ve daha kısa

Playerone = turtle.Turtle()
Playerone.shape('square')
Playerone.shapesize(5, 1)
Playerone.color('white')
Playerone.speed(0)
Playerone.penup()
Playerone.goto(350, 0)
Playerone.direction = 'stop'



Playertwo = turtle.Turtle()
Playertwo.shape('square')
Playertwo.shapesize(5, 1)
Playertwo.color('white')
Playertwo.speed(0)
Playertwo.penup()
Playertwo.goto(-350, 0)
Playertwo.direction = 'stop'



Ball = turtle.Turtle()
Ball.shape('circle')
Ball.color('white')
Ball.penup()
Ball.goto(0, 0)
Ball.speed(0)
Ball.dx = 0.1
Ball.dy = 0.1


Screen.listen()
Screen.onkey(Up1, 'Up')
Screen.onkey(Down1, 'Down')
Screen.onkeypress(Up2, 'w')
Screen.onkeypress(Down2, 's')


while True:

    Screen.update()

    Ball.goto(Ball.xcor() + Ball.dx, Ball.ycor() + Ball.dy)



    if Ball.ycor() > 290:
        Ball.dy = Ball.dy * -1

    if Ball.ycor() < -290:
        Ball.dy = Ball.dy * -1



    if 350 > Ball.xcor() > 340 and Playerone.ycor() + 39 > Ball.ycor() > Playerone.ycor() - 39:
        Ball.setx(340)
        Ball.dx = Ball.dx * -1

    if -350 < Ball.xcor() < -340 and Playertwo.ycor() + 39 > Ball.ycor() > Playertwo.ycor() - 39:
        Ball.setx(-340)
        Ball.dx = Ball.dx * -1



    if Ball.xcor() > 380:

        Puan1 = Puan1 + 1
        Sounc1.clear()
        Sounc1.write(a1 + ' Adlı Oyuncu: {}'.format(Puan1), align='center', font=('courier', 24, 'bold'))

        Ball.goto(0, 0)
        Ball.dx = Ball.dx * -1


    if Ball.xcor() < -380:

        Puan2 = Puan2 + 1
        Sounc2.clear()
        Sounc2.write(a2 + ' Adlı Oyuncu: {}'.format(Puan2), align='center', font=('courier', 24, 'bold'))

        Ball.goto(0, 0)
        Ball.dx = Ball.dx * -1



    if Playerone.ycor() > 270:
        Down1()

    if Playerone.ycor() < -270:
        Up1()

    if Playertwo.ycor() > 270:
        Down2()

    if Playertwo.ycor() < -270:
        Up2()

    Move()