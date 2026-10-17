label chapter2:
    scene black
    with dissolve

    centered "{size=+8}CHAPTER 2{/size}\n{size+=3}didn't we do this already?{/size}"
    pause 1.0

    narrator "Tuesday, 8:03 AM"
    noah "Good morning, sweetheart. Did you sleep well?"
    mc "(The same message, at the same time.)"
    mc "(At lunch, I decided to test something.)"
    mc "Hey, remember what I told you yesterday about my class?"
    noah "Of course."
    mc "What did I say?"
    noah "You said.. it was a class."
    mc "(He laughs, waiting for me to laugh too.)"

    menu:
        "Pretend that was a good answer.":
            $ affection += 1
            mc "Wow, incredible memory."
            noah "I try my best for you."

        "Tell him you're serious.":
            $ suspicion += 1
            mc "I'm serious, Noah. You don't remember?"
            noah "I just got distracted."

        "Ask if days ever feel repititive.":
            $ memory += 1
            mc "Do you ever feel like you've lived through the same day before?"
            noah "No."
            mc "(His answer is immediate.)"
            noah "Why would you ask me that?"

    mc "I suggest we go to a bookstore across town."
    noah "Our cafe closes early today, doesn't it?"
    mc "We are not going to a cafe."
    noah "Right.. the bookstore."
    mc "(He says it like he's reading a correction on an invisible screen.)"
    noah "Of course, as you lo-"
    mc "(He stops.)"
    noah "You love books."
    mc "I do?"
    noah "Don't you?"
    if suspicion >= 2:
        noah "Have I done something wrong?"
        mc "I don't know yet."
    else:
        noah "Hey, don't overthink things."
    
    mc "For the first time, Noah looks genuinely unsure."

    jump chapter3