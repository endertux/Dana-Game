# character customization tutorial: https://www.youtube.com/watch?v=6pNWrjbDwIU&ab_channel=__ess__Ren%27PyTutorials
# assets by __ess__ Ren'Py Tutorials

image character = Composite(
    (846, 1028),
    (0, 0), "Character/hair-long-[hair_color]-back.png",
    (0, 0), "Character/body-skin-[skin_color].png",
    (0, 0), "Character/eyecolor-[eye_color].png",
    (0, 0), "Character/shirt-[shirt_color].png",
    (0, 0), "Character/hair-long-[hair_color]-front.png",

)

transform character_transform:
    zoom 0.5
    align(0.0, 0.7)

label scene_1:
    scene background
    show character at character_transform
    "This is a custom character"

label start:
    $skin_colors = ["light", "medium", "dark"]
    $hair_colors = ["blonde", "brown", "pink"]
    $eye_colors = ["blue", "dark-pink", "green"]
    $shirt_colors = ["blue", "green", "pink"]

    $skin_color = skin_colors[0]
    $hair_color = hair_colors[0]
    $eye_color = eye_colors[0]
    $shirt_color = shirt_colors[0]
    jump scene_1

    return
