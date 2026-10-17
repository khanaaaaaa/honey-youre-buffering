define noah = Character(
    "Noah"
)

define mc = Character(
    "You"
)

define narrator = Character(
    " "
)

image bg room = "images/room.avif"
image bg cafe = "images/cafe.avif"

transform bg_fit:
    fit "cover"
    xalign 0.5
    yalign 0.5

transform center_char:
    xalign 0.5
    yalign 1.0
    zoom 1.5

default affection = 0
default suspicion = 0
default memory = 0
default stayed_on_call = False

label start:
    scene black
    with fade

    centered "{size=+12}honey, you're buffering{/size}"
    centered "{i}a romance that keeps repeating itself{/i}"

    pause 1.5

    jump chapter1