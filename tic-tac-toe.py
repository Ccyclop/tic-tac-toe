import turtle
import time

xpoint = 0
opoint = 0

# Screen Setup
wn = turtle.Screen()
wn.setup(900,900)
wn.bgcolor('black')
wn.title("Tic Tac Toe")
wn.tracer(0,0)
turtle.hideturtle()
dot = turtle.Turtle()

# Draw Grid
dot.pencolor('white')
dot.pensize(5)
dot.up()
dot.setpos(-160,450)
dot.down()
dot.goto(-160,-450)
dot.up()
dot.setpos(160,450)
dot.down()
dot.goto(160,-450)
dot.up()
dot.setpos(-450,160)
dot.down()
dot.goto(450,160)
dot.up()
dot.setpos(-450,-160)
dot.down()
dot.goto(450,-160)
dot.up()

# Set Grid Coordinates
c = {
    #    t-left       t-right     b-left      b-right   drawn?  X or O
    1: [(-450,450), (-160,450), (-450,160), (-160,160), False, ''],
    2: [(-160,450), (160,450), (-160,160), (160,160), False, ''],
    3: [(160,450), (450,450), (160,160), (450,160), False, ''],
    4: [(-450,160), (-160,160), (-450,-160), (-160,-160), False,''],
    5: [(-160,160), (160,160), (-160,-160), (160,-160), False,''],
    6: [(160,160), (450,160), (160,-160), (450,-160), False,''],
    7: [(-450,-160), (-160,-160), (-450,-450), (-160,-450), False,''],
    8: [(-160,-160), (160,-160), (-160,-450), (160, -450), False,''],
    9: [(160,-160), (450,-160), (160, -450), (450, -450), False,'']
}

# Draw Functions
# takes left upper corner of the box
xandotr = turtle.Turtle()
xandotr.pensize(5)
xandotr.up()

def draw_x(c: tuple() ):
    xandotr.pencolor('yellow')
    xandotr.setpos(c[0],c[1])
    xandotr.down()
    xandotr.goto(c[0]+(450-160), c[1]-(450-160))
    xandotr.penup()
    xandotr.setpos(c[0]+290, c[1])
    xandotr.down()
    xandotr.goto(c[0], c[1]-290)
    xandotr.up()

