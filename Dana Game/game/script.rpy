# dress up mini game by dicortesia --> https://www.youtube.com/watch?v=oZU0CmyuZHE&ab_channel=dicortesia

#These variables correspond to the images saved in "images/Minigame". If the variable is 0, the corresponding clothes will have 0 in their filename and so on.
#I set the default to 0, but you can set it to whatever you want.
#We need these variables if you want to keep the outfit you chose for the rest of the game, or if you want to do a reveal at the end of the minigame.
default skirt = 0
default socks = 0
default top = 0

define s = Character("Sweet", who_color="#000000")


#This is where we create a separate screen for each article of clothing, as well as the character base.
#Make sure they're all aligned!
screen sweet_base:
    image "Minigame/sweet_base0.png":
        xpos 0
        ypos 0

screen top0 zorder 2:
    image "Minigame/top_0.png":
        xpos 0
        ypos 0

screen top1 zorder 2:
    image "Minigame/top_1.png":
        xpos 0
        ypos 0

screen top2 zorder 2:
    image "Minigame/top_2.png":
        xpos 0
        ypos 0

screen top3 zorder 2:
    image "Minigame/top_3.png":
        xpos 0
        ypos 0

screen skirt0 zorder 1:
    image "Minigame/skirt_0.png":
        xpos 0
        ypos 0

screen skirt1 zorder 1:
    image "Minigame/skirt_1.png":
        xpos 0
        ypos 0

screen skirt2 zorder 1:
    image "Minigame/skirt_2.png":
        xpos 0
        ypos 0

screen skirt3 zorder 1:
    image "Minigame/skirt_3.png":
        xpos 0
        ypos 0

screen socks0:
    image "Minigame/socks_0.png":
        xpos 0
        ypos 0

screen socks1:
    image "Minigame/socks_1.png":
        xpos 0
        ypos 0

screen socks2:
    image "Minigame/socks_2.png":
        xpos 0
        ypos 0

screen socks3:
    image "Minigame/socks_3.png":
        xpos 0
        ypos 0


#This is where we create the main "functional" screens, making the clothes selection possible.

#Start button
screen outfits:
    image "Minigame/bg.png"
    imagebutton auto "Minigame/start_%s.png" align(0.5, 0.40) action [Show("outfits_ui"), Show("sweet_base"), Show("top0"), Show("skirt0"), Show("socks0")]

#Minigame
screen outfits_ui:
    image "Minigame/bg.png"
    image "Minigame/ui_base.png" align(1.0, 0.0)

    imagebutton auto "Minigame/done_%s.png" align(0.67, 0.0) action Jump("instructions")

#Tops
    imagebutton auto "Minigame/button_top_0_%s.png" align(0.44, 0.25) action [Show("top0"), Hide("top1"), Hide("top2"), Hide("top3"), SetVariable("top", 0)]
    imagebutton auto "Minigame/button_top_1_%s.png" align(0.44, 0.45) action [Show("top1"), Hide("top0"), Hide("top2"), Hide("top3"), SetVariable("top", 1)]
    imagebutton auto "Minigame/button_top_2_%s.png" align(0.44, 0.65) action [Show("top2"), Hide("top1"), Hide("top0"), Hide("top3"), SetVariable("top", 2)]
    imagebutton auto "Minigame/button_top_3_%s.png" align(0.44, 0.85) action [Show("top3"), Hide("top1"), Hide("top2"), Hide("top0"), SetVariable("top", 3)]

#Skirts
    imagebutton auto "Minigame/button_skirt_0_%s.png" align(0.655, 0.25) action [Show("skirt0"), Hide("skirt1"), Hide("skirt2"), Hide("skirt3"), SetVariable("skirt", 0)]
    imagebutton auto "Minigame/button_skirt_1_%s.png" align(0.655, 0.45) action [Show("skirt1"), Hide("skirt0"), Hide("skirt2"), Hide("skirt3"), SetVariable("skirt", 1)]
    imagebutton auto "Minigame/button_skirt_2_%s.png" align(0.655, 0.65) action [Show("skirt2"), Hide("skirt1"), Hide("skirt0"), Hide("skirt3"), SetVariable("skirt", 2)]
    imagebutton auto "Minigame/button_skirt_3_%s.png" align(0.655, 0.85) action [Show("skirt3"), Hide("skirt1"), Hide("skirt2"), Hide("skirt0"), SetVariable("skirt", 3)]

#Socks
    imagebutton auto "Minigame/button_socks_0_%s.png" align(0.875, 0.25) action [Show("socks0"), Hide("socks1"), Hide("socks2"), Hide("socks3"), SetVariable("socks", 0)]
    imagebutton auto "Minigame/button_socks_1_%s.png" align(0.875, 0.45) action [Show("socks1"), Hide("socks0"), Hide("socks2"), Hide("socks3"), SetVariable("socks", 1)]
    imagebutton auto "Minigame/button_socks_2_%s.png" align(0.875, 0.65) action [Show("socks2"), Hide("socks1"), Hide("socks0"), Hide("socks3"), SetVariable("socks", 2)]
    imagebutton auto "Minigame/button_socks_3_%s.png" align(0.875, 0.85) action [Show("socks3"), Hide("socks1"), Hide("socks2"), Hide("socks0"), SetVariable("socks", 3)]


#This image can be used for the rest of the game, or just as a final reveal.
#If this looks confusing, you can check out the video tutorial I made, or look into layered images.
layeredimage sweet:
    always:
        "Minigame/sweet_base.png"

    group face:
        attribute face1 default:
            "Minigame/sweet_face1.png"
        attribute face2:
            "Minigame/sweet_face2.png"
        attribute face3:
            "Minigame/sweet_face3.png"
        attribute face4:
            "Minigame/sweet_face4.png"

    group top:
        attribute 0 default:
            "Minigame/top_0.png"
    if top == 0:
        "Minigame/top_0.png"
    if top == 1:
        "Minigame/top_1.png"
    if top == 2:
        "Minigame/top_2.png"
    if top == 3:
        "Minigame/top_3.png"

    group skirt:
        attribute 0 default:
            "Minigame/skirt_0.png"
    if skirt == 0:
        "Minigame/skirt_0.png"
    if skirt == 1:
        "Minigame/skirt_1.png"
    if skirt == 2:
        "Minigame/skirt_2.png"
    if skirt == 3:
        "Minigame/skirt_3.png"

    group socks:
        attribute 0 default:
            "Minigame/socks_0.png"
    if socks == 0:
        "Minigame/socks_0.png"
    if socks == 1:
        "Minigame/socks_1.png"
    if socks == 2:
        "Minigame/socks_2.png"
    if socks == 3:
        "Minigame/socks_3.png"

label start:
    call screen outfits

    label instructions:
        scene bg with dissolve

        hide screen outfits
        hide screen outfits_ui

        hide screen sweet_base

        hide screen top0
        hide screen top1
        hide screen top2
        hide screen top3

        hide screen skirt0
        hide screen skirt1
        hide screen skirt2
        hide screen skirt3

        hide screen socks0
        hide screen socks1
        hide screen socks2
        hide screen socks3

        show sweet:
            xpos 0.35
            ypos 0

        s "Hi!"
        s "Thank you for trying this minigame!"

        show sweet face3

        s "Please take a look at the game files, script, and video tutorial to understand how it works!"

        show sweet face1

        s "Have fun making your game!"

        return
