# -*- coding: utf-8 -*-
"""
Game link - https://www.miniclip.com/games/sushi-go-round/en/
@author: NarutoNick
"""
#-------------------------------------------------------------------------------------------------------------------------------------------
""" 
All coordinates assume a screen resolution of 1280x1024, and Chrome 
maximized with the Bookmarks Toolbar enabled with 50% zoom Out
x_pad = 583
y_pad = 198
Play area =  x_pad+1, y_pad+1, 796, 825
"""
#-------------------------------------------------------------------------------------------------------------------------------------------
# Importing libraries -
#-------------------------------------------------------------------------------------------------------------------------------------------

from PIL import ImageGrab as imgb
# It gives us the basic screen gabbing functionality our bot will rely on

from PIL import ImageOps as imop
#  It is used to perform operations (such as grayscaling) on an Image.

import os
# This gives us the ability to easily navigate around our operating system's directories

import time
# Well use this mostly for stamping the current time onto snapshots, 
# but it can be very useful as a timer for bots that need events triggered over a given number of seconds.

import win32api,win32con
# To get pointer location or to use mouse or keyboard in the game

import numpy as np

#------------------------------------------------------------------------------------------------------------------------------
#
#GLOBAL VARIABLE 
#
#------------------------------------------------------------------------------------------------------------------------------
#
x_pad=583
y_pad=198
#
# These will be used to store the relationship between the game area and the rest of the screen. 
# This will make it very easy to port the code from place to place since every new coordinate will be relative to these 
# two global variables we're going to create, and to adjust for changes in screen area, all that's required is to reset these two variables.
#
foodOnHand={
        'shrimp':5,
        'rice':10,
        'nori':10,
        'roe':10,
        'salmon':5,
        'unagi':5
        }

sushiTypes={
        1236:'onigiri', 
        2134:'caliroll',
        1370:'gunkan',
        1497:'gunkan',
        1274:'dragonroll',
        1338:'dragonroll'
        }


class Blank:
    seat_1=3973
    seat_2=2437
    seat_3=8178
    seat_4=6641
    seat_5=3138
    seat_6=6220
#------------------------------------------------------------------------------------------------------------------------------#Defining Function -
#------------------------------------------------------------------------------------------------------------------------------
def screenGrab():
    #
    # The first line def screenGrab() defines the name of our function. 
    # The empty parentheses mean it expects no arguments.
    #
    # box=() assigns an empty tuple to a variable named "box".
    #
    # im = ImageGrab.grab() creates a full snapshot of your screen and returns an RGB image to the instance im.
    #
    # The first part im.save() calls the "save" method from the Image class. 
    # It expects two arguments. The first is the location in which to save the file, 
    # and the second is the file format.
    #
    # Here we set the location by first calling os.getcwd(). 
    # This gets the current directory the code is being run from and returns it as a string. We next add a +.
    # This will be used in between each new argument to concatenate all of the strings together.
    # The next piece '\\full_snap__ give our file a simple descriptive name. 
    # (Because the backslash is an escape character in Python, we have to add two of them to avoid cancelling out 
    # one of our letters).
    
    # str(int(time.time()). This takes advantage of Python's built-in Type methods.
    #
    # time.time() returns the number of seconds since Epoch, which is given as a type Float. 
    # Since we're creating a file name we can't have the decimal in there, so we first convert it to an integer by 
    # wrapping it in int(). This gets us close, but Python can't concatenate type Int with type String, so the last
    # step is to wrap everything in the str() function to give us a nice usable timestamp for the file name. 
    # 
    # From here, all that remains is adding the extension as part of the string: + '.png' and passing 
    # the second argument which is again the extension's type: "PNG".
    #
    #
    #
    # The ImageGrab.grab() function accepts one argument which defines a bounding box.
    # This is a tuple of coordinates following the pattern of (x,y,x,y) where,
    # The first pair of values (x,y.. defines the top left corner of the box
    # The second pair ..x,y) defines the bottom right.
    # Combining these allows us to only copy the part of the screen we need.
    
    box=(x_pad+1,y_pad+1,x_pad+480,y_pad+360)
    im=imgb.grab(box)
    #im.save(os.getcwd()+'\\full_snap__'+str(time.time())+'.png', 'PNG') //TO SAVE THE SCREENSHOTS
    return im

