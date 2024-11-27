# character customization tutorial: https://www.youtube.com/watch?v=6pNWrjbDwIU&ab_channel=__ess__Ren%27PyTutorials
# assets by __ess__ Ren'Py Tutorials



# check if items will be selected, switched, and then returned
init python:
    def customize_character(type, direction):
        global skin_color
        global hair_color
        global eye_color
        global shirt_color

        if direction == "right":
            # check skin
            if type == "skin":
                if skin_colors.index(skin_color) < len(skin_colors) - 1:
                    skin_color = skin_colors[skin_colors.index(skin_color) + 1]
            else:
                skin_color = skin_colors[0]
            # check hair
            if type == "hair":
                if hair_colors.index(hair_color) < len(hair_colors) - 1:
                    hair_color = hair_colors[hair_colors.index(hair_color) + 1]
            else:
                hair_color = hair_colors[0]
            # check eyes
            if type == "eyes":
                if eye_colors.index(eye_color) < len(eye_colors) - 1:
                    eye_color = eye_colors[eye_colors.index(eye_color) + 1]
            else:
                eye_color = eye_colors[0]
            # check shirt
            if type == "shirt":
                if shirt_colors.index(shirt_color) < len(shirt_colors) - 1:
                    shirt_color = shirt_colors[shirt_colors.index(shirt_color) + 1]
            else:
                shirt_color = shirt_colors[0]

        elif direction == "left":
            # check skin
            if type == "skin":
                if skin_colors.index(skin_color) > 0:
                    skin_color = skin_colors[skin_colors.index(skin_color) - 1]
            else:
                skin_color = skin_colors[-1]
            # check hair
            if type == "hair":
                if hair_colors.index(hair_color) > 0:
                    hair_color = hair_colors[hair_colors.index(hair_color) - 1]
            else:
                hair_color = hair_colors[-1]
            # check eyes
            if type == "eyes":
                if eye_colors.index(eye_color) > 0:
                    eye_color = eye_colors[eye_colors.index(eye_color) - 1]
            else:
                eye_color = eye_colors[-1]
            # check shirt
            if type == "shirt":
                if shirt_colors.index(shirt_color) > 0:
                    shirt_color = shirt_colors[shirt_colors.index(shirt_color) - 1]
            else:
                shirt_color = shirt_colors[-1]
        
    #renpy.retain_after_load()


# player alignment
image character = Composite(
    (846, 1028),
    (0, 0), "Character/hair-long-[hair_color]-back.png",
    (0, 0), "Character/body-skin-[skin_color].png",
    (0, 0), "Character/eyecolor-[eye_color].png",
    (0, 0), "Character/shirt-[shirt_color].png",
    (0, 0), "Character/hair-long-[hair_color]-front.png",
)

# change size of player sprite
transform character_transform:
    zoom 0.5
    align(0.0, 0.7)

# change size, position arrows, & animate arrows
transform arrows:
    zoom 0.5
    anchor(0.5, 0.5)
    on hover:
        zoom 0.55
    on idle:
        zoom 0.5

# the customization
screen character_customization:
    add "character" align(0.5, 0.5)
    #add "character" at half_size align(0.5, 0.5)
    # Hair
    imagebutton idle "UI/arrow-right.png" align(0.7, 0.3) action Function(customize_character, type = "hair", direction = "right") at arrows
    imagebutton idle "UI/arrow-left.png" align(0.3, 0.3) action Function(customize_character, type = "hair", direction = "left") at arrows
    # Skin
    imagebutton idle "UI/arrow-right.png" align(0.7, 0.4) action Function(customize_character, type = "skin", direction = "right") at arrows
    imagebutton idle "UI/arrow-left.png" align(0.3, 0.4) action Function(customize_character, type = "skin", direction = "left") at arrows
    # Eyes
    imagebutton idle "UI/arrow-right.png" align(0.7, 0.5) action Function(customize_character, type = "eyes", direction = "right") at arrows
    imagebutton idle "UI/arrow-left.png" align(0.3, 0.5) action Function(customize_character, type = "eyes", direction = "left") at arrows
    # Shirt
    imagebutton idle "UI/arrow-right.png" align(0.7, 0.6) action Function(customize_character, type = "shirt", direction = "right") at arrows
    imagebutton idle "UI/arrow-left.png" align(0.3, 0.6) action Function(customize_character, type = "shirt", direction = "left") at arrows

# start scene
label scene_1:
    scene background
    show character at character_transform
    c "This is a custom character"

# customization screen
screen start_screen:
    image "Backgrounds/background.png"
    imagebutton auto "UI/start-button-%s.png" align(0.2, 0.9) action Jump("scene_1") #at half_size
    hbox:
        align(0.2, 0.1)
        text "Character name:" size 18 color "#000000" yalign 0.5 outlines[(absolute(2), "#FFFFFF", 0, 0)]
        frame:
            background "#FFFFFF"
            yalign 0.5
            input value VariableInputValue("character_name") minwidth 150 length 10

    use character_customization

define character_name = ""
define c = Character(name = "character_name", dynamic = True)

# define customization assets
label start:
    $skin_colors = ["light", "medium", "dark"]
    $hair_colors = ["blonde", "brown", "pink"]
    $eye_colors = ["blue", "dark-pink", "green"]
    $shirt_colors = ["blue", "green", "pink"]

    $skin_color = skin_colors[0]
    $hair_color = hair_colors[0]
    $eye_color = eye_colors[0]
    $shirt_color = shirt_colors[0]
    call screen start_screen
    return
