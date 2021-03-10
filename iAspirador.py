from Ambiente import *
import random
import turtle
from time import sleep


class IAspirador(Ambiente):
  def __init__(self, Ambiente):
    #localização do aspirador, se Local A ou B
    self.localasp = random.choice(["A","B"])
    print(40*"*")
    print("O ambiente está:", Ambiente.condlocad)
    self.Asp = turtle.Turtle()
    self.Asp.penup()
    self.Asp.setpos(0, 0)
    self.Asp.begin_fill()
    self.Asp.shape("circle")
    self.Asp.color("blue")
    self.Asp.end_fill()
    self.Asp.penup()

  def verifica_estado_aspirador(self, Ambiente):#sensor
    if self.localasp == "A":
      result1 = "O aspirador é colocado aleatoriamente no local A\n"
      self.Asp.speed(100)
      self.Asp.setpos(-120, 0)
      return print(result1)
    elif self.localasp == "B":
      result2 = "O aspirador é colocado aleatoriamente no local B\n"
      self.Asp.speed(100)
      self.Asp.setpos(120, 0)
      return print(result2)

  def verifica_estado_ambiente(self, Ambiente):#sensor
    #se o lado A estiver sujo
    if Ambiente.condlocad["A"] == 1 and Ambiente.condlocad["B"] == 0:
      if self.localasp == "B":
        print("O lado B já está limpo")
        IAspirador.move_se(self, Ambiente)
        print("O lado A está sujo...")
        IAspirador.aspiraA(self, Ambiente)
      else:
        print("O lado A está sujo...")
        IAspirador.aspiraA(self, Ambiente)
        IAspirador.move_se(self, Ambiente)
        print("O lado B já está limpo")

    elif Ambiente.condlocad["A"] == 0 and Ambiente.condlocad["B"] == 1:
      if self.localasp == "A":
        print("Lado A já está limpo")
        IAspirador.move_se(self, Ambiente)
        print("O lado B está sujo...")
        IAspirador.aspiraB(self, Ambiente)
      else:
        print("O lado B está sujo...")
        IAspirador.aspiraB(self, Ambiente)
        IAspirador.move_se(self, Ambiente)
        print("Lado A já está limpo")

    elif Ambiente.condlocad["A"] == 1 and Ambiente.condlocad["B"] == 1:
      if self.localasp == "A":
        print("O lado A está sujo...")
        #limpar o ambiente
        IAspirador.aspiraA(self, Ambiente)
        IAspirador.move_se(self, Ambiente)
        print("O lado B está sujo...")
        IAspirador.aspiraB(self, Ambiente)
      else:
        print("O lado B está sujo...")
        #limpar o ambiente
        IAspirador.aspiraB(self, Ambiente)
        IAspirador.move_se(self, Ambiente)
        print("O lado A está sujo...")
        IAspirador.aspiraA(self, Ambiente)

    else:
      if self.localasp == "A":
        print("O lado A já está limpo...")
        IAspirador.move_se(self, Ambiente)
        print("O lado B já está limpo...")
      else:
        print("O lado B já está limpo...")
        IAspirador.move_se(self, Ambiente)
        print("O lado A já está limpo...")
      print("\n---- Os dois lados estão limpos ----")

  def aspiraA(self, Ambiente):
    #Ambiente.A.color("pink")#durante limpeza
    sleep(.5)
    Ambiente.A.color("gray")
    Ambiente.condlocad["A"] = 0
    print("O lado A foi limpo!")

  def aspiraB(self, Ambiente):
    #Ambiente.A.color("pink")
    sleep(.5)
    Ambiente.B.color("gray")
    Ambiente.condlocad["B"] = 0
    print("Lado B foi limpo!")

  def move_se(self, Ambiente):
    if self.localasp == "A":
      print("\nMove-se para o lado B...")
      IAspirador.localasp = "B"
      sleep(2.25)
      self.Asp.forward(240)
    else:
      print("\nMove-se para o lado A...")
      IAspirador.localasp = "A"
      sleep(2.25)
      self.Asp.back(240)

#LIMPANDO:
OAmbiente = Ambiente()
OAspirador = IAspirador(OAmbiente)
OAspirador.verifica_estado_aspirador(OAmbiente)
OAspirador.verifica_estado_ambiente(OAmbiente)
# mostra ao final os dois lados limpos
print("Após ação do aspirador, o ambiente está: ", OAmbiente.condlocad)

turtle.done()