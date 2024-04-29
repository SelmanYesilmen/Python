import turtle
import random
import time

Kuyruklar = []

TusSayisi = 0

def Mouse(x, y):
    global deger, TusSayisi

    if TusSayisi == 0:

        Sonuc.clear()
        Snake.color('white')

        Aim.setposition(random.randint(-270, 270), random.randint(-270, 270))
        Puan.clear()
        deger = deger + 1
        Puan.write('Puan: {}'.format(deger), align='center', font=('courier', 24, 'normal'))

        # Burada yapmak istediğim sadece fareylede işlem yapılabileceğini göstermek istememdir.

def Move():

    if Snake.direction == 'up':
        y = Snake.ycor()
        Snake.sety(y + 20)

    if Snake.direction == 'down':
        y = Snake.ycor()
        Snake.sety(y - 20)

    if Snake.direction == 'right':
        x = Snake.xcor()
        Snake.setx(x + 20)

    if Snake.direction == 'left':
        x = Snake.xcor()
        Snake.setx(x - 20)



def Right():
    global Sonuc, Snake, TusSayisi, deger

    if TusSayisi == 0:
        Puan.clear()
        deger = 0
        Puan.write('Puan: {}'.format(deger), align='center', font=('courier', 24, 'normal'))


    TusSayisi = TusSayisi + 1

    #if Snake.direction == 'up':
     #   Snake.right(90)

    #if  Snake.direction == 'down':
     #   Snake.left(90)

    if Snake.direction != 'left':
        Snake.direction = 'right'

    Sonuc.clear()
    Snake.color('white')

def Left():
    global Sonuc, Snake, TusSayisi, deger

    if TusSayisi == 0:
        Puan.clear()
        deger = 0
        Puan.write('Puan: {}'.format(deger), align='center', font=('courier', 24, 'normal'))

    TusSayisi = TusSayisi + 1

    #if Snake.direction == 'up':
     #   Snake.left(90)

    #if Snake.direction == 'down':
     #   Snake.right(90)
    if Snake.direction != 'right':
        Snake.direction = 'left'

    Sonuc.clear()
    Snake.color('white')



def Up():
    global Sonuc, Snake, TusSayisi, deger

    if TusSayisi == 0:
        Puan.clear()
        deger = 0
        Puan.write('Puan: {}'.format(deger), align='center', font=('courier', 24, 'normal'))

    TusSayisi = TusSayisi + 1

    #if Snake.direction == 'right':
     #   Snake.left(90)

    #if Snake.direction == 'left':
     #   Snake.right(90)
    if Snake.direction != 'down':
        Snake.direction = 'up'

    Sonuc.clear()
    Snake.color('white')

def Down():
    global Sonuc, Snake, TusSayisi, deger

    if TusSayisi == 0:
        Puan.clear()
        deger = 0
        Puan.write('Puan: {}'.format(deger), align='center', font=('courier', 24, 'normal'))

    TusSayisi = TusSayisi + 1

    #if Snake.direction == 'right':
     #   Snake.right(90)

    #if Snake.direction == 'left':
     #   Snake.left(90)

    if Snake.direction != 'up':
        Snake.direction = 'down'

    Sonuc.clear()
    Snake.color('white')


Screen = turtle.Screen()
#Screen.screensize(600, 600)
Screen.setup(width=600, height=600)
Screen.title('SnakeGame')
Screen.bgcolor('black')
#Screen.tracer(10)

Snake = turtle.Turtle()
Snake.color('white')
Snake.shape('square')
Snake.shapesize(1.2)
Snake.penup()
Snake.goto(0, 0)
Snake.direction = 'stop'

Aim = turtle.Turtle()
Aim.color('blue')
Aim.speed(0)
Aim.penup()
Aim.shape('circle')
Aim.shapesize(1.2)
Aim.setposition(random.randint(-270, 270), random.randint(-270, 270))

Screen.listen()
Screen.onkey(Right, 'Right')
Screen.onkey(Left, 'Left')
Screen.onkey(Up, 'Up')
Screen.onkey(Down, 'Down')

Sonuc = turtle.Turtle()
Sonuc.penup()
Sonuc.speed(0)
Sonuc.color('red')
Sonuc.shape('square')
Sonuc.hideturtle()

deger = 0

Puan = turtle.Turtle()
Puan.shape('square')
Puan.hideturtle()
Puan.color('white')
Puan.penup()
Puan.goto(0, 269)
Puan.write('Puan: {}'.format(deger), align='center', font=('courier', 24, 'normal'))


while True:

    Aim.onclick(Mouse)

    Screen.update()  # bunu yazmazsam kod çalışmıyordu bi nevi direction sağ olsun

    #Snake.forward(1)

    if Snake.ycor() < -300 or Snake.ycor() > 300 or Snake.xcor() < -300 or Snake.xcor() > 300:
        Snake.clear()
        Snake.goto(0, 0)
        Snake.color('red')
        #Aim.goto(1000, 1000)

        Snake.direction = 'stop'
        Sonuc.goto(0, -45)
        Sonuc.write('THE END', align='center', font=('courier', 60, 'normal'))
        TusSayisi = 0

        for Kuyruk in Kuyruklar:
            #Kuyruk.clear() # Denedim ama işe yaramadı
            Kuyruk.goto(1000, 1000)

        Kuyruklar = []
        deger = 0
        #Puan.clear()
        #Puan.write('Puan: {}'.format(deger), align='center', font=('courier', 24, 'normal'))

    for Kuyruk in Kuyruklar:
        if Snake.xcor() == Kuyruk.xcor() and Snake.ycor() == Kuyruk.ycor():
            Snake.clear()
            Snake.goto(0, 0)
            Snake.color('red')
            #Aim.goto(1000, 1000)

            Snake.direction = 'stop'
            Sonuc.goto(0, -45)
            Sonuc.write('THE END', align='center', font=('courier', 60, 'normal'))
            TusSayisi = 0

            for Kuyruk in Kuyruklar:
                Kuyruk.goto(1000, 1000)

            Kuyruklar = []
            deger = 0
            # Puan.clear()
            # Puan.write('Puan: {}'.format(deger), align='center', font=('courier', 24, 'normal'))


    if Snake.distance(Aim) < 20:
        Aim.setposition(random.randint(-270, 270), random.randint(-270, 270))
        Puan.clear()
        deger = deger + 1
        Puan.write('Puan: {}'.format(deger), align='center', font=('courier', 24, 'normal'))

        YeniKuyruk = turtle.Turtle()
        YeniKuyruk.speed(0)
        YeniKuyruk.shape('square')
        YeniKuyruk.color('white')
        YeniKuyruk.penup()
        Kuyruklar.append(YeniKuyruk)

        if len(Kuyruklar) > 1:

            y = Kuyruklar[-1].ycor()
            x = Kuyruklar[-1].xcor()

            YeniKuyruk.goto(x, y)

    for i in range(len(Kuyruklar) - 1, 0, -1):
        y = Kuyruklar[i - 1].ycor()
        x = Kuyruklar[i - 1].xcor()
        Kuyruklar[i].goto(x, y)

    if len(Kuyruklar) > 0:
        x = Snake.xcor()
        y = Snake.ycor()
        Kuyruklar[0].goto(x, y)


    time.sleep(0.1)
    Move()