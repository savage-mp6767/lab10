##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()

w = 800
h = 600

housex = w / 3
housey = h / 2
housex1 = w - (w / 4)
housey1 = h

# Create the canvas widget
drawpad = Canvas(root, width=w,height=h, background='white')
drawpad.grid(row=0, column=1)

# Insert your code here to draw the house!
drawpad.create_rectangle(0,h / 4,w,h,fill="darkgreen") #grass

drawpad.create_rectangle(housex,housey,housex1,housey1,fill="#94000c") #main room
drawpad.create_rectangle(housex + 25,housey,housex + 100,housey - 125,fill="#94000c") #chimney
drawpad.create_rectangle(housex + 15,housey - 110,housex + 110,housey - 125,fill="#94000c")

drawpad.create_polygon(housex, housey,housex + 167, housey - 145, housex1, housey,fill = "#661d00") #roof
drawpad.create_line(housex, housey, housex + 167, housey - 145) #roof outline because create_polygon doesn't do lines
drawpad.create_line(housex1, housey, housex + 167, housey - 145) 

drawpad.create_rectangle(housex + 100,housey + 100,housex1 - 100,housey1,fill="#661d00") #door
drawpad.create_oval(housex + 225, housey + 225, housex1 - 115, housey1 - 95, fill="#000000") #doorhandle

drawpad.create_rectangle(housex + 125,housey + 125,housex1 - 125,housey1 - 25,fill = "lightblue") #door window
drawpad.create_line(housex + 167, housey + 125, housex1 - 167, housey1 - 25)
#drawpad.create_line(housex + 125, housey + 150, housex1 - 125, housey1 - 150)
drawpad.create_line(housex + 125, housey + 175, housex1 - 125, housey1 - 125)
#drawpad.create_line(housex + 125, housey + 200, housex1 - 125, housey1 - 100)
drawpad.create_line(housex + 125, housey + 225, housex1 - 125, housey1 - 75)
#drawpad.create_line(housex + 125, housey + 250, housex1 - 125, housey1 - 50)

drawpad.create_rectangle(housex + 25,housey + 25,housex1 - 25,housey1 - 225,fill = "lightblue") #above-door window
drawpad.create_line(housex + 25, housey + 50, housex1 - 25, housey1 - 250)
drawpad.create_line(housex + 167, housey + 25, housex1 - 167, housey1 - 225)
drawpad.create_line(housex + 167 / 2, housey + 25, housex1 - 167 - 84, housey1 - 225)
drawpad.create_line(housex + 167 + 84, housey + 25, housex1 - 167 + 84, housey1 - 225)

root.mainloop()