def draw_o(c: tuple()):
    xandotr.pencolor('blue')
    xandotr.setpos(c[0]+(290//2),c[1]-290)
    xandotr.down()
    xandotr.circle(290//2)
    xandotr.up()

def reset():
    c[1][4] = False
    c[1][5] = ''
    c[2][4] = False
    c[2][5] = ''
    c[3][4] = False
    c[3][5] = ''
    c[4][4] = False
    c[4][5] = ''
    c[5][4] = False
    c[5][5] = ''
    c[6][4] = False
    c[6][5] = ''
    c[7][4] = False
    c[7][5] = ''
    c[8][4] = False
    c[8][5] = ''
    c[9][4] = False
    c[9][5] = ''

cout = 0
def play(x,y):
    global cout, xpoint, opoint

    # 1
    if x > c[1][0][0] and x < c[1][1][0] and y > c[1][2][1]:
        if cout % 2 == 0:
            if not c[1][4]:
                draw_x(c[1][0]) 
                c[1][4] = True
                cout += 1
                c[1][5] = 'X'
        else:
            if not c[1][4]:
                draw_o(c[1][0])
                c[1][4] = True
                cout += 1
                c[1][5] = 'O'
    # 2    
    elif x > c[2][0][0] and x < c[2][1][0] and y > c[2][2][1]:
        if cout % 2 == 0:
            if not c[2][4]:
                draw_x(c[2][0])
                c[2][4] = True
                cout += 1
                c[2][5] = 'X'
        else:
            if not c[2][4]:
                draw_o(c[2][0])
                c[2][4] = True
                cout += 1
                c[2][5] = 'O'
    # 3
    elif x > c[3][0][0] and x < c[3][1][0] and y > c[3][2][1]:
        if cout % 2 == 0:
            if not c[3][4]:
                draw_x(c[3][0])
                c[3][4] = True
                cout += 1
                c[3][5] = 'X'
        else:
            if not c[3][4]:
                draw_o(c[3][0])
                c[3][4] = True
                cout += 1
                c[3][5] = 'O'
    # 4            
    elif x > c[4][0][0] and x < c[4][1][0] and y > c[4][2][1]:
        if cout % 2 == 0:
            if not c[4][4]:
                draw_x(c[4][0])
                c[4][4] = True
                cout += 1
                c[4][5] = 'X'
        else:
            if not c[4][4]:
                draw_o(c[4][0])
                c[4][4] = True
                cout += 1
                c[4][5] = 'O'
    # 5
    elif x > c[5][0][0] and x < c[5][1][0] and y > c[5][2][1]:
        if cout % 2 == 0:
            if not c[5][4]:
                draw_x(c[5][0])
                c[5][4] = True
                cout += 1
                c[5][5] = 'X'
        else:
            if not c[5][4]:
                draw_o(c[5][0])
                c[5][4] = True
                cout += 1
                c[5][5] = 'O'
    # 6
    elif x > c[6][0][0] and x < c[6][1][0] and y > c[6][2][1]:
        if cout % 2 == 0:
            if not c[6][4]:
                draw_x(c[6][0])
                c[6][4] = True
                cout += 1
                c[6][5] = 'X'
        else:
            if not c[6][4]:
                draw_o(c[6][0])
                c[6][4] = True
                cout += 1
                c[6][5] = 'O'
    # 7
    elif x > c[7][0][0] and x < c[7][1][0] and y > c[7][2][1]:
        if cout % 2 == 0:
            if not c[7][4]:
                draw_x(c[7][0])
                c[7][4] = True
                cout += 1
                c[7][5] = 'X'
        else:
            if not c[7][4]:
                draw_o(c[7][0])
                c[7][4] = True
                cout += 1
                c[7][5] = 'O'
    # 8
    elif x > c[8][0][0] and x < c[8][1][0] and y > c[8][2][1]:
        if cout % 2 == 0:
            if not c[8][4]:
                draw_x(c[8][0])
                c[8][4] = True
                cout += 1
                c[8][5] = 'X'
        else:
            if not c[8][4]:
                draw_o(c[8][0])
                c[8][4] = True
                cout += 1
                c[8][5] = 'O'
    # 9
    elif x > c[9][0][0] and x < c[9][1][0] and y > c[9][2][1]:
        if cout % 2 == 0:
            if not c[9][4]:
                draw_x(c[9][0])
                c[9][4] = True
                cout += 1
                c[9][5] = 'X'
        else:
            if not c[9][4]:
                draw_o(c[9][0])
                c[9][4] = True
                cout += 1
                c[9][5] = 'O'

    txt = turtle.Turtle()
    if c[1][5]=='X'and c[2][5]=='X' and c[3][5]=='X':
        dot.hideturtle()
        xandotr.clear()
        txt.color('white')
        style = ('Arial', 30, 'italic')
        xpoint+=1
        txt.write(f"X won \n X: {xpoint} \n O: {opoint}", font=style, align='center')
        cout = 0
        time.sleep(2)
        txt.clear()
        dot.showturtle()
        reset()
    elif c[4][5]=='X'and c[5][5]=='X' and c[6][5]=='X':
        dot.hideturtle()
        xandotr.clear() 
        txt.color('white')
        style = ('Arial', 30, 'italic')
        xpoint+=1
        txt.write(f"X won \n X: {xpoint} \n O: {opoint}", font=style, align='center')
        cout = 0
        time.sleep(2)
        txt.clear()
        dot.showturtle()
        reset()
    elif c[7][5]=='X'and c[8][5]=='X' and c[9][5]=='X':
        dot.hideturtle()
        xandotr.clear() 
        txt.color('white')
        style = ('Arial', 30, 'italic')
        xpoint+=1
        txt.write(f"X won \n X: {xpoint} \n O: {opoint}", font=style, align='center')
        cout = 0
        time.sleep(2)
        txt.clear()
        dot.showturtle()
        reset()
    elif c[1][5]=='X'and c[4][5]=='X' and c[7][5]=='X':
        dot.hideturtle()
        xandotr.clear() 
        txt.color('white')
        style = ('Arial', 30, 'italic')
        xpoint+=1
        txt.write(f"X won \n X: {xpoint} \n O: {opoint}", font=style, align='center')
        cout = 0
        time.sleep(2)
        txt.clear()
        dot.showturtle()
        reset()
    elif c[2][5]=='X'and c[5][5]=='X' and c[8][5]=='X':
        dot.hideturtle()
        xandotr.clear() 
        txt.color('white')
        style = ('Arial', 30, 'italic')
        xpoint+=1
        txt.write(f"X won \n X: {xpoint} \n O: {opoint}", font=style, align='center')
        cout = 0
        time.sleep(2)
        txt.clear()
        dot.showturtle()
        reset()
    elif c[3][5]=='X'and c[6][5]=='X' and c[9][5]=='X':
        dot.hideturtle()
        xandotr.clear() 
        txt.color('white')
        style = ('Arial', 30, 'italic')
        xpoint+=1
        txt.write(f"X won \n X: {xpoint} \n O: {opoint}", font=style, align='center')
        cout = 0
        time.sleep(2)
        txt.clear()
        dot.showturtle()
        reset()
    elif c[1][5]=='X'and c[5][5]=='X' and c[9][5]=='X':
        dot.hideturtle()
        xandotr.clear() 
        txt.color('white')
        style = ('Arial', 30, 'italic')
        xpoint+=1
        txt.write(f"X won \n X: {xpoint} \n O: {opoint}", font=style, align='center')
        cout = 0
        time.sleep(2)
        txt.clear()
        dot.showturtle()
        reset()
    elif c[3][5]=='X'and c[5][5]=='X' and c[7][5]=='X':
        dot.hideturtle()
        xandotr.clear() 
        txt.color('white')
        style = ('Arial', 30, 'italic')
        xpoint+=1
        txt.write(f"X won \n X: {xpoint} \n O: {opoint}", font=style, align='center')
        cout = 0
        time.sleep(2)
        txt.clear()
        dot.showturtle()
        reset()
    elif c[1][5]=='O'and c[2][5]=='O' and c[3][5]=='O':
        dot.hideturtle()
        xandotr.clear() 
        txt.color('white')
        style = ('Arial', 30, 'italic')
        opoint+=1
        txt.write(f'O won \n X: {xpoint} \n O: {opoint}', font=style, align='center')
        cout = 0
        time.sleep(2)
        txt.clear()
        dot.showturtle()
        reset()
    elif c[4][5]=='O'and c[5][5]=='O' and c[6][5]=='O':
        dot.hideturtle()
        xandotr.clear() 
        txt.color('white')
        style = ('Arial', 30, 'italic')
        opoint+=1
        txt.write(f'O won \n X: {xpoint} \n O: {opoint}', font=style, align='center')
        cout = 0
        time.sleep(2)
        txt.clear()
        dot.showturtle()
        reset()
    elif c[7][5]=='O'and c[8][5]=='O' and c[9][5]=='O':
        dot.hideturtle()
        xandotr.clear() 
        txt.color('white')
        style = ('Arial', 30, 'italic')
        opoint+=1
        txt.write(f'O won \n X: {xpoint} \n O: {opoint}', font=style, align='center')
        cout = 0
        time.sleep(2)
        txt.clear()
        dot.showturtle()
        reset()
    elif c[1][5]=='O'and c[4][5]=='O' and c[7][5]=='O':
        dot.hideturtle()
        xandotr.clear() 
        txt.color('white')
        style = ('Arial', 30, 'italic')
        opoint+=1
        txt.write(f'O won \n X: {xpoint} \n O: {opoint}', font=style, align='center')
        cout = 0
        time.sleep(2)
        txt.clear()
        dot.showturtle()
        reset()
    elif c[2][5]=='O'and c[5][5]=='O' and c[8][5]=='O':
        dot.hideturtle()
        xandotr.clear() 
        txt.color('white')
        style = ('Arial', 30, 'italic')
        opoint+=1
        txt.write(f'O won \n X: {xpoint} \n O: {opoint}', font=style, align='center')
        cout = 0
        time.sleep(2)
        txt.clear()
        dot.showturtle()
        reset()
    elif c[3][5]=='O'and c[6][5]=='O' and c[3][9]=='O':
        dot.hideturtle()
        xandotr.clear() 
        txt.color('white')
        style = ('Arial', 30, 'italic')
        opoint+=1
        txt.write(f'O won \n X: {xpoint} \n O: {opoint}', font=style, align='center')
        cout = 0
        time.sleep(2)
        txt.clear()
        dot.showturtle()
        reset()
    elif c[1][5]=='O'and c[5][5]=='O' and c[9][5]=='O':
        dot.hideturtle()
        xandotr.clear() 
        txt.color('white')
        style = ('Arial', 30, 'italic')
        opoint+=1
        txt.write(f'O won \n X: {xpoint} \n O: {opoint}', font=style, align='center')
        cout = 0
        time.sleep(2)
        txt.clear()
        dot.showturtle()
        reset()
    elif c[3][5]=='O'and c[5][5]=='O' and c[7][5]=='O':
        dot.hideturtle()
        xandotr.clear() 
        txt.color('white')
        style = ('Arial', 30, 'italic')
        opoint+=1
        txt.write(f'O won \n X: {xpoint} \n O: {opoint}', font=style, align='center')
        cout = 0
        time.sleep(2)
        txt.clear()
        dot.showturtle()
        reset()
    

wn.onclick(play)


while True:
    wn.update()
