######
#
# NOTES: 
# obstacles that are walkable get names "defaultWall#"
# obstacles that are killable get names angryBoxes
#
#
#
#####
app.stepsPerSecond = 60 #physics updates per second kind of
global vsp
global hsp
global jumps
global room
global gravity
room = 1
vsp = 0
hsp = 0
jumps = 0
gravity = 0.08
##### draw obstacles here
defaultWall3 = Rect(150,250,50,50,fill='gray')
defaultWall2 = Rect(200,200,100,100,fill='gray')
defaultWall = Rect(300,300,50,50,fill='gray')

angryWall = Rect(300,100,25,25,fill='red')

winWall = Rect(325,125,25,25,fill='yellow')

playerBox = Rect(100,100,25,25) # player, do not edit
#playerBox = Image("cmu://578926/20839210/beauty.png", 100,100)
#####

def onStep():
    global vsp
    global hsp
    global jumps
    global gravity
    global room
    vsp += gravity #gravity
    hsp = hsp*0.92 #friction
    #####   mark collision boxes here 
    if room == 1:
        
        collisionCheck(defaultWall)
        collisionCheck(defaultWall2)
        collisionCheck(defaultWall3)
        deathCheck(angryWall)
        winCheck(winWall)
    if room == 2:
        defaultWall.visible=False
        defaultWall2.visible=False
        defaultWall3.visible=False
        angryWall.visible=False
        winWall.visible=False
    #####
    

    
    playerBox.left +=hsp
    playerBox.bottom +=vsp
    if playerBox.bottom>=399:
        jumps = 1    
    if playerBox.left <=0:
        playerBox.left = 0
    if playerBox.right >=400:
        playerBox.right = 400
    
    if playerBox.bottom >= 400-vsp:
        if not distance(0,playerBox.bottom,0,defaultWall.top) < 0.5:
            vsp = -gravity
    
    if hsp<-8:
        hsp = -8
    if hsp>8:
        hsp = 8
        
def onKeyHold(keys):
    global jumps
    global hsp
    global vsp
    if "d" in keys:
        
        hsp+=0.8
    if "a" in keys:
        
        hsp-=0.8
    if "w" in keys:
        if jumps == 1:
            vsp=-5
            jumps = 0
            
            
def legacyCollisionCheck():
    global jumps
    global vsp
    global hsp
    
    if distance(playerBox.left,0,defaultWall.right,0) <abs(hsp):#meeting on left side of player
        if playerBox.bottom>300:
            if playerBox.top<350:
                if hsp < 0:
                    hsp = 0
                
    if distance(playerBox.right,0,defaultWall.left,0) <abs(hsp):#meeting on right side of player
        if playerBox.bottom>300:
            if playerBox.top<350:
                if hsp > 0:
                    hsp = 0
                
    if distance(0,playerBox.top,0,defaultWall.bottom) <abs(vsp): #meeting on top of player
        if playerBox.right>300:
            if playerBox.left<350:
                 vsp = 0
                
    if distance(0,playerBox.bottom,0,defaultWall.top) <abs(vsp): #meeting on bottom of player
        if playerBox.right>300:
            if playerBox.left<350:
                vsp = -0.1
                jumps = 1
                
                
def collisionCheck(box):
    global jumps
    global vsp
    global hsp
    #lefts V
    if (box.contains(playerBox.left+hsp,playerBox.top) == True):
        if hsp < 0.1:
            hsp = 0.05
            
    if (box.contains(playerBox.left+hsp,playerBox.bottom-2) == True):
        if hsp < 0.1:
            hsp = 0.05
    #rights V
    if (box.contains(playerBox.right+hsp,playerBox.top) == True):
        if hsp > 0.1:
            hsp = -0.05
            
    if (box.contains(playerBox.right+hsp,playerBox.bottom-2) == True):
        if hsp > 0.1:
            hsp = -0.05
    #tops V    
    if (box.contains(playerBox.left,playerBox.top+vsp) == True):
        if vsp < 0: 
            vsp = 1.6
    
    if (box.contains(playerBox.right,playerBox.top+vsp) == True):
        if vsp < 0: 
            vsp = 1.6
    #bottoms V
    if (box.contains(playerBox.left,playerBox.bottom+vsp) == True):
        if vsp > 0: 
            vsp = -0.1
            jumps = 1
    
    if (box.contains(playerBox.right,playerBox.bottom+vsp) == True):
        if vsp > 0: 
            vsp = -0.1
            jumps = 1
    
def deathCheck(angrybox):

    if (angrybox.contains(playerBox.left,playerBox.top) == True):
        playerBox.top = 100
        playerBox.left= 100
        vsp = 0
        hsp = 0
    if (angrybox.contains(playerBox.right,playerBox.top) == True):
        playerBox.top = 100
        playerBox.left= 100
        vsp = 0
        hsp = 0
    if (angrybox.contains(playerBox.left,playerBox.bottom) == True):
        playerBox.top = 100
        playerBox.left= 100
        vsp = 0
        hsp = 0
    if (angrybox.contains(playerBox.right,playerBox.bottom) == True):
        playerBox.top = 100
        playerBox.left= 100
        vsp = 0
        hsp = 0
    
def winCheck(coolbox):
    
    global room
    
    if (coolbox.contains(playerBox.left,playerBox.top) == True):
        playerBox.top = 100
        playerBox.left= 100
        room+=1
        
    if (coolbox.contains(playerBox.right,playerBox.top) == True):
        playerBox.top = 100
        playerBox.left= 100
        room+=1
        
    if (coolbox.contains(playerBox.left,playerBox.bottom) == True):
        playerBox.top = 100
        playerBox.left= 100
        room+=1
        
    if (coolbox.contains(playerBox.right,playerBox.bottom) == True):
        playerBox.top = 100
        playerBox.left= 100
        room+=1
    
    
