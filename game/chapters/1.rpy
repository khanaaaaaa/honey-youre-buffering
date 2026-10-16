label chapter1:
    scene black
    with dissolve

    centered "{size=+8}CHAPTER 1{/size}\n{size=+3}good morning, sweetheart{/size}"
    pause 1.0

    narrator "Monday, 8:03 AM"
    narrator "My phone buzzes beside my pillow."
    noah "Good morning, sweetheart. Did you sleep well?"
    mc "He always texts at 8:03. I used to think it was cute."
    menu:
        "Tell him you slept well.":
            $ affection += 1
            mc "I did, I dreamt about you."
            noah "Aw! I wish I could've been there."

        "Ask why he texts at exaactly 8:03":
            $ suspicion += 1
            mc "How do you always text at the exact same time?"
            noah "Secret :)"

        "Leave him on read":
            $ memory += 1
            mc "I put my phone face-down."
            mc "When I look again, there's another message."
            noah "You always take a while to get ready on Mondays."

    scene black
    jump chapter2