# End of ScreenGrab function -
#
#------------------------------------------------------------------------------------------------------------------------------
#
# Function Grab -
#
#-------------------------------------------------------------------------------------------------------------------------------------------
#
#def Grab():
#    '''
#    Line 2: We're taking a screengrab just as we have before, 
#            but now we're converting it to grayscale before we assign it to the
#            instance im. Converting to grayscale makes traversing all of the color 
#            values much faster; instead of each pixel having a Red, Green, and 
#            Blue value, it only has one value ranging from 0-255.
#
#    Line 3: We create an array of the image's color values using the PIL method 
#            getcolors() and assign them to the variable a
#
#    Line 4: We sum all the values of the array and print them to the screen. 
#            These are the numbers we'll use when we compare two images.
#            
#    '''
#    box=(x_pad+1,y_pad+1,x_pad+480,y_pad+360)
#    im=imop.grayscale(imgb.grab(box))
#    a=np.array(im.getcolors())
#    a=a.sum()
#    print(a)
#    return a

# End of Grab function -
#
#------------------------------------------------------------------------------------------------------------------------------

# Function LeftClick, LeftUp, and LeftDown -
#
#------------------------------------------------------------------------------------------------------------------------------
#
def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print("Click")

"""
The Leftup and Leftdown function will be used when we need to hold down the mouse for a length of time (for dragging, shooting, etc..).
"""
def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print("Left UP")
    
def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print("Left Down")
    
# End of LeftClick, LeftUp, and LeftDown Function -
#
#------------------------------------------------------------------------------------------------------------------------------#------------------------------------------------------------------------------------------------------------------------------
"""

The win32api.mouse_event():
   
    win32api.mouse_event(
            dwflags,'
            dx,
            dy,
            dwdata
    )

-------------------------------------------------------------------------------------------------------------------------------
First Parametre is DWFLAGS :
    
dwflags defines the "action" of the mouse. It controls things such as movement, clicking, scrolling, etc..
The following list shows the most common parameters used while scripting movement.

dwFlags:

    win32con.MOUSEEVENTF_LEFTDOWN
    win32con.MOUSEEVENTF_LEFTUP
    win32con.MOUSEEVENTF_MIDDLEDOWN
    win32con.MOUSEEVENTF_MIDDLEUP
    win32con.MOUSEEVENTF_RIGHTDOWN
    win32con.MOUSEEVENTF_RIGHTUP
    win32con.MOUSEEVENTF_WHEEL

Each name is self explanatory. If you wanted to send a virtual right-click,
you would pass win32con.MOUSEEVENTF_RIGHTDOWN to the dwFlags parameter.

-------------------------------------------------------------------------------------------------------------------------------------------
 
Second parametre is DX and DY :
    
dx and dy, describe the mouse's absolute position along the x and y axis. 
While we could use these parameters for scripting mouse movement, they use a coordinate system different than the one we've been using. 
So, we'll leave them set to zero and rely on a different part of the API for our mouse moving needs.
    
-------------------------------------------------------------------------------------------------------------------------------------------
 
Third parametre is DWDATA :
    
This function is used if (and only if) dwFlags contains MOUSEEVENTF_WHEEL. 
Otherwise is can be omitted or set to zero. dwData specifies the amount of movement on your mouse's scroll wheel.
    
"""

# Function MousePos and Get_Cord -
#
#------------------------------------------------------------------------------------------------------------------------------
#
def mousePos(cord):
    #
    # This function will be used for scripting movement in the program. 
    #
    # Calling SetCursorPos() function sets the mouse to the coordinates passed to it as an x,y tuple. 
    # Notice that we've added in our x and y pads; it's important to do this anywhere a coordinate is called.
    #
    win32api.SetCursorPos((x_pad+cord[0],y_pad+cord[1]))

def get_Cord():
    #
    # This Function prints to the console the current position of the mouse as an x,y tuple.
    #
    x,y=win32api.GetCursorPos()
    x=x-x_pad
    y=y-y_pad
    print(x,y)

