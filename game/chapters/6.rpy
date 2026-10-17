label chapter6:
    scene black
    with fade

    centered "{size=+8}chapter 6: honey, you're buffering{/size}" 

    scene bg cafe at bg_fit

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