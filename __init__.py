from tkinter import *

try:
    from main.tools import  *
    from main.items import  *
    from main.Globals import *
except ImportError:
    from Main.tools import  *
    from Main.items import  *
    from Main.Globals import *



content=[
    ]




colors= ["red","green","blue","orange","pink","violet","cyan","yellow","white","black"]
       
def DrawAll(canvas):
    canvas.delete('all')
    for c in content: c.Draw(canvas)
    toolsbar.draw(canvas)
    selected = globals['selected']
    if selected != None : selected.drawZone(canvas)
    

def OnMousePress(event):
    global selected
    if(event.y < 30):
        toolsbar.click(event)
        DrawAll(canvas)
        return
    selected = Here(event.x, event.y)
    globals['selected'] = selected
    if(selected == None):
        content.append( Rectangle(event.x-10, event.y-20,20,20,"red"))
    DrawAll(canvas)

    
def Here(x,y):
    for c in content:
        if(c.here(x,y)): return c
    return None

window = Tk()
window.title("Pinte")
canvas = Canvas(window,width = 800, height = 800)
canvas.pack()
toolsbar = Toolsbar()
 
rectangle = Rectangle(100,100,200,50,"pink")
content.append(rectangle)
content.append(Rectangle(350,100,50,200,"red"))
content.append(Circle(150, 200,50,"black"))
content.append(Line(200,500,100,50,"black"))
content.append(Oval(300,500,50,100,"yellow"))

window.bind("<ButtonPress-1>", OnMousePress)

DrawAll(canvas)


window.mainloop()