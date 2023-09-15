import sys
import turtle
import math

helpStr="\n a demonstration of several drawings using built-in turtle module "
helpStr+="\n\n command:\t draw [# of item to draw]\n\n"
helpStr+=" items:"

a = sys.argv
    
def main():
    if len(a)<2 or a[1]=="?" or a[1]=="help":
        print(helpStr)
        for i in range(0,len(lst)):
            print("\t\t",i+1,".  ",lst[i][0])
    else:
        if not isIntInRange(a[1]):
            print("INPUT ERROR!")
            exit()
        item = int(a[1])
        # initialize turtle #
        global wn
        wn = turtle.Screen()
        wn.bgcolor("black")
        wn.title("Turtle - "+lst[item-1][0].upper())
        global ttt
        ttt = turtle.Turtle()
        ttt.color("white")
        ttt.shape("turtle")
        ttt.speed(2)
        # choose item #
        print(lst[item-1][0])
        lst[item-1][1]()
        # halt after done drawing #
        turtle.done()


##################################
    
def isIntInRange(value):
    try:
        return int(value)>0 and int(value)<=len(lst)
    except ValueError:
        return False

##################################

# 1
def square():
    regular_polygon(4)

# 2
def circle():
    ttt.circle(150)

# 3    
def triangle():
    regular_polygon(3)