# End of MousePos and Get_Cord Function -
#
#-------------------------------------------------------------------------------------------------------------------------------------------

 
# Function StartGame -
#
#-------------------------------------------------------------------------------------------------------------------------------------------
#
def startGame():
    #
    # Location of First menu
    #
    mousePos((-37,45))
    leftClick()
    time.sleep(.1)
    #
    # Location of Second menu
    #
    mousePos((-2,141))
    leftClick()
    time.sleep(.1)
    #
    # Location of Third menu
    #
    mousePos((98,178))
    leftClick()
    time.sleep(.1)
    #
    # Location of Fourth menu
    #
    mousePos((-30,139))
    leftClick()
    time.sleep(.1)
    
# End of StartGame Function -
#
#-------------------------------------------------------------------------------------------------------------------------------------------


# Function Clear_Table -
#
#-------------------------------------------------------------------------------------------------------------------------------------------
#
def clear_Table():
    #
    # Location of First plate
    #
    mousePos((-155,53))
    leftClick()
    #
    # Location of Second plate
    #
    mousePos((-105,50))
    leftClick()
    #
    # Location of Third plate
    #
    mousePos((-48,53))
    leftClick()
    #
    # Location of Fourth plate
    #
    mousePos((-3,53))
    leftClick()
    #
    # Location of Fifth plate
    #
    mousePos((52,53))
    leftClick()
    #
    # Location of Sixth plate
    #
    mousePos((96,52))
    leftClick()
    
# End of Clear_Table Function -
#
#-------------------------------------------------------------------------------------------------------------------------------------------


# Class ShopCords -
#
#-------------------------------------------------------------------------------------------------------------------------------------------
#
class shopCord :
    #
    # ("f_" prefix for food) Co-ordinates of different food in the Menu
    # ("t_" prefix for telephone) Co-ordinates of different food ordering
    #
    f_shrimp=(-160,110)
    f_rice=(-148,115)
    f_nori=(-176,143)
    f_roe=(-146,141)
    f_salmon=(-176,165)
    f_unagi=(-148,171)
    #
    #-----------------------------------------
    #
    # Ordering Food
    #
    phone=(96,130)
    menu_topping=(56,85)
    menu_rice=(68,93)
    menu_sake=(74,106)
    t_exit=(103,119)
    #
    # TOPPING
    #
    t_shrimp=(95,64)
    t_unagi=(90,69)
    t_nori=(55,90)
    t_roe=(97,89)
    t_salmon=(52,115)
    #
    delivery_norm=(53,97)
    order_rice=(75,96)    

# End of FoodCord class -
#
#-------------------------------------------------------------------------------------------------------------------------------------------
#
    
'''
Recipes:
 
    onigiri
        2 rice, 1 nori
     
    caliroll:
        1 rice, 1 nori, 1 roe
         
    gunkan:
        1 rice, 1 nori, 2 roe
        
    dragonroll:
        1 rice, 1 nori, 2 salmon
'''

