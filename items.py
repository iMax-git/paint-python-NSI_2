'''
Created on 23 sept. 2020

@author: tdiard
'''
from math import sqrt

 
class Rectangle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y 
        self.width = width
        self.height = height
        self.color = color
        self.fg = "black"
    
    def Draw(self, canvas):
        canvas.create_rectangle(self.x,self.y,self.x+self.width,self.y+self.height, fill=self.color, outline=self.fg)
    
    def drawZone(self, canvas):
        canvas.create_rectangle(self.x-5,self.y-5,self.x+5,self.y+5, fill=None, outline="black")
        canvas.create_rectangle((self.x+self.width)-5,(self.y+self.height)-5,self.x+self.width+5,self.y+self.height+5, fill=None, outline="black")
        canvas.create_rectangle(self.x+-5,(self.y+self.height)-5,self.x+5,self.y+self.height+5, fill=None, outline="black")
        canvas.create_rectangle((self.x+self.width)-5,self.y-5,self.x+self.width+5,self.y+5, fill=None, outline="black")
    
    def here(self, x, y):
        if(x < self.x): return False
        if(x > self.x + self.width): return False
        if(y < self.y): return False
        if(y > self.y + self.height): return False
        return True
    

class Circle:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y 
        self.radius = radius
        self.color = color
    
    def Draw(self, canvas):
        canvas.create_oval(self.x,self.y,self.x+self.radius,self.y+self.radius, fill=self.color)
        
    def drawZone(self, canvas):
        canvas.create_rectangle(self.x-5,self.y-5,self.x+5,self.y+5, fill=None, outline="black")
        canvas.create_rectangle((self.x+self.radius)-5,(self.y+self.radius)-5,self.x+self.radius+5,self.y+self.radius+5, fill=None, outline="black")
        canvas.create_rectangle(self.x+-5,(self.y+self.radius)-5,self.x+5,self.y+self.radius+5, fill=None, outline="black")
        canvas.create_rectangle((self.x+self.radius)-5,self.y-5,self.x+self.radius+5,self.y+5, fill=None, outline="black")
    
    def here(self, x, y):
        if(x < self.x): 
            return False
        if(x > self.x + self.radius): 
            return False
        if(y < self.y): 
            return False
        if(y > self.y + self.radius): 
            return False
        return True

class Line:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y 
        self.width = width
        self.height = height
        self.color = color
    
    def Draw(self, canvas):
        canvas.create_line(self.x,self.y,self.x+self.width,self.y+self.height, fill=self.color)
    
    def drawZone(self, canvas):
        canvas.create_rectangle(self.x-5,self.y-5,self.x+5,self.y+5, fill=None, outline="black")
        canvas.create_rectangle((self.x+self.width)-5,(self.y+self.height)-5,self.x+self.width+5,self.y+self.height+5, fill=None, outline="black")

        
    def here(self, x, y):
        if(x < self.x): return False
        if(x > self.x + self.width): return False
        if(y < self.y): return False
        if(y > self.y + self.height): return False
        r = sqrt(self.width*self.width+self.height*self.height)
        a = self.height/r
        b = -self.width/r
        c = ((self.x+self.width)*self.y-self.x*(self.y+self.height))/r
        d = a * x + b * y +c
        if(d>5): return False
        if(d<-5): return False
        return True
        
class Oval:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y 
        self.width = width
        self.height = height
        self.color = color
    
    def Draw(self, canvas):
        canvas.create_oval(self.x,self.y,self.x+self.height,self.y+self.width, fill=self.color)
    
    def drawZone(self, canvas):
        canvas.create_rectangle(self.x-5,self.y-5,self.x+5,self.y+5, fill=None, outline="black")
        canvas.create_rectangle((self.x+self.height)-5,(self.y+self.width)-5,self.x+self.height+5,self.y+self.width+5, fill=None, outline="black")
        canvas.create_rectangle(self.x+-5,(self.y+self.width)-5,self.x+5,self.y+self.width+5, fill=None, outline="black")
        canvas.create_rectangle((self.x+self.height)-5,self.y-5,self.x+self.height+5,self.y+5, fill=None, outline="black")
            
    def here(self, x, y):
        if(x < self.x): return False
        if(x > self.x + self.height): return False
        if(y < self.y): return False
        if(y > self.y + self.width): return False
        return True
    