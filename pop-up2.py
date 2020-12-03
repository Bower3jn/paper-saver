from guizero import App, Text, Picture, Window
import random
from PIL import Image

#Creating App
app = App(title="System Sustainability Assistant")
#Creating yes no user interface 
printinglmt = app.yesno("S.S.A", "Are you sure you need to print?")

#Senerio when user clicks "yes"
if printinglmt == True:
#import GIF's
    img= [
        "deforest.gif",
        "cutwood.gif",
        "deforestation-brazil.gif",
        "view.gif"
    ]
#Selecting random file from previous list to display and setting layout options
    picture = Picture(app,image=random.choice(img), width=400, height=275, align="top")
#Creating a list of messages   
    arg = [
        "Trees help us breathe Trees are important",
        "Trees are important Trees are important 2"
    ]
#Selecting random series of text from list above and setting font and layout options
    message = Text(app,text=random.choice(arg),size="10",font="Proxima Nova",width=400)
#Creating reply to user interference
    app.info("S.S.A", "Continue to print")
#Senerio when user clicks no
else:
#creating a way to close window when user clicks "no"
    def close_window():
        window.hide()
        window.hide()
    reward = Text(app,text="ie. good job",size="10",font="Proxima Nova",width=400)
    
    
app.display()