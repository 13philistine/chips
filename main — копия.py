# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 20:51:38 2015

@author: Simon94
"""

import random


s_ai = 0
s_you = 0
s_buf = 0
b_a = 0
b_y = 0
f = 6



class ai():
    
    def __init__(self,a):
        self.a = a
        
    
    def ai_sel(self):
        v = 0
        while (1 > v) or (v > 6):  # choose
            v = int(random.randint(1,6))
        i = v - 1
        # add X
        while self.a[i] == "X":
            v = 0
            while (1 > v) or (v > 6):
                v = int(random.randint(1,6))
            i = v - 1
        self.a[i] = "X"
        global s_buf
        s_buf += v
        print("AI: ", v)
        global b_a
        b_a = v
        

class player():
    
    def __init__(self,y):
        self.y = y    
        
    def sel(self):
        v = 0
        while (1 > v) or (v > 6):  #
            print("Choose chips: ")
            v = int(input())
        v -= 1
        i = v
    
        while self.y[i] == "X":
            print("Chips used")
            v = -1
            while (0 > v) or (v > 5):
                print("Choose chips: ")
                v = int(input())
                v -= 1
                i = v
        self.y[i] = "X"
        global s_buf
        s_buf = v + 1
        global b_y
        b_y = v + 1

        
    

print("CHIPS")


def out(a,y):
    print("\n=====================================")
    print("   YOU   |", y[0], "|", y[1], "|", y[2], "|", y[3], "|", y[4], "|", y[5], "|")
    print("   AI    |", a[0], "|", a[1], "|", a[2], "|", a[3], "|", a[4], "|", a[5], "|")
    print("   Score:  ", "AI =", s_ai, " ||  YOU =", s_you)
    print("=====================================")





def ito(a,y):
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
    y = ["1", "2", "3", "4", "5", "6"]
    global a    
    a = ["1", "2", "3", "4", "5", "6"]
    AI = ai(a)
    Player = player(y)
    while f != 0:
        out(a,y)
        Player.sel()
        AI.ai_sel()
        ito(a,y)

    out(a,y)
    win()
    print("===  GAME OVER   ===")


game()
