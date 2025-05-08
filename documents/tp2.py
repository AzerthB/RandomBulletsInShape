import math

# Function to initialize global variables and default settings
def init():
    global shape
    global nbBullets
    global widthBullets
    global scale
    global bulletsPositionsList
    global taille

    widthBullets = 7
    nbBullets = 10
    scale = 10.0
    taille = 70
    bulletsPositionsList = ''
    shape = 'circle'
    refresh()
    return

# Function to refresh the elements on the page
def refresh():
    global bulletsPositionsList

    bulletsPositionsList = ''
    root           = document.querySelector("#cb-body") 
    root.innerHTML = html()

# Function to apply the html and css of the page
def html():
    global shape
    global nbBullets
    global widthBullets
    global scale
    global bulletsPositionsList
    global taille

    css = ("""
    body { width: 100%; height:100%; max-width: 95%; margin: auto; }
    .title {
        position: absolute;
        top: 1%;
        left: 1%;
    }
    .parameters {
        position: absolute;
        bottom: 1%;
        left: 1%;
    }
    .positions {
        position: absolute;
        top: 1%;
        right: 1%;
        text-align: right;
    }
    .scroll {
        margin: 4px, 4px;
        padding: 4px;
        background-color: transparent;
        width: 30vh;
        height: 95vh;
        overflow-x: hidden;
        overflow-y: auto;
        text-align: right;
        font-family: "Arial", Arial, monospace;
    }
    .bold {
        font-weight: bold;
    }
    .transparent {
        background-color: transparent;
        border-color: transparent;
    }
    .scale {
        height: 3px;
        width: """+ str(taille) +"""vh;
        background-color: #333;
        margin: auto;
        position: relative;
        align-items: left;
    }
    .circle {
        height: """+ str(taille) +"""vh;
        width: """+ str(taille) +"""vh;
        background-color: #333;
        border-radius: 50%;
        margin: auto;
        position: relative;
        z-index: -1;
    }
    .oval {
        height: """+ str(taille) +"""vh;
        width: """+ str(taille * 2) +"""vh;
        background-color: #333;
        border-radius: 50%;
        margin: auto;
        position: relative;
        z-index: -1;
    }
    .square {
        height: """+ str(taille) +"""vh;
        width: """+ str(taille) +"""vh;
        background-color: #333;
        margin: auto;
        position: relative;
        z-index: -1;
    }
    .rectangle {
        height: """+ str(taille) +"""vh;
        width: """+ str(taille * 2) +"""vh;
        background-color: #333;
        margin: auto;
        position: relative;
        z-index: -1;
    }
    .silhouette {
        height: """+ str(taille) +"""vh;
        width: """+ str(taille//2) +"""vh;
        background-color: #333;
        margin: auto;
        position: relative;
        z-index: -1;
    }
    .silhouetteHead {
        height: """+ str(taille/6) +"""vh;
        width: """+ str(taille/6) +"""vh;
        background: rgba(256, 256, 256, 0.3); 
        border-radius: 30%;
        margin: auto;
        position: absolute;                  
        top:  """+ str(taille/8) +"""vh;         
        left: """+ str(taille/6) +"""vh; 
        z-index: -1;
    }
    .silhouetteBody {
        height: """+ str(taille/3.5) +"""vh;
        width: """+ str(taille/6) +"""vh;
        background: rgba(256, 256, 256, 0.3); 
        border-radius: 2%;
        margin: auto;
        position: absolute;                  
        top:  """+ str(taille/3.2) +"""vh;         
        left: """+ str(taille/6) +"""vh; 
        z-index: -1;
    }
    .silhouetteArm1 {
        height: """+ str(taille/3.5) +"""vh;
        width: """+ str(taille/14) +"""vh;
        background: rgba(256, 256, 256, 0.3); 
        border-radius: 2%;
        margin: auto;
        position: absolute;                  
        top:  """+ str(taille/3.2) +"""vh;         
        left: """+ str(taille/13.5) +"""vh; 
        z-index: -1;
    }
    .silhouetteArm2 {
        height: """+ str(taille/3.5) +"""vh;
        width: """+ str(taille/14) +"""vh;
        background: rgba(256, 256, 256, 0.3); 
        border-radius: 2%;
        margin: auto;
        position: absolute;                  
        top:  """+ str(taille/3.2) +"""vh;         
        left: """+ str(taille/2.819) +"""vh; 
        z-index: -1;
    }
    .silhouetteLeg1 {
        height: """+ str(taille/3.5) +"""vh;
        width: """+ str(taille/14) +"""vh;
        background: rgba(256, 256, 256, 0.3); 
        border-radius: 2%;
        margin: auto;
        position: absolute;                  
        top:  """+ str((taille/3.2) + (taille/3.3)) +"""vh;         
        left: """+ str(taille/16+ taille/9.5) +"""vh; 
        z-index: -1;
    }
    .silhouetteLeg2 {
        height: """+ str(taille/3.5) +"""vh;
        width: """+ str(taille/14) +"""vh;
        background: rgba(256, 256, 256, 0.3); 
        border-radius: 2%;
        margin: auto;
        position: absolute;                  
        top:  """+ str((taille/3.2) + (taille/3.3)) +"""vh;         
        left: """+ str(taille/6.5+ taille/9.2) +"""vh; 
        z-index: -1;
    }
    """+ bulletsCSS() +"""
    """)

    html = ("""
    
    <style>
    """ + css + """
    </style>
    <body>
        <div class="title">
            <div class="bold">
                Random Bullets in Shapes V2.3
            </div>
            <div>
                by Éloi Bonneville
            </div>
            <table>
                """+ str(taille) + " %" +"""
                <button class="transparent" onclick="chooseZoom('remove10');   refresh();">--</button>
                <button class="transparent" onclick="chooseZoom('remove');     refresh();">-</button>
                <button class="transparent" onclick="chooseZoom('add');        refresh();">+</button>
                <button class="transparent" onclick="chooseZoom('add10');      refresh();">++</button>
            </table>
        </div>

        <p></p>
        <div class=" """+ shape +""" " id=" """+ shape +""" ">
            """+ silhouetteHTML() +"""
            <div class="scaleY"></div>
            """+ bulletsHTML() +"""
        </div>
        <div class="scale">
            """+ str(scale) +"""
            <button class="transparent" onclick="chooseScale('remove10');    refresh();">--</button>
            <button class="transparent" onclick="chooseScale('remove');      refresh();">-</button>
            <button class="transparent" onclick="chooseScale('add');         refresh();">+</button>
            <button class="transparent" onclick="chooseScale('add10');       refresh();">++</button>
        </div>
        <div class="positions">
            <div class="bold">
                Positions of Projectiles:
            </div>
            <div class="scroll">
                """+ str(bulletsPositionsList) +"""
            </div>
        </div>
        <div class="parameters">
            <table> 
                <div class="bold">
                    Number of Projectiles : 
                </div>
            </table>
            <table>
                &nbsp
                """+ str(nbBullets) +"""
                <button class="transparent" onclick="chooseBullets('remove10');  refresh();">--</button>
                <button class="transparent" onclick="chooseBullets('remove');    refresh();">-</button>
                <button class="transparent" onclick="chooseBullets('add');       refresh();">+</button>
                <button class="transparent" onclick="chooseBullets('add10');     refresh();">++</button>
            </table>
            <table> 
                <div class="bold">
                    Diameter of Projectiles :
                </div>
            </table>
            <table>
                &nbsp
                """+ str((int(10 * (widthBullets/taille) * scale))/10) + """
                <button class="transparent" onclick="chooseBulletWidth('remove10');  refresh();">--</button>
                <button class="transparent" onclick="chooseBulletWidth('remove');    refresh();">-</button>
                <button class="transparent" onclick="chooseBulletWidth('add');       refresh();">+</button>
                <button class="transparent" onclick="chooseBulletWidth('add10');     refresh();">++</button>
            </table>
            <table>
                <div class="bold">
                    Shape :
                </div>
            </table>
            <table>
                <button class="transparent" onclick="shapes('circle');    refresh();">Circle</button>
                <button class="transparent" onclick="shapes('oval');      refresh();">Oval</button>
                <button class="transparent" onclick="shapes('square');    refresh();">Square</button>
                <button class="transparent" onclick="shapes('rectangle'); refresh();">Rectancle</button>
                <button class="transparent" onclick="shapes('silhouette'); refresh();">Silhouette</button>
            </table>
        </div>
    </body>
    """)
   
    return html

