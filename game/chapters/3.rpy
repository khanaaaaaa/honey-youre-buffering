label chapter3:
    scene black
    with dissolve

    centered "{size=+8}CHAPTER 3{/size}\n{size=+3}typing...{/size}"
    pause 1.0

    narrator "Wednesday, 11:47 PM"
    mc "(Noah calls me.)"
    noah "Hi, honey."
    mc "You're still awake?"
    noah "I wanted to hear your voice."
    mc "(We talk about nothing for a while.)"

    menu:
        "Ask what he wants for his birthday.":
            mc "Your birthday's coming up, what do you want?"
            noah "That little silver necklace you showed me."
            mc "I never showed you a necklace."
            $ suspicion += 1
            noah "You did, you just forgot."

        "Ask about our first date.":
            mc "What do you remember about our first date?"
            noah "The cafe, when you spilled your drink."
            mc "We met at the bus stop."
            $ memory += 1
            noah "No, we didn't."

        "Tell him you love him.":
            $ affection += 1
            mc "I love you, Noah."
            noah "I love you too."
            noah "I love you too."
            noah "I love you too."

    mc "(A sharp cackle cuts through the call.)"
    noah "I'm sorry, my phone's being weird."
    noah "I'm here."
    noah "I'm here."
    noah "I'm here."

    menu:
        "Stay on the call":
            $ stayed_on_call = True
            $ memory += 1
            mc "I'm not hanging up, talk to me."
            noah "I don't know what I'm supposed to say."
            noah "Please don't make me start over."

        "Hang up.":
            $ suspicion += 1
            mc "See you tomorrow."
            mc "(The call ends.)"

    mc "(The next morning, I check my call history.)"
    mc "(There is no call from Noah.)"
    mc "(But a new text is waiting.)"
    noah "Good morning, sweetheart. Did you sleep well?"

    if stayed_on_call:
        narrator "{color=#ff718d}please remember me{/color}"

    jump chapter4