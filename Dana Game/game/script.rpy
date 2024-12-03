###############################################################
######################### Text Sound ##########################
###############################################################

# code by Aquapaulo --> https://github.com/aquapaulo/renpy-typewriter-sounds

##regular taps, medium intervals
define sounds = ['audio/A1.ogg', 'audio/A2.ogg', 'audio/A3.ogg', 'audio/A4.ogg', 'audio/A5.ogg']

init python:
    def type_sound(event, interact=True, **kwargs):
        if not interact:
            return

#if text's being written by character, spam typing sounds until the text ends
        if event == "show":
            renpy.sound.play(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            #dumb way to do it but it works, dunno if it causes memory leaks but it's almost 6AM :v (from Aquapaulo)



        elif event == "slow_done" or event == "end":
            renpy.sound.stop()

###############################################################
######################### Dress Up ############################
###############################################################

# dress up mini game by dicortesia --> https://www.youtube.com/watch?v=oZU0CmyuZHE&ab_channel=dicortesia

#These variables correspond to the images saved in "images/Minigame". If the variable is 0, the corresponding clothes will have 0 in their filename and so on.
#I set the default to 0, but you can set it to whatever you want.
#We need these variables if you want to keep the outfit you chose for the rest of the game, or if you want to do a reveal at the end of the minigame.
default bottom = 0
default socks = 0
default top = 0

define d = Character("Dana", who_color="#FF0000", callback=type_sound)
define v = Character("Virginia", who_color="#0000FF", callback=type_sound)
define c = Character("Charon", callback=type_sound)
define e = Character("Cleo", callback=type_sound)

image Virginia = "Virginia.png"
image Charon = "Charon.png"
image Cleo = "Cleo.png"


#This is where we create a separate screen for each article of clothing, as well as the character base. Make sure they're all aligned!
screen Dana_Sprite:
    image "Dana_Imgs/Dana_Sprite.png":
        xpos 300
        ypos 0

screen top0 zorder 2:
    image "Dana_Imgs/Dana_Top_1.png":
        xpos 300
        ypos 0

screen top1 zorder 2:
    image "Dana_Imgs/Dana_Top_2.png":
        xpos 300
        ypos 0

screen bottom0 zorder 1:
    image "Dana_Imgs/Dana_Bottom_1.png":
        xpos 300
        ypos 0

screen bottom1 zorder 1:
    image "Dana_Imgs/Dana_Bottom_2.png":
        xpos 300
        ypos 0


#Dress up menu screen
#Start button
screen outfits:
    image "Minigame/bg.png"
    imagebutton auto "Minigame/start_%s.png" align(0.5, 0.40) action [Show("outfits_ui"), Show("Dana_Sprite"), Show("top0"), Show("bottom0")]

#Minigame
screen outfits_ui:
    image "Minigame/bg.png"
    image "Minigame/ui_base.png" align(1.0, 0.0)

    imagebutton auto "Minigame/done_%s.png" align(0.80, 0.75) action Jump("instructions")

#Tops
    imagebutton auto "Dana_Imgs/Dana_Top_1_%s.png" align(0.655, 0.25) action [Show("top0"), Hide("top1"), SetVariable("top", 0)]
    imagebutton auto "Dana_Imgs/Dana_Top_2_%s.png" align(0.655, 0.45) action [Show("top1"), Hide("top0"), SetVariable("top", 1)]

#Bottoms
    imagebutton auto "Dana_Imgs/Dana_Bottom_1_%s.png" align(0.755, 0.25) action [Show("bottom0"), Hide("bottom1"),SetVariable("bottom", 0)]
    imagebutton auto "Dana_Imgs/Dana_Bottom_2_%s.png" align(0.755, 0.45) action [Show("bottom1"), Hide("bottom0"), SetVariable("bottom", 1)]


#This image can be used for the rest of the game, or just as a final reveal.
layeredimage Dana_N:
    always:
        "Dana_Imgs/Dana_Sprite.png"

    group top:
        attribute 0 default:
            "Dana_Imgs/Dana_Top_1.png"
    if top == 1:
        "Dana_Imgs/Dana_Top_2.png"

    group bottom:
        attribute 0 default:
            "Dana_Imgs/Dana_Bottom_1.png"
    if bottom == 1:
        "Dana_Imgs/Dana_Bottom_2.png"

###############################################################
######################### Gameplay ############################
###############################################################
label start:
        with fade
        scene black bg
        d "Dinner is going to be at Satanya's place tonight..."

        d "Hmm...What should I wear?"

        jump dress

label dress:
    call screen outfits

    label instructions:
        scene bg with dissolve

        hide screen outfits
        hide screen outfits_ui

        hide screen Dana_Sprite

        hide screen top0
        hide screen top1

        hide screen bottom0
        hide screen bottom1

        show Dana_N:
            xpos 0.38
            ypos 0
        
        "Looking good! Now lets start the game!"

        jump story

label story:
    scene black bg
    hide bg
    hide Dana_N
    with fade

    "Dana, along with her friend Virginia, are invited to an extravagant dinner party hosted by the one and only Satanya."

    "This dinner party would be unlike anything anyone had ever seen before, and to be invited meant that you were worthy of Satanya’s presence…"

    scene road bg
    with dissolve
    "As Dana drives to the dinner party, she feels her car shaking as she drives. The engine takes its last breath…"

    show Dana_N
    with dissolve

    d "No…No!!!"

    d "Damn it! I should’ve just stolen my dads car!"

    "Dana leaves her car and finds herself in the middle of an empty road. She gets a phone call…"

    d "Hello?"

    v "Hey queen! Your ex called me and said you haven’t arrived at the party yet. Is everything ok?"

    d "My ex called you!? Why the hell did he get invited…"

    d "Anyway, my car just broke down and I’m in the middle of nowhere…"

    scene black bg
    with dissolve
    v "Send me your location. I'll be there soon."

    "Dana sends Virginia her location. Thirty minutes pass and you find Virginia’s car driving towards you."

    scene road bg
    with fade

    show Dana_N:
        xpos 300
        ypos 0

    d "Took you long enough!"

    show Virginia:
        xpos 1000
        ypos 0

    v "Sorry queen, lots of traffic today…"

    v "Anyway, I know a shortcut! But we would have to go through a creepy forest…"

    d "No way! I’m not trying to get eaten by Cerberus’s babies!"

    v "But there’s this really cool mall on the way, I heard they sell all of the luxury stuff at cheap prices! Maybe we can shop for a better outfit over there?"
    
    v "After all, that outfit you're wearing was so last season…"
    if top == 0:
        v "Like— girl you look like an inflamed pimple."
    elif top == 1:
        v "Purple? Seriously? Do you remember what your color consultant said?"
        v "Its so not your color..."

    d "Ugh! You—! Fine whatever, but my outfit is still in style…"

    show trees bg
    with fade

    "Dana and Virginia arrive at the creepy forest. The trees are devoid of life, and have faces carved into them."

    v "Talk about déjà vu... have I been here before?"
    
    show Virginia:
        xpos 1000
        ypos 0

    "As Dana and Virginia traverse through the creepy forest, they find lights in the distance."

    show mall bg
    with dissolve

    d "Hey look! Is that the mall? It looks huge!"

    d "This doesn’t look like any mall I’ve ever been to, and I’ve been to thousands of malls…"

    v "Thousands of malls!? And yet you dress like that?"

    d "Oh come on! I was in a rush!"

    show black bg
    with fade

    show river bg
    with dissolve

    "A few minutes pass, Dana and Virginia arrive in front of the strange mall. However, there is a river that leads towards the mall."

    "In front of the mall lies a tall figure. An old man with a boat."

    show charon cg
    with fade

    c "Ladies…It appears that you are lost. I suggest you turn back now before it’s too late… "

    d "We want to go inside that mall."

    c "I’m afraid I can’t let you pass. This mall is only for those who have died without forgiveness from their sins."

    hide charon cg
    with dissolve
    show river bg

    d "What? But it’s just a shopping mall…what's with the exclusivity?"

    v "…We were invited by Satanya to attend her dinner party. We just came here to shop for a better outfit."

    show Charon

    c "Satanya!? May I see your invitation…"

    "Dana and Virginia show the old man their invitations as proof."

    c "Well why didn’t you just say so! Please have a seat on my boat, I’ll take you to the entrance."

    c "But please be warned, this isn’t just your ordinary shopping mall…"

    "Dana and Virginia enter the man’s boat. As they slowly approach the mall, they hear the cries of the sinners echoing throughout the mall…"

    "The entrance of the mall says…"

    hide river bg
    hide Charon
    show black bg
    with fade

    "“Abandon all hope, ye who enter here.”"

    hide black bg
    show mall bg
    with fade

    d "Jeez, what a creepy mall…no wonder everything is half-off…"
    
    show Dana_N

    v "Lets just find an outfit and go…"

    hide Dana_N
    show Virginia

    hide Dana_N
    hide Virginia
    with dissolve

    "Dana and Virginia leave the boat and enter the mall…"

    show Charon

    c "Hey! You forgot to tip!"

    show black bg
    with fade
    show shop bg
    with dissolve

    "The mall appears to have nine floors, each floor representing a sin…"

    show Dana_N

    d "Wow! This mall is huge! We’re gonna need a map…"

    hide Dana_N
    show Virginia

    v "Over there!"

    hide Virginia
    with dissolve

    "Dana and Virginia find the map of the mall. A clothing store catches their eye…"

    "“Lucie’s Boutique”"

    show Dana_N

    d "I’ve heard of this store, they have this beautiful red dress that's being sold in very limited quantities!"

    hide Dana_N
    show Virginia

    v "Looks like that store is on the ninth floor…We should hurry."

    hide Virginia
    show Dana_N

    d "Why are you in such a rush? The dinner party doesn’t officially start til midnight, and it’s only 9pm."

    hide Dana_N
    show Virginia

    v "It’s nothing…This place just gives me the creeps."

    v "Let's go."

    hide shop bg
    hide Dana_N
    hide Virginia
    show black bg
    with fade

    "Dana and Virginia take the escalator. They notice a bunch of people fawning over an image of a model wearing a clothing brand's latest collection, all while being swept away by an imaginary wind."

    show Dana_N

    d "What's up with those guys?"

    hide Dana_N
    show Virginia

    v "It looks like this floor is reserved to those who are lustful…"

    "Suddenly, Virginia finds a familiar face in the distance."
    
    "Her arch nemesis… {b}Cleo{/b}."

    v "Oh no…not her…"

    hide Virginia
    show Dana_N

    d "What's wrong? Who is that?"

    hide Dana_N
    show Virginia

    v "That's Cleo, my former best friend."

    v "I…um…"

    hide Virginia
    show Dana_N

    d "Come on! Spill the tea!"

    hide Dana_N
    show Virginia

    v "I…borrowed her beloved lip gloss once… never gave it back."

    hide Virginia
    show Dana_N

    d "Seriously? That's it?"

    hide Dana_N
    show Cleo

    e "Well, well, well, look what the roaches dragged in…"

    e "What's with the outfits? Did your grandma dress you?"

    hide Cleo
    show Dana_N

    d "Excuse me…"

    d "Have you looked in the mirror lately? It looks like a toddler cut your hair blindfolded…miss bob."

    hide Dana_N
    show Cleo

    e "Hey! Bob cuts are the new thing!"

    hide Cleo
    show Virginia

    v "Whatever helps you sleep at night…"

    hide Virginia
    with fade

    "End of prototype"
    "Thank you for playing!"

    with fade

    return
