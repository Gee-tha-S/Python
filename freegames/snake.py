"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.


Version UPDATE
1. Faster snake
2. Snake can go around edges with no limits , has corner glitch
3. Color change of background, snake, and food
4. Game will force close after loosing
5. Largely prints 'YOU HAVE LOST'
6. When eaten itself entire snake turns red


"""

from turtle import *
from random import randrange
from freegames import square, vector
import time

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def printTitle():
    '''within the turtle screen prints YOU HAVE LOST '''
    penup()
    goto( 120, 50)
    pendown()
    color('red')
    style = ('courier', 35, 'italic')
    write('YOU HAVE LOST', font= style, align= 'right')
    hideturtle()
    
def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def lost():
    '''declares on screen and within the command line that the player lost and closes everything'''
    printTitle()
    print('YOU HAVE LOST')
    highScore(len(snake))
    time.sleep(3) 
    bye()
    SystemExit()                   

def wall(head,x,y):
    '''Creates no walls so the snake can go to the edge and reappear on the exact other edge'''
    if x == (-200):
        head.x = 190
        head.y = y
        head = (head.x, head.y)
        return(head)
    if y == (-200):
        head.x = x
        head.y = 190
        head = (head.x, head.y)
        return(head)
    if x == (190):
        head.x = -200
        head.y = y
        head = (head.x, head.y)
        return(head)
    if y == (190):
        head.x = x
        head.y = -200
        head = (head.x, head.y)
        return(head)
    '''slight glitch when entering the limit edge of the screen'''

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)
    game = 1

    if head in snake:
        game = 0
        for body in snake:
            square(body.x, body.y, 9, 'red')

    if game == 0:
        lost()
        return (head)
    
    if not inside(head):
        '''checks if the snake is going out of bounds to reappear on oppisite side'''
        wallx = head.x
        wally = head.y
        wall(head, wallx, wally)
        
    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        '''changed to be green snake, with yellow food, on a black background'''
        square(body.x, body.y, 9, 'green')

    square(food.x, food.y, 9, 'yellow')
    update()
    ontimer(move, 90)

def highScore(score):
    f = open("snake.txt","r")
    high = f.read()
    high = int(high)
    f.close()
    if score > high:
        open("snake.txt", "w").close()
        f = open("snake.txt","w")
        f.write(str(score))
        print('NEW HIGH SCORE')

setup(420, 420, 370, 0)
bgcolor('black')
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