# 4 
def infinity():
    r = 150     # radius
    cycles = 2  # at least 2 !
    ttt.right(45)
    for i in range(1,cycles+1):
        ttt.circle(r,90)
        ttt.circle(r//2,90)
        ttt.circle(r,90)
        ttt.fd(r)
        ttt.circle(-r,90)
        ttt.circle(-r//2,90)
        ttt.circle(-r,90)
        if i!=cycles:
            ttt.fd(r)
    ttt.fd(r//2)
    
# 5
def spiral_inout():
    r=20
    for i in range(0,280,5):
        ttt.circle(r+i,60)

# 6
def spiral_outin():
    r=180
    for i in range(0,180,5):
        ttt.circle(r-i,60)


# 7

    # helper function
def sqrfunc_inout(size):
    for i in range(4):
        ttt.fd(size)
        ttt.left(90)
        size = size + 5
        
    # main drawing function    
def sqr_spiral_inout():
    for i in range(6,166,20):
        sqrfunc_inout(i)

# 8

    # helper function
def sqrfunc_outin(size):
    for i in range(4): 
            ttt.fd(size) 
            ttt.left(90) 
            size = size-5

    # main drawing function  
def sqr_spiral_outin():
    for i in range(146,6,-20):
        sqrfunc_outin(i)

# 9    
def star():
    for i in range(5):
        ttt.forward(200)
        ttt.right(144)

# 10

poslst = [(5,4),(-100,-50),(100,50),(-50,100),
          (150,-100),(-50,200), (200,-200),(-200,-200),
          (250,250),(-200,50),(-300,200),(-300,0),
          (0,-200),(300,0),(75,300),(-80,300)]

def gotopos(i):
    ttt.penup()
    ttt.goto(poslst[i][0],poslst[i][1])
    ttt.pendown()

def draw_star(size):
    for i in range(5):
        ttt.forward(size)
        ttt.right(144)
        
def star_sky():
    for i in range(0,len(poslst)):
        gotopos(i)
        draw_star(70)

# 11    
def hexagon():
    regular_polygon(6)

# 12        
def pentagon():
    regular_polygon(5)

# 13
def septagon():
    regular_polygon(7)

# 14
def octagon():
    regular_polygon(8)

# 15
def nested_infinity():
    r = 220
    ttt.right(45)
    for _ in range(1,11):
            ttt.fd(r//2)
            ttt.circle(r,90)
            ttt.circle(r//2,90)
            ttt.circle(r,90)
            ttt.fd(r)
            ttt.circle(-r,90)
            ttt.circle(-r//2,90)
            ttt.circle(-r,90)
            ttt.fd(r//2)
            r -= 20

# 16
def ellipse(rad):
    ttt.circle(rad,90)
    ttt.circle(rad//2,90)
    ttt.circle(rad,90)
    ttt.circle(rad//2,90)
    
def ellipse_special():
    # wn.setup(500,500)
    colors = ['violet','blue','green','yellow','orange','red']
    val,ind=10,0
    ttt.speed(10)
    for i in range(36):
        ttt.seth(-val)
        ttt.color(colors[ind%len(colors)])
        ind+=1
        ellipse(125)
        val+=10
    ttt.hideturtle()

# 17
def infinity_spiral():
    ttt.penup()
    ttt.goto(100,0)
    ttt.pendown()
    r=20
    ttt.right(60)
    for i in range(0,115,5):
        ttt.circle(r+i,60)
    ttt.fd(115)
    for i in range(115,0,-5):
        ttt.circle(-r-i,60)

# 18
def flower():
    colors = ['violet','yellow','red','blue']
    color = 0
    r = 100
    angle = 0
    for i in range(0,180,45):
        ttt.color(colors[color])
        color +=1
        angle += i
        ttt.right(i)
        ttt.fd(r//2)
        ttt.circle(r,90)
        ttt.circle(r//2,90)
        ttt.circle(r,90)
        ttt.fd(r)
        ttt.circle(-r,90)
        ttt.circle(-r//2,90)
        ttt.circle(-r,90)
        ttt.fd(r//2)
    ttt.hideturtle()

# 19
def cube():
    base_side = 175
    angle = 30
    factor = 3/4
    # bottom base
    ttt.left(angle)
    ttt.fd(base_side*(factor))
    ttt.right(angle)
    ttt.fd(base_side*(1/factor))
    ttt.right(180-angle)
    ttt.fd(base_side*(factor))
    ttt.right(angle)
    ttt.fd(base_side*(1/factor))
    # front face
    ttt.right(90)
    ttt.fd(base_side)
    ttt.right(90)
    ttt.fd(base_side*(1/factor))
    ttt.right(90)
    ttt.fd(base_side)
    # right face
    ttt.left(90+angle)
    ttt.fd(base_side*factor)
    ttt.left(90-angle)
    ttt.fd(base_side)
    ttt.left(90+angle)
    ttt.fd(base_side*factor)
    # top base
    ttt.right(angle)
    ttt.fd(base_side*(1/factor))
    ttt.right(180-angle)
    ttt.fd(base_side*factor)
    ttt.right(angle)
    ttt.fd(base_side*(1/factor))
    # last side
    ttt.right(90)
    ttt.fd(base_side)
    ttt.right(90)
    ttt.fd(base_side*(1/factor))
    ttt.right(90)
    ttt.fd(base_side)
    # done , adios !
    ttt.hideturtle()

# 20
def helix():
    # initial position
    ttt.penup()
    ttt.goto(300,300)
    ttt.pendown()
    # draw helix as series of ellipses
    r = 80
    for i in range(25):
        ttt.circle(-r,90)
        ttt.circle(-r//2,90)
        ttt.circle(-r,90)
        ttt.circle(-r//4,90)
    ttt.circle(-r,90)
    ttt.circle(-r//2,90)
    ttt.circle(-r,90)
    ttt.hideturtle()

# 21
def benzene():
    ttt.hideturtle()
    colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
    t = turtle.Pen()
    t.hideturtle()
    t.speed(0)
    for x in range(360): 
        t.pencolor(colors[x%6]) 
        t.width(x/100 + 1) 
        t.forward(x) 
        t.left(59)

# 22
def tree_fractal():
    ttt.speed(0)
    ttt.left(90)
    angle = 30
    y(90,9,angle)
    ttt.hideturtle() # adios !

def y(sz, level,angle):
    if (level >0):
        turtle.colormode(255)
        # base / trunk
        ttt.pencolor(0,255//level,0)
        ttt.fd(sz)
        # right sub-tree
        ttt.right(angle)
        y(0.8*sz,level-1,angle)
        # left sub-tree
        ttt.pencolor(0,255//level,0)
        ttt.left(2*angle)
        y(0.8*sz,level-1,angle)
        # go backwards
        ttt.pencolor(0,255//level,0)
        ttt.right(angle)
        ttt.fd(-sz)

# 23
def sine():
    # initial position
    ttt.penup()
    ttt.goto(-300,0)
    ttt.pendown()
    amplitude = 75
    for x in range(-300,301):
        ttt.goto(x,amplitude*math.sin((x/100)*2*math.pi))
    ttt.hideturtle()
    

## helper function for several ones above ##
def regular_polygon(sides):
    side_length = 150
    angle = 360.0 / sides
    for i in range(sides):
        ttt.forward(side_length)
        ttt.right(angle)
    
##################################

## main list which maps items to their functions ##
        
lst = [
       ["square",square],                           # 1 
       ["circle",circle],                           # 2
       ["triangle",triangle],                       # 3
       ["infinity",infinity],                       # 4
       ["spiral in-out",spiral_inout],              # 5
       ["spiral out-in",spiral_outin],              # 6
       ["square-spiral in-out",sqr_spiral_inout],   # 7
       ["square-spiral out-in",sqr_spiral_outin],   # 8
       ["star",star],                               # 9 
       ["star sky",star_sky],                       # 10
       ["hexagon",hexagon],                         # 11
       ["pentagon",pentagon],                       # 12
       ["septagon",septagon],                       # 13
       ["octagon",octagon],                         # 14
       ["nested infinity",nested_infinity],         # 15
       ["ellipses colorful special",ellipse_special],  #16
       ["spiral of infinity",infinity_spiral],      # 17
       ["flower",flower],                           # 18
       ["cube",cube],                               # 19
       ["helix",helix],                             # 20
       ["Rainbow Benzene", benzene],                # 21
       ["Y Fractal Tree", tree_fractal],            # 22
       ["sine wave", sine],                         # 23
       ]

##################################

if __name__=="__main__": 
    main()

