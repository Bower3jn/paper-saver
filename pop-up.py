import random
from guizero import App, Text, Picture, Window
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
        "Fun fact: 500 pieces of paper use about 6% of a tree!",
        "Fun fact: 1 tree makes about 8,333 sheets of paper!",
        """
        Fun fact: The average cost of a wasted piece of paper
        is about $0.06!
        """,
        """
        Fun fact: The average employee prints 6 wasted pages
        per day, that's 1,410 wasted pages per year!
        """, 
        """
        Fun fact: In 2004 the United States used 8 million tons
        of office paper (3.2 billion reams). That’s the equivalent
        of 178 million trees!
        """,
        """
        Fun fact: The U.S. is by far the world’s largest producer
        and consumer of paper. Per capita U.S. paper consumption
        is over six times greater than the world average.
        """,
        """
        Fun fact: In the United States, we use enough office paper
        each year to build a 10-foot-high wall that’s 6,815 miles 
        long. That’s more than the distance from New York to Tokyo!
        """,
        """
        Fun fact: Making one single sheet of copy paper can 
        use over 13oz. of water– more than a typical soda can!
        """,
        """
        Fun fact: Production of 1 ton of copy paper produces 
        19,075 gallons of waste water!
        """,
        """
        Fun fact: Production of 1 ton of copy paper produces
        2,278 lb of solid waste!
        """,
        """
        Fun fact: In 2003, paper and paperboard accounted
        for 35 percent of the total materials discarded in
        the United States.
        """,
        """
        Fun fact: One ton of paper requires the use of 98
        tons of various resources.
        """,
        """
        Fun fact: In the U.S. we have lost 95 percent of
        our old growth forests!
        """,
        """
        Fun fact: 4281 acres of rainforest are lost every 
        hour worldwide!
        """,
        """
        Fun fact: It takes 3 tons of wood to produce 
        1 ton of copy paper.
        """

    ]
#Selecting random series of text from list above and setting font and layout options
    message = Text(app,text=random.choice(arg),size="12",font="BASKERVILLE",width=400)
#Creating reply to user interference
    app.info("S.S.A", "Continue to print")
#Senerio when user clicks no
else:
#creating a way to close window when user clicks "no"
    def close_window():
        window.hide()
        Window = window.hide()
#Image displayed to make user feel good
    ecofriend =Picture(app,image="ecofriendly.gif") 
app.display()