# Function to control the number of bullets present on the page
def chooseBullets(operation):
    global nbBullets

    if   operation == 'add':
         nbBullets += 1
    elif operation == 'remove' and nbBullets >= 1:
         nbBullets -= 1
    elif operation == 'add10':
         nbBullets += 10
    elif operation == 'remove10' and nbBullets >= 10:
         nbBullets -= 10

# Function to control the width of each bullets
def chooseBulletWidth(operation):
    global widthBullets
    global scale
    global taille

    if   operation == 'add':
         widthBullets += int(taille / scale)/10
    elif operation == 'remove' and widthBullets >= int(taille / scale)/10:
         widthBullets -= int(taille / scale)/10
    elif operation == 'add10':
         widthBullets += int(taille / scale)
    elif operation == 'remove10' and widthBullets >= int(taille / scale):
         widthBullets -= int(taille / scale)

# Function to control the bottom scale on the page to adjust the calculations of every position
def chooseScale(operation):
    global scale

    scale = int(scale * 10)

    if   operation == 'add':
         scale += 1
    elif operation == 'remove' and scale >= 2:
         scale -= 1
    elif   operation == 'add10':
         scale += 10
    elif operation == 'remove10' and scale >= 11:
         scale -= 10
    
    scale = scale / 10


# Function to control the zoom of the tabletop section
def chooseZoom(operation):
    global taille
    global widthBullets

    if   operation == 'add':
         taille += 1
    elif operation == 'remove' and taille >= 1:
         taille -= 1
    elif operation == 'add10':
         taille += 10
    elif operation == 'remove10' and taille >= 10:
         taille -= 10
    
