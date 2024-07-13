print ("hello world")

from tkinter import *
import ast
root =Tk()
i=0
def get_number(num):
    global i
    display.insert(i,num)
    i+=1

def get_operation(operator):
    global i
    length =len(operator)
    display.inert(i,operator)
    i+=length