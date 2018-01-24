#########################################
#Autor:Diego Lopes da Silva             #
#Data:04/12/2017                        #
#Descrição:Drivers para ligar e desligar#
#########################################
import os

def cutOn():
    os.system("echo A > /dev/ttyACM0")

def cutOff():
    os.system("echo D > /dev/ttyACM0")

