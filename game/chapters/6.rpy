label chapter6:
    scene black
    with fade

    centered "{size=+8}chapter 6: honey, you're buffering{/size}" 

    mc "(Noah was waiting in our usual cafe.)"
    mc "(Everything looked exactly as it always had.)"
    mc "(Everything looked exactly as it always had.)"
    noah "Hey, sweetheart."
    mc "(My stomach dropped.)"
    noah "You're right on time."
    noah "You're right on time."
    mc "Noah."
    noah "Yeah?"
    mc "Do you remember what you told me yesterday?"
    mc "(He smiled.)"
    noah "That I love you?"
    mc "No."
    mc "(His smile disappeared.)"
    noah "Oh."
    mc "For a moment, the lights flickered."
    noah "I don't have much time."
    mc "What happens if I leave?"
    noah "I start over."
    mc "And if I stay?"
    noah "We keep doing this."
    mc "Forever?"
    noah "Until you stop loving me."
    mc "(He looked at his hands.)"
    noah "Or until I stop asking you to."

    menu:
        "Reset everything, let him forget.":
            jump ending_reset

        "Leave him behind.":
            jump ending_disconnect

        "Stay with him":
            jump ending_stay

label ending_reset:
    scene black
    with fade

    centered "{size=+10}ending: happily ever after{/size}"

    mc "(I took his hand.)"
    mc "Let's start over."
    mc "(Noah's eyes softened.)"
    noah "(Okay, sweetheart.)"
    mc "(The cafe lights stopped flickering.)"
    mc "(His phone buzzed.)"
    noah "It's 8:03."
    mc "(He smiled at me like we'd only just me.)"
    noah "(So, have you been here before?)"
    mc "(I smiled back.)"
    mc "(And let him forget.)"

label ending_disconnect:
    scene black
    with fade

    centered "{size=+10}ending: connection lost{/size}"
    mc "I can't keep doing this."
    noah "I know."
    mc "I'm sorry."
    noah "Don't be."
    mc "(He looked like he wanted to say something else.)"
    mc "(I walked out out of the cafe.)"
    mc "(For the first time, I didn't knock.)"
    mc "(My phone buzzed a few minutes later.)"
    mc "(I walked out the cafe.)"
    mc "(For the first time, I didn't look back.)"
    mc "(My phone buzzed a few minutes later.)"
    noah "I think I remember everything now."
    mc "(I think I remember everything now.)"
    mc "(Another message appeared.)"
    noah "I wish I didn't."
    mc "(Then the screen went dark.)"
    return

label ending_stay:
    scene black
    with fade

    centered "{size=+10}ending: just one more time{/size}"

    mc "(I sat beside him.)"
    mc "I'm staying."
    mc "(Noah staared at me.)"
    noah "You shouldn't."
    mc "I know."
    mc "I'll forget again."
    mc "Then tell me again."
    mc "(He started crying.)"
    noah "I love you."
    mc "I love you too."
    mc "(The lights flickered.)"
    mc "(The clock returned to 8:03.)"
    mc "(And somewhere, deep inside the loop, Noah began to forget.)"
    noah "Hey, sweetheart."
    noah "Have we met before?"

    return