#Function MakeFood -
#
#-------------------------------------------------------------------------------------------------------------------------------------------
#
def makeFood(food) :
    #
    # Making diiferent foods in this function accrding to Recipe book
    #
    if food=='caliroll' :
        print("MAKING CALIROLL")
        foodOnHand['rice']-=1
        foodOnHand['nori']-=1
        foodOnHand['roe']-=1
        mousePos(shopCord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(shopCord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(shopCord.f_roe)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)
        
    if food=='onigiri' :
        print("MAKING ONIGIRI")
        foodOnHand['rice']-=2
        foodOnHand['nori']-=1
        mousePos(shopCord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(shopCord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(shopCord.f_rice)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)
        
    if food=='gunkan' :
        print("MAKING GUNKAN")
        foodOnHand['rice']-=1
        foodOnHand['nori']-=1
        foodOnHand['roe']-=2
        mousePos(shopCord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(shopCord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(shopCord.f_roe)
        leftClick()
        time.sleep(.05)
        mousePos(shopCord.f_roe)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)
        
    if food=='dragonroll' :
        print("MAKING Salmon Roll")
        foodOnHand['rice']-=1
        foodOnHand['nori']-=1
        foodOnHand['salmon']-=2
        mousePos(shopCord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(shopCord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(shopCord.f_salmon)
        leftClick()
        time.sleep(.05)
        mousePos(shopCord.f_salmon)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)
        
# End of MakeFood Function -
#
#-------------------------------------------------------------------------------------------------------------------------------------------

        
#Function FoldMat-
#
#-------------------------------------------------------------------------------------------------------------------------------------------
#
def foldMat() :
    #
    # Making diferent foods in this function accrding to Recipe book
    #
        print("Folding Mat")
        mousePos((shopCord.f_rice[0]+40,shopCord.f_rice[1]))
        leftClick()
        time.sleep(1)
        
# End of FoldMat Function -
#
#-------------------------------------------------------------------------------------------------------------------------------------------


#Function BuyFood-
#
#-------------------------------------------------------------------------------------------------------------------------------------------
#
def buyFood(food) :
    #
    # Buying diferent foods in this function
    #
    if food =='rice':
        mousePos(shopCord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(shopCord.menu_rice)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        if s.getpixel(shopCord.order_rice)!=(141,168,175):
            print('Rice is available')
            mousePos(shopCord.order_rice)
            time.sleep(1)
            leftClick()
            mousePos(shopCord.delivery_norm)
            time.sleep(1)
            leftClick()
            mousePos(shopCord.t_exit)
            leftClick()
            time.sleep(.5)
            foodOnHand['rice']+=10
            time.sleep(3)
        else:
            print('Rice is NOT available')
            mousePos(shopCord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)
        
    if food =='nori':
        mousePos(shopCord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(shopCord.menu_topping)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        if s.getpixel(shopCord.t_nori)!=(186,219,205):
            print('Nori is available')
            mousePos(shopCord.t_nori)
            time.sleep(1)
            leftClick()
            mousePos(shopCord.delivery_norm)
            time.sleep(1)
            leftClick()
            foodOnHand['nori']+=10
            time.sleep(3)
        else:
            print('Nori is NOT available')
            mousePos(shopCord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)
    
    if food =='roe':
        mousePos(shopCord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(shopCord.menu_topping)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        if s.getpixel(shopCord.t_roe)!=(111,254,101):
            print('Roe is available')
            mousePos(shopCord.t_roe)
            time.sleep(1)
            leftClick()
            mousePos(shopCord.delivery_norm)
            time.sleep(1)
            leftClick()
            foodOnHand['roe']+=10
            time.sleep(3)
        else:
            print('Roe is NOT available')
            mousePos(shopCord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)
            
            
    if food =='salmon':
        mousePos(shopCord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(shopCord.menu_topping)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        if s.getpixel(shopCord.t_salmon)!=(39,32,29):
            print('salmon is available')
            mousePos(shopCord.t_roe)
            time.sleep(1)
            leftClick()
            mousePos(shopCord.delivery_norm)
            time.sleep(1)
            leftClick()
            foodOnHand['salmon']+=5
            time.sleep(3)
        else:
            print('salmon is NOT available')
            mousePos(shopCord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)
            
        
# End of BuyFood Function -
#
#-------------------------------------------------------------------------------------------------------------------------------------------

 
#Function CheckFood-
#
#-------------------------------------------------------------------------------------------------------------------------------------------

def checkFood() :
    #
    # Check and maintain quantity of diferent foods
    #
    for i,j in foodOnHand.items():
        if i=='rice' or i=='roe' or i=='nori' or i=='salmon':
            if j<2:
                print('%s is low in quantity and needs to be replineshed'%i)
                buyFood(i)
    
# End of CheckFood Function -
#
#-------------------------------------------------------------------------------------------------------------------------------------------

 
#Function Get_order -
#
#-------------------------------------------------------------------------------------------------------------------------------------------

def getSeatOne() :
    box=(613, 264,613+25,264+16)
    im=imop.grayscale(imgb.grab(box))
    a=np.array(im.getcolors())
    a=a.sum()
    print(a)
    im.save(os.getcwd()+'\\img_data\\First_seat__'+str(int(time.time()))+'.png', 'PNG')
    return a
    
    

def getSeatTwo() :
    box=(689,264,689+25,264+16)
    im=imop.grayscale(imgb.grab(box))
    a=np.array(im.getcolors())
    a=a.sum()
    print(a)
    im.save(os.getcwd()+'\\img_data\\Second_seat__'+str(time.time())+'.png', 'PNG')
    return a
    
    

def getSeatThree() :
    box=(765,264,765+25,264+16)
    im=imop.grayscale(imgb.grab(box))
    a=np.array(im.getcolors())
    a=a.sum()
    print(a)
    im.save(os.getcwd()+'\\img_data\\Third_seat__'+str(time.time())+'.png', 'PNG')
    return a
    
    
def getSeatFour() :
    box=(841,264,841+25,264+16)
    im=imop.grayscale(imgb.grab(box))
    a=np.array(im.getcolors())
    a=a.sum()
    print(a)
    im.save(os.getcwd()+'\\img_data\\Fourth_seat__'+str(time.time())+'.png', 'PNG')
    return a
    
def getSeatFive() :
    box=(917,264,917+25,264+16)
    im=imop.grayscale(imgb.grab(box))
    a=np.array(im.getcolors())
    a=a.sum()
    print(a)
    im.save(os.getcwd()+'\\img_data\\Fifth_seat__'+str(time.time())+'.png', 'PNG')
    return a
    

def getSeatSix() :
    box=(993,264,993+25,264+16)
    im=imop.grayscale(imgb.grab(box))
    a=np.array(im.getcolors())
    a=a.sum()
    print(a)
    im.save(os.getcwd()+'\\img_data\\Sixth_seat__'+str(time.time())+'.png', 'PNG')
    return a
    
    
def getOrder() :
    getSeatOne() 
    getSeatTwo() 
    getSeatThree() 
    getSeatFour() 
    getSeatFive() 
    getSeatSix() 
    
# End of Get_Order Function -
#
#-------------------------------------------------------------------------------------------------------------------------------------------
      
#Function Check_buds -
#
#-------------------------------------------------------------------------------------------------------------------------------------------
    
def check_buds():
    checkFood()
    s1 = getSeatOne() 
    if s1 != Blank.seat_1:
        if s1 in sushiTypes:
            print('Table 1 is occupied and needs %s' % sushiTypes[s1])
            makeFood(sushiTypes[s1])
        else:
           print('Sushi not found!\n sushiType = %i' % s1)
    else:
        print('Table 1 unoccupied')
    
    checkFood()
    s2 = getSeatTwo() 
    if s2 != Blank.seat_2:
        if s2 in sushiTypes:
            print('Table 2 is occupied and needs %s' % sushiTypes[s2])
            makeFood(sushiTypes[s2])
        else:
           print('Sushi not found!\n sushiType = %i' % s2)
    else:
        print('Table 2 unoccupied')
        
        
    checkFood()
    s3 = getSeatThree() 
    if s3 != Blank.seat_3:
        if s3 in sushiTypes:
            print('Table 3 is occupied and needs %s' % sushiTypes[s3])
            makeFood(sushiTypes[s3])
        else:
           print('Sushi not found!\n sushiType = %i' % s3)
    else:
        print('Table 3 unoccupied')
    
    
    checkFood()
    s4 = getSeatFour() 
    if s4 != Blank.seat_4:
        if s4 in sushiTypes:
            print('Table 4 is occupied and needs %s' % sushiTypes[s4])
            makeFood(sushiTypes[s4])
        else:
           print('Sushi not found!\n sushiType = %i' % s4)
    else:
        print('Table 4 unoccupied')
    
    checkFood()
    s5 = getSeatFive() 
    if s5 != Blank.seat_5:
        if s5 in sushiTypes:
            print('Table 1 is occupied and needs %s' % sushiTypes[s5])
            makeFood(sushiTypes[s5])
        else:
           print('Sushi not found!\n sushiType = %i' % s5)
    else:
        print('Table 6 unoccupied')
        
    clear_Table()
    checkFood()
    s6 = getSeatSix() 
    if s6 != Blank.seat_6:
        if s6 in sushiTypes:
            print('Table 6 is occupied and needs %s' % sushiTypes[s6])
            makeFood(sushiTypes[s6])
        else:
           print('Sushi not found!\n sushiType = %i' % s6)
    else:
        print('Table 6 unoccupied')
    
# End of Check_Buds Function -
#
#------------------------------------------------------------------------------------------------------------------------------    
# Defining Main Function -
#
#------------------------------------------------------------------------------------------------------------------------------
def main():
     startGame()
     while True:
        check_buds()

if __name__=='__main__':
    main()