# coding: cp866
import random


s_ai = 0
s_you = 0
s_buf = 0
b_a = 0
b_y = 0
f = 6

y = ["1", "2", "3", "4", "5", "6"]
a = ["1", "2", "3", "4", "5", "6"]

print("CHIPS")


def out():
    print("\n=====================================")
    print("   YOU   |", y[0], "|", y[1], "|", y[2], "|", y[3], "|", y[4], "|", y[5], "|")
    print("   AI    |", a[0], "|", a[1], "|", a[2], "|", a[3], "|", a[4], "|", a[5], "|")
    print("   Score:  ", "AI =", s_ai, " ||  YOU =", s_you)
    print("=====================================")


def sel():
    v = 0
    while (1 > v) or (v > 6):  #
        print("Choose chips: ")
        v = int(input())
    v -= 1
    i = v

    while y[i] == "X":
        print("Chips used")
        v = -1
        while (0 > v) or (v > 5):
            print("Choose chips: ")
            v = int(input())
            v -= 1
            i = v
    y[i] = "X"
    global s_buf
    s_buf = v + 1
    global b_y
    b_y = v + 1


def ai_sel():
    v = 0
    while (1 > v) or (v > 6):  # choose
        v = int(random.randint(1,6))
    i = v - 1
    # add X
    while a[i] == "X":
        v = 0
        while (1 > v) or (v > 6):
            v = int(random.randint(1,6))
        i = v - 1
    a[i] = "X"
    global s_buf
    s_buf += v
    print("AI: ", v)
    global b_a
    b_a = v


def ito():
    if b_a > b_y:
        global s_ai
        s_ai += s_buf
        global f
        f -= 1
    elif b_y > b_a:
        global s_you
        s_you += s_buf
        f -= 1
    else:
        print("Chips draw")
        a[b_a-1] = b_a
        y[b_y-1] = b_y


def win():
    if s_ai > s_you:
        print("AI WIN")
    elif s_you > s_ai:
        print("YOU WIN")
    else:
        print("DRAW")


def game():
    while f != 0:
        out()
        sel()
        ai_sel()
        ito()

    out()
    win()
    print("===  GAME OVER   ===")


game()