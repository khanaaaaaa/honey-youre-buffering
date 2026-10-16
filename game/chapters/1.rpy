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
    with dissolve

    narrator "Later that afternoon"
    mc "We meet at our usual cafe."
    noah "There she is, my favorite person."
    mc "You say that everytime."
    noah "Because it's true everytime."
    mc "He tells me the story about the pigeon that stole his sandwich."
    mc "I've heard it before."

    menu:
        "Laugh and kiss his cheek.":
            $ affection += 1
            mc "It's a good story."
            noah "You're a good audience."

        "Tell him he's told you already.":
            $ suspicion += 1
            mc "Noah, you told me that last week."
            noah "Did I? Guess it's just that funny."

        "Ask him to tell you something new.":
            $ memory += 1
            mc "Tell me something I've never heard before."
            noah "Something new."
            mc "He goes quiet."
            noah "I really love your hair today."
            mc "You said the same thing yesterday."
            noah "Right, I meant.. I really like you."
    
    mc "When we leave, Noah takes my hand."
    noah "Same time tomorrow?"
    mc "Maybe somewhere different?"
    noah "Sure.. somewhere different."
    mc "(For a second, his smile doesn't show.)"
    mc "(Then he blinks, and it's normal again.)"
    jump chapter2