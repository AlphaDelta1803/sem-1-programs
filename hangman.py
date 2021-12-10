import random, time
import turtle

turtle.color("black")
turtle.speed(1)


def stand():
    turtle.forward(100)
    turtle.backward(50)
    turtle.left(90)
    turtle.forward(250)
    turtle.right(90)
    turtle.forward(90)
    turtle.right(90)
    turtle.forward(30)


def head():
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(20)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)


def hands():
    turtle.forward(30)
    turtle.right(87)
    turtle.forward(42)
    turtle.right(180)
    turtle.forward(42)
    turtle.right(6)
    turtle.forward(42)
    turtle.right(180)
    turtle.forward(42)
    turtle.left(93)


def body():
    turtle.forward(30)
    turtle.right(37)


def leg():
    turtle.forward(42)
    turtle.right(180)
    turtle.forward(42)
    turtle.right(106)
    turtle.forward(42)


def face():
    turtle.penup()
    turtle.left(180)
    turtle.forward(42)
    turtle.right(37)
    turtle.forward(87)
    turtle.left(90)
    turtle.forward(8)
    turtle.right(90)
    turtle.pendown()
    turtle.left(30)
    turtle.forward(5)
    turtle.backward(10)
    turtle.forward(5)
    turtle.right(90)
    turtle.forward(5)
    turtle.backward(10)
    turtle.forward(5)
    turtle.penup()
    turtle.right(30)
    turtle.forward(17)
    turtle.left(30)
    turtle.pendown()
    turtle.forward(5)
    turtle.backward(10)
    turtle.forward(5)
    turtle.left(90)
    turtle.forward(5)
    turtle.backward(10)
    turtle.forward(5)
    turtle.penup()
    turtle.right(30)
    turtle.backward(17)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(3)
    turtle.backward(21)
    turtle.forward(18)
    turtle.right(85)
    turtle.forward(4)
    turtle.right(80)
    turtle.forward(3)
    turtle.right(80)
    turtle.forward(3)
    turtle.forward(1)
    turtle.hideturtle()
    time.sleep(1000)


answerList = ["world", "animation", "africa", "computer", "rickshaw", "physics", "chemistry", "inception"]
vowelsList = ["a", "e", "i", "o", "u"]
L = [face, leg, body, hands, head, stand]
random.shuffle(answerList)
answer1 = answerList[0]
answer = list(answerList[0])
display = []
display.extend(answer)

for i in range(len(display)):
    w = 0
    for j in range(len(vowelsList)):
        if display[i] == vowelsList[j]:
            w = 1
    if w == 0:
        display[i] = "_"
print(" ".join(display))
print()

count = 6

while count > 0 and display != answer:
    guess = input("Please guess a letter: ")

    c = 0
    for i in range(len(answer)):
        if answer[i] == guess:
            display[i] = guess
            c = 1
    print(" ".join(display))
    print()
    if c == 0:
        count -= 1
        L[count]()
    print(count)

    if count == 0:
        print("Sorry you lost...better luck next time.The word was", answer1)
if count != 0:
    print("Well done you guessed the word")