# Function to choose the shape of the battlefield
def shapes(chosenShape):
    global shape

    shape = chosenShape
    return shape

# Function to create the html of the bullets depending on the number of bullets
def bulletsHTML():
    global nbBullets

    bulletsHTML = ''
    for i in range(nbBullets):
        bulletsHTML += '<div class="bullet' + str(i) + '"></div>'
    return bulletsHTML

# Function to create the css of the bullets depending on the number of bullets and their width
def bulletsCSS():
    global nbBullets
    global widthBullets
    
    bulletsCSS = ''
    for i in range(nbBullets):
        position = placeProjectile()
        bulletsCSS += ('                      \
    .bullet' + str(i) + ' {                   \
        height:  ' + str(widthBullets) + 'vh; \
        width:   ' + str(widthBullets) + 'vh; \
        background: rgba(256, 0, 0, 0.5);     \
        border-radius: 50%;                   \
        position: absolute;                   \
        top:  ' + position[1] + 'vh;          \
        left: ' + position[0] + 'vh;          \
    }                                         \
    ')
    return bulletsCSS

# Function to return the silhouette shape instead of default battlefield shapes
def silhouetteHTML():
    global shape
    silhouette = """<div class="silhouetteHead"></div>
                    <div class="silhouetteBody"></div>
                    <div class="silhouetteArm1"></div>
                    <div class="silhouetteArm2"></div>
                    <div class="silhouetteLeg1"></div>
                    <div class="silhouetteLeg2"></div> """

    if shape == 'silhouette':
        return silhouette
    else:
        return ''

# Function to calculate the position of the bullets depending on the selected scale
def bulletsPositions(coordinates):
    global scale
    global bulletsPositionsList
    global widthBullets
    global taille

    x = coordinates[0]
    y = coordinates[1]

    scale = int(scale * 10)
    x = (x + (widthBullets//2)) * scale//taille
    y = (taille - y - (widthBullets//2)) * scale//taille
    scale /= 10

    x /= 10
    y /= 10

    bulletsPositionsList += "<div>[" + str(x) + "; " + str(y) + "]</div>"

# Function to randomly place every projectile depending on the battlefield shape and bullets caracteristics
def placeProjectile():
    global shape
    global widthBullets
    global bulletsPositionsList
    global taille

    if shape    == 'circle':
        radius = (taille//2) * random()
        if radius < taille/8:
            check = random() * 0.7
            radius   = (taille//2) * ((0.8 * random()) + 0.2) if check < 0.5 else radius
        angle    = 2 * math.pi * random()
        x        = int( radius * math.cos(angle) ) + (taille//2) - widthBullets//2
        y        = int( radius * math.sin(angle) ) + (taille//2) - widthBullets//2
        bulletsPositions([x, y])
        position = [str(x), str(y)]
        return position
    elif shape  == 'oval':
        a        = taille
        b        = (taille//2)
        angle    = 2 * math.pi * random()
        if (angle > math.pi/4 and angle < (math.pi * 3)/4) or (angle > (math.pi * 5)/4 and angle < (math.pi * 7)/4):
            check = random()
            angle = (2 * math.pi * random()) if check > 0.5 else angle
        radius   = math.sqrt(( a**2 * b**2 ) / ( a**2 * math.sin(angle)**2 + b**2 * math.cos(angle)**2 ))
        rand = 0
        while rand < 0.2:
            rand = random()
        radius   = radius * rand
        x        = int( radius * math.cos(angle) ) + taille - widthBullets//2
        y        = int( radius * math.sin(angle) ) + (taille//2) - widthBullets//2
        bulletsPositions([x - (taille//2), y])
        position = [str(x), str(y)]
        return position
    elif shape  == 'square':
        x        = int( taille * random() ) - widthBullets//2
        y        = int( taille * random() ) - widthBullets//2
        bulletsPositions([x, y])
        position = [str(x), str(y)]
        return position
    elif shape  == 'rectangle':
        x        = int( (taille * 2) * random() ) - widthBullets//2
        y        = int( taille  * random() ) - widthBullets//2
        bulletsPositions([x - (taille//2), y])
        position = [str(x), str(y)]
        return position
    elif shape == 'silhouette':
        x        = int( (((taille//2) * random() ) - widthBullets//2))
        y        = int( taille * random() ) - widthBullets//2
        bulletsPositions([x + (taille//4), y])
        position = [str(x), str(y)]
        return position