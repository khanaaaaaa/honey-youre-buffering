label chapter1:
    scene black
    with dissolve

    centered "{size=+8}CHAPTER 1{/size}\n{size=+3}good morning, sweetheart{/size}"
    pause 1.0

    narrator "Monday, 8:03 AM"
    narrator "My phone buzzes beside my pillow."
    noah "Good morning, sweetheart. Did you sleep well?"
    mc "(He always texts at 8:03.)"
    menu:
        "Tell him you slept well.":
            $ affection += 1
            mc "I did, I dreamt about you."
            noah "Aw! I wish I could've been there."

        "Ask why he texts at exactly 8:03":
            $ suspicion += 1
            mc "How do you always text at the exact same time?"
            noah "Secret :)"

        "Leave him on read":
            $ memory += 1
            mc "(I put my phone face-down.)"
            mc "(When I look again, there's another message.)"
            noah "You always take a while to get ready on Mondays."

    scene black
    with dissolve

    narrator "Later that afternoon"
    mc "We meet at our usual cafe."
    show noahsmiletalk at center_char
    noah "There she is, my favorite person."
    hide noahsmiletalk
    show noahsmilequiet at center_char
    mc "You say that everytime."
    hide noahsmilequiet
    show noahsmiletalk at center_char
    noah "Because it's true everytime."
    mc "(He tells me the story about the pigeon that stole his sandwich.)"
    mc "(I've heard it before.)"

    menu:
        "Laugh and kiss his cheek.":
            $ affection += 1
            hide noahsmiletalk
            show noahsmilequiet at center_char
            mc "It's a good story."
            hide noahsmilequiet
            show noahsmiletalk at center_char
            noah "You're a good audience."

        "Tell him he's told you already.":
            $ suspicion += 1
            hide noahsmiletalk
            show noahsmilequiet at center_char
            mc "Noah, you told me that last week."
            hide noahsmilequiet
            show noahsmiletalk at center_char
            noah "Did I? Guess it's just that funny."

        "Ask him to tell you something new.":
            $ memory += 1
            hide noahsmiletalk
            show noahsmilequiet at center_char
            mc "Tell me something I've never heard before."
            hide noashsmilequiet
            show noahsmiletalk at center_char
            noah "Something new."
            hide noahsmiletalk
            show noahsmilequiet at center_char
            mc "He goes quiet."
            hide noahsmilequiet
            show noahsmiletalk at center_char
            noah "I really love your hair today."
            hide noahsmiletalk
            show noahsmilequiet at center_char
            mc "You said the same thing yesterday."
            hide noahsmilequiet
            show noahsmiletalk at center_char
            noah "Because I feel it everyday"
    
    hide noahsmiletalk
    show noashsmilequiet at center_char
    mc "When we leave, Noah takes my hand."
    hide noahsmilequiet
    show noahsmiletalk at center_char
    noah "Same time tomorrow?"
    hide noahsmiletalk
    show noahsmilequiet at center_char
    mc "Maybe somewhere different?"
    hide noahsmilequiet
    show noahneutralquiet at center_char
    noah "Sure.. somewhere different."
    hide noahneutralquiet
    show noahsmilequiet at center_char
    mc "(For a second, his smile doesn't show.)"
    mc "(Then he blinks, and it's normal again.)"
    jump chapter2