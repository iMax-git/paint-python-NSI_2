'''
Created on 23 sept. 2020

@author: tdiard
'''
from main.Globals import *

colors= ["red","green","blue","orange","pink","violet","cyan","yellow","white","black"]


class Toolsbar:
    def __init__(self):
        self.buttons = []
        self.endx = 0
        for c in colors:
            self.add(ColorButton(c))
        for stroke in range(4):
            self.add(StrokeButton(stroke))
        
    def add(self, button):
        self.buttons.append(button)
        button.x = self.endx
        button.y = 5
        self.endx += button.width
        
    def draw(self, canvas):
        canvas.create_rectangle(0,0,self.endx+5,40, fill="white")
        for b in self.buttons: 
            b.draw(canvas)
    
    def click(self,event):
        x = event.x
        for b in self.buttons: 
            if(x < b.width):
                b.click(event)
                return
            x -= b.width
            
class ColorButton:
    def __init__(self, value):
        self.value = value
        self.width = 30
        self.height = 30
    
    def draw(self, canvas):
        canvas.create_rectangle(self.x,self.y,self.x+self.width,self.y+self.height, fill=self.value)          
            
    def click(self, event):
        if(event.num == 1):
            globals["bg"] = self.value
            selected = globals['selected']
            if(selected != None):
                selected.color = self.value
        else:
            globals["bg"] = self.value
            selected = globals['selected']
            if(selected != None):
                selected.fg = self.value
        print(selected)

class StrokeButton:
    def __init__(self, value):
        self.value = value
        self.width = 30
        self.height = 30
    
    def draw(self, canvas):
        canvas.create_rectangle(self.x,self.y,self.x+self.width,self.y+self.height)
        canvas.create_line(self.x,self.y,self.x+self.width,self.y+self.height, width=(self.value+1)) 
            
    def click(self, event):
        if(event.num == 1):
            globals["stroke"] = self.value
            selected = globals['selected']
            if(selected != None):
                selected.width = self.value
        print(selected)
        print(self.value)
