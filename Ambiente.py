import random
import turtle

class Ambiente(object):
  def __init__(self):
    # 0 é o estado LIMPO    :   1 é o estado SUJO
    #condições iniciais dos estados ou seja SUJO e SUJO, inicialmente | A lado A e B lado B. || Limpo : "gray" sujo : "red"
    self.condlocad = {"A":"1", "B":"1"}
    #As condições das localizações tornam-se aleatórias
    self.condlocad["A"] = random.choice([0,1])
    self.condlocad["B"] = random.choice([0,1])
    #construção dos lados (turtle)
    self.A = turtle.Turtle()
    self.A.penup()
    self.A.setpos(-120, 0)
    self.A.begin_fill()
    self.A.shape("square")
    self.A.turtlesize(5)
    if self.condlocad["A"]==1: 
        self.A.color("red")
    if self.condlocad["A"]==0:
        self.A.color("gray")
    self.A.end_fill()
    self.B = turtle.Turtle()
    self.B.penup()
    self.B.setpos(120, 0)
    self.B.begin_fill()
    self.B.shape("square") 
    self.B.turtlesize(5)
    if self.condlocad["B"]==1: 
        self.B.color("red")
    if self.condlocad["B"]==0:
        self.B.color("gray")
    self.B.end_fill()


    self.t1 = turtle.Turtle()
    self.t2 = turtle.Turtle()
    self.t3 = turtle.Turtle()
    self.t4 = turtle.Turtle()

    self.t1.penup()
    self.t1.begin_fill()
    self.t1.setpos(-140, 60)
    self.t1.write("Lado A", align="center", font=("Arial", 15, "normal"))
    self.t2.end_fill()
    self.t1.penup()

    self.t2.penup()
    self.t2.begin_fill()
    self.t2.setpos(140, 60)
    self.t2.write("Lado B", align="center", font=("Arial", 15, "normal"))
    self.t2.end_fill()
    self.t2.penup()

   
   