import random
import time
import turtle

window = turtle.Screen()
turtle.setup(800, 700)
window.bgcolor('light steel blue')
window.addshape('stone.gif')
window.addshape('paper.gif')
window.addshape('scissors.gif')

gure = turtle.Turtle()
gure.up()
gure.setposition(-230, 0)
gure.shape('stone.gif')
leter = turtle.Turtle()
leter.up()
leter.shape('paper.gif')
gershere = turtle.Turtle()
gershere.up()
gershere.setposition(230, 0)
gershere.shape('scissors.gif')
text2 = turtle.Turtle()
text2.up()
text2.ht()
text2.setposition(0, 250)
text = turtle.Turtle()
text.up()
text.ht()
text.setposition(0, -250)

luaj = turtle.Turtle()
luaj.up()
luaj.ht()
luaj.setposition(0, 300)

quit_t = turtle.Turtle()
quit_t.up()
quit_t.ht()
quit_t.setposition(0, -300)

style = ('Courier', 20, 'normal')
string = ""
string2 = ""
text.write(string, font=style, align='center')
loja = ["gure", "leter", "gershere"]

player = ""
computer = ""
player_turn = True

def clicked(x, y):
    global loja
    global player
    global player_turn
    global computer
    global text
    global text2
    global style
    global gure
    global leter
    global gershere
    global luaj
    global string2
    global quit_t
    copy1 = turtle.Turtle()
    copy1.ht()
    copy1.up()
    copy2 = turtle.Turtle()
    copy2.ht()
    copy2.up()

    def kompjuteri(computer, loja, copy2, string, text, string2, text2, luaj, quit_t):
        time.sleep(2)
        computer = random.choice(loja)
        if (computer == "gure"):
            copy2 = gure.clone()
            copy2.setposition(230, 0)
        elif (computer == "gershere"):
            copy2 = gershere.clone()
            copy2.setposition(230, 0)
        elif (computer == "leter"):
            copy2 = leter.clone()
            copy2.setposition(230, 0)
        copy2.st()
        text.clear()
        string = ("Kompjuteri zgjodhi " + computer)
        text.write(string, font=style, align='center')
        time.sleep(0.5)
        if computer == player:
            string2 = "Barazim"
            text2.clear()
            text2.write(string2, font=style, align='center')
        if ((computer == "gershere" and player == "gure") or
            (computer == "leter" and player == "gershere") or
            (computer == "gure" and player == "leter")):
            string2 = "Fitove"
            text2.clear()
            text2.write(string2, font=style, align='center')
        elif ((computer == "gershere" and player == "leter") or
            (computer == "gure" and player == "gershere") or
            (computer == "leter" and player == "gure")):
            string2 = "Humbe"
            text2.clear()
            text2.write(string2, font=style, align='center')
        time.sleep(1)
        luaj.write('Luaj perseri!', font=style, align='center')
        quit_t.write('Perfundo!', font=style, align='center')
        copy1.hideturtle()
        copy2.hideturtle()



    if player_turn == True:
        gershere.st()
        leter.st()
        gure.st()
        if (x > -100 and x < 104 and y > -168 and y < 175):
            player = "leter"
            text.clear()
            string = ("Ju zgjodhet " + player)
            text.write(string, font=style, align='center')
            copy1 = leter.clone()
            copy1.setposition(-230, 0)
            gershere.ht()
            leter.ht()
            gure.ht()
            copy1.showturtle()
            kompjuteri(computer, loja, copy2, string, text, string2, text2, luaj, quit_t)
            player_turn = False
        elif (x > 141 and x < 319 and y > -168 and y < 175):
            player = "gershere"
            text.clear()
            string = ("Ju zgjodhet " + player)
            text.write(string, font=style, align='center')
            copy1 = gershere.clone()
            copy1.setposition(-230, 0)
            gershere.ht()
            leter.ht()
            gure.ht()
            copy1.showturtle()
            kompjuteri(computer, loja, copy2, string, text, string2, text2, luaj, quit_t)
            player_turn = False
        elif (x > -332 and x < -127 and y > -168 and y < 143):
            player = "gure"
            text.clear()
            string = ("Ju zgjodhet " + player)
            text.write(string, font=style, align='center')
            copy1 = gure.clone()
            copy1.setposition(-230, 0)
            gershere.ht()
            leter.ht()
            gure.ht()
            copy1.showturtle()
            kompjuteri(computer, loja, copy2, string, text, string2, text2, luaj, quit_t)
            player_turn = False
        else:
            player = ""
    else:
        if (x > -60 and x < 60 and y > -300 and y < -270):
            window.bye()
        if (x > -104 and x < 101 and y < 334 and y > 300):
            player_turn = True
            player = ""
            computer = ""
            text2.clear()
            luaj.clear()
            quit_t.clear()
            text.clear()
            gure.st()
            gershere.st()
            leter.st()

turtle.onscreenclick(clicked)
window.mainloop()
