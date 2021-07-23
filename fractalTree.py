#import the math module and the graphics module
from graphics import GraphWin, Point, Line, color_rgb
from math import sin,cos,pi


#define the height and width of the canvas
width,height = 700,700

#editable values    
xStart = width /2               #the starting x pos of the tree ( should be bottom of the trunk )
yStart = height - height/10     #the starting y pos of the tree ( should be bottom of the trunk )
trunkLength = 100               #length of the trunk / first branch                  
angle_delta = 0.25              #size of the angle from a straight branch 
widthS = 6                      #width of the first branch 
min_len = 8                     #min length of a branch ( the point of the end of the recursion )
width_factor = 0.75             #the multiplier for the width of a branch with each layer of recursion

#create the canvas
canvas = GraphWin('Fractal Tree',width,height)

#define the starting direction 
direction = -pi/2    

#colors are set so the tree goes from brown to green 
redS = 150                  #red starting color
greenS = 5                  #green starting color
blueS = 0                   #blue starting color


#recursive branch function
def branch(x,y,l,theta,heading,r,g,b,w, min_len, width_factor):
    #if the length is less than min_len then break out of the recursion
    if l < min_len: return
    #get the change in x and y using the current length a trig functions of the direction
    delta_x = l * cos(heading)
    delta_y = l * sin(heading)

    #add that to the currect x and y values
    x2 = x + delta_x
    y2 = y + delta_y

    #draw a line from the start values to the calculated values
    line = Line(Point(x,y), Point(x2,y2))
    #set the color of the line (branch) to the r,g,b values
    line.setOutline(color_rgb(r,g,b))
    #set the width of the branch to the width
    line.setWidth(w)
    #draw the line to the canvas
    line.draw(canvas)

    #calculate the limits of the colors 
    if g + 10 > 255: g = 255
    if r -10 < 0: r = 0

    #recursive branch so that each branch has 2 new branches 
    branch(x2,y2,l-(l/5), theta,heading-theta,r-10,g+10,b,w*width_factor,min_len, width_factor)
    branch(x2, y2, l -(l/5),theta, heading +theta,r-10,g+10,b,w*width_factor,min_len, width_factor)


#call the first branch function
branch(xStart,yStart,trunkLength,angle_delta,direction,redS,greenS,blueS,widthS, min_len, width_factor)

#on mouse click close the canvas
canvas.getMouse()
canvas.close()