label chapter6:
    scene black
    with fade

    centered "{size=+8}chapter 6: honey, you're buffering{/size}" 

    mc "(Noah was waiting in our usual cafe.)"
    mc "(Everything looked exactly as it always had.)"
    show noahneutralquiet at center_char
    noah "Hey, sweetheart."
    hide noahneutralquiet
    show noahsadquiet at center_char
    mc "(My stomach dropped.)"
    hide noahsadquiet
    show noahneutraltalk at center_char
    noah "You're right on time."
    hide noahneutraltalk
    show noahsadquiet at center_char
    mc "Noah."
    hide noahsadquiet
    show noahneutraltalk at center_char
    noah "Yeah?"
    hide noahneutraltalk
    show noahsadquiet at center_char
    mc "Do you remember what you told me yesterday?"
    mc "(He smiled.)"
    hide noahsadquiet
    show noahneutraltalk at center_char
    noah "That I love you?"
    hide noahneutraltalk
    show noahsadquiet at center_char
    mc "No."
    hide noahsadquiet
    show noahneutraltalk at center_char
    noah "Oh."
    hide noahneutraltalk
    show noahsadquiet at center_char
    mc "For a moment, the lights flickered."
    hide noahsadquiet
    show noahneutraltalk at center_char
    noah "I don't have much time."
    hide noahneutraltalk
    show noahneutralquiet at center_char
    mc "What happens if I leave?"
    hide noahneutralquiet
    show noahneutraltalk at center_char
    noah "I start over."
    hide noahneutraltalk
    show noahneutralquiet at center_char
    mc "And if I stay?"
    hide noahneutralquiet
    show noahneutraltalk at center_char
    noah "We keep doing this."
    hide noahneutraltalk
    show noahneutralquiet at center_char
    mc "Forever?"
    hide noahneutralquiet
    show noahneutraltalk at center_char
    noah "Until you stop loving me."
    hide noahneutraltalk
    show noahneutralquiet at center_char
    mc "(He looked at his hands.)"
    hide noahneutralquiet
    show noahneutraltalk at center_char
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