label chapter2:
    scene black
    with dissolve

    centered "{size=+8}CHAPTER 2{/size}\n{size=+3}didn't we do this already?{/size}"
    pause 1.0

    narrator "Tuesday, 8:03 AM"
    noah "Good morning, sweetheart. Did you sleep well?"
    mc "(The same message, at the same time.)"

    narrator "Later that day.."
    scene bg cafe at bg_fit

    mc "(At lunch, I decided to test something.)"
    mc "Hey, remember what I told you yesterday about my class?"
    show noahsmiletalk at center_char
    noah "Of course."
    hide noahsmiletalk
    show noahsmilequiet at center_char
    mc "What did I say?"
    hide noahsmilequiet
    show noahsmiletalk at center_char
    noah "You said.. it was a class."
    hide noahsmiletalk
    show noahsmilequiet at center_char
    mc "(He laughs, waiting for me to laugh too.)"

    menu:
        "Pretend that was a good answer.":
            $ affection += 1
            mc "Wow, incredible memory."
            hide noahsmilequiet
            show noahsmiletalk at center_char
            noah "I try my best for you."

        "Tell him you're serious.":
            $ suspicion += 1
            mc "I'm serious, Noah. You don't remember?"
            hide noahsmilequiet
            show noahsmiletalk at center_char
            noah "I just got distracted."

        "Ask if days ever feel repititive.":
            $ memory += 1
            mc "Do you ever feel like you've lived through the same day before?"
            hide noahsmilequiet
            show noahsmiletalk at center_char
            noah "No."
            hide noahsmiletalk
            show noahsmilequiet at center_char
            mc "(His answer is immediate.)"
            hide noahsmilequiet
            show noahsmiletalk at center_char
            noah "Why would you ask me that?"

    hide noahsmiletalk
    show noahsmilequiet at center_char
    mc "I suggest we go to a bookstore across town."
    hide noahsmilequiet
    show noahsmiletalk at center_char
    noah "Our cafe closes early today, doesn't it?"
    hide noahsmiletalk
    show noahsmilequiet at center_char
    mc "We are not going to a cafe."
    hide noahsmilequiet
    show noahsmiletalk at center_char
    noah "Right.. the bookstore."
    hide noahsmiletalk
    show noahsmilequiet at center_char
    mc "(He says it like he's reading a correction on an invisible screen.)"
    hide noahsmilequiet
    show noahsmiletalk at center_char
    noah "Of course, as you lo-"
    hide noahsmiletalk
    show noahsmilequiet at center_char
    mc "(He stops.)"
    hide noahsmilequiet
    show noahsmiletalk at center_char
    noah "You love books."
    hide noahsmiletalk
    show noahsmilequiet at center_char
    mc "I do?"
    hide noahsmilequiet
    show noahsmiletalk at center_char
    noah "Don't you?"
    if suspicion >= 2:
        noah "Have I done something wrong?"
        hide noahsmiletalk
        show noahsmilequiet at center_char
        mc "I don't know yet."
    else:
        noah "Hey, don't overthink things."
        hide noahsmiletalk
        show noahsmilequiet at center_char
 
    mc "For the first time, Noah looks genuinely unsure."

    jump chapter3