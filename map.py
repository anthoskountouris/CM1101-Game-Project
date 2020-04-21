from items import *

room_warehouse = {
    "name": "Warehouse",

    "description":
   """An old abandoned warehouse that used to be a car wash.
      It's around 2:30 am in the morning, the only source of
      light in the room is the moonlight through barred windows,
      a bouncing off the grey walls. You take a deep
      breath, bracing yourself for the mission to come.""",

    "alt description":
    """The warehouse is the same as you left it, eerily quiet.""",

    "exits": {"forward": "Main Entrance to the Research Facility"},

    "items": [item_wrench,item_hacking_device],

    "check": 0
}

room_research = {
    "name": "Main Entrance to the Research Facility",

    "description":
        """As the doors swiftly part, you feel a sudden brush of warmth,
           the regal interior of the facility masking its cruel purpose.
           No expense was wasted, fanciful furniture dotting the lobby,
           whilst a large, marble statue of the founder graces the centre.
           Ahead, you note a sign leading you to one of their no doubt
           exquisite bathrooms. To your right you see a cooped up
           Security Booth, certainly leading to further rooms in the
           facility. """,

    "alt description":
    """You better hurry with your mission before you are spotted.""",

    "exits":  {"right": "Security Booth", "left" : "Bathroom"},

    "items": [],

    "check":0
}

room_security = {
    "name": "Security Booth",

    "description":
    """The booth is small and well lit, an array of CCTV screens
    displayed on the wall. At the desk is a security
    guard, who is busy playing on their phone. Atop the desk itself rests
    a cup of coffee, steam slowly wafting from its lid.""",

    "alt description":
    """The cup of coffee is spilled across the desk, slowly dripping down
       on the phone on the floor. The security guard is still unconscious.""",

    "exits":  {"back":"Main Entrance to the Research Facility"},

    "items": [item_key,item_water],

    "check":0
}

room_bathroom = {
    "name": "Bathroom",

    "description":
    """Compared to the rest of the facility, the bathroom is rather
       bland and dull. Simple stalls dot the room, matching sinks
       opposite them.
       Above, your eye catches upon a mettalic vent, with a couple
       bolts already missing. """,

    "alt description":
    """The bathroom continues to look both bland and clean. With
       all the money in the facility, they could at least improve
       their bathrooms?""",

    "exits": {"back":"Main Entrance to the Research Facility"},

    "items": [item_soap],

    "check":0
}

room_vent = {
    "name": "Vents",

    "description":
    """The vents are dark and narrow. They're a tight fit, but there's thankfully
       just enough space to crawl. Occasionally, you catch a glimpse of other
       rooms in the building on your way through. Most of them consist of
       bland office rooms, however you do come across questionable operating
       rooms...
       You really hope it's not too late. """,

    "alt description":
    """The vents are still dark and narrow.You're running out of time.""",

    "exits": {"down": "Main Corridor","back":"Bathroom"},

    "items": [],

    "check":0
}

room_maincorridor = {
    "name": "Main Corridor",

    "description":
    """The corridors have white walls and white floors like ones from a hospital,
       which is ironic considering how this facility was built for a purpose
       opposite to that of a hospital.""",

    "alt description":
    """The corridors have white walls and white floors like ones from a hospital,
       which is ironic considering how this facility was built for a purpose
       opposite to that of a hospital.""",

    "exits": {"left": "Office","forward":"Laboratory F137","right":"Inner Corridor"},

    "items": [],

    "check":0
}

room_office = {
    "name": "Office",

    "description":
    """You enter an office, noticing the title "Director" on the door. A breeze
    blows from an exit hatch in the ceiling. A pile of documents sits unsorted 
    on the desk. Glancing at the top document you see the name Moira.
    Your mother. She's here.""",

    "alt description":
    """It's a decent room with a desk and a chair.""",

    "exits": {"back": "Main Corridor","up":"Roof"},

    "items": [item_mirror],

    "check":0
}

room_lab = {
    "name": "Labratory F137",

    "description":
    """This would look like a normal lab to someone oblivious to the facility's purpose.
       For you, that is not the case.""",

    "alt description":
    """The sooner you leave this horrifying building, the better.""",

    "exits": {"back": "Main Corridor"},

    "items": [item_smoke],

    "check":0
}

room_trappedRoom = {
    "name": "Inner Corridor",

    "description":
    """This is the room that kills.
       You. Tread. Carefully.""",

    "alt description":
    """ """,

    "exits": {"right": "Secret Laboratory","back":"Main Corridor","forward":"deathroom"},

    "items": [],

    "check":0
}

room_deathroom = {
    "name": "Deathroom",

    "description":
    """You try and walk through the corridor, but as you step forward, you smell something
    burning. The pain hits a moment later""",

    "alt description":
    """this may be unnecessary. edit as required.""",

    "exits": {"back":"Main Corridor"},

    "items":[],

    "check":0
}

room_vault_unlocked = {
    "name": "Vault ",

    "description":
    """You step into the vault to find four people tied up with black bags covering their heads.
       Unaware of who has entered, they start to tremble with fear.
       You take off the bag off the person on the far left first,
       and find yourself looking into the soft but scared eyes of your mother.
       Your heart floods with relief.
       """,

    "alt description":
    """The vault is empty, all hostages safe for now.""",

    "exits": {"back": "Inner Corridor"},

    "items": [item_treasure],

    "check":0

}

room_vault_locked = {
    "name": "Vault",

    "description":
    """You notice you're stood outside a vault, as big as a grage.
       You run your hand over the door, realising it's metal.
       """,

    "alt description":
    """You notice you're stood outside a vault, as big as a grage.
       You run your hand over the door, realising it's metal.""",

    "exits": {"back": "Inner Corridor"},

    "items": [],

    "check":0

}

room_secret_lab = {
    "name": "Secret Laboratory",

    "description":
    """You try to keep down the nausea from all the horrors brewing in this labratory.""",

    "alt description":
    """The sooner you leave this horrifying building, the better.""",

    "exits": {"back": "Inner Corridor"},

    "items": [item_acid],

    "check":0
}

room_roof = {
    "name": "Roof",

    "description":
    """Everything still seems quiet which means nobody has been alerted of your break in yet.""",

    "exits": {"back": "Vents"},

    "items": [],

    "check":0
}

rooms = {
    "Warehouse":room_warehouse,
    "Roof":room_roof,
    "Main Entrance to the Research Facility":room_research,
    "Security Booth":room_security,
    "Bathroom":room_bathroom,
    "Vents":room_vent,
    "Main Corridor":room_maincorridor,
    "Office":room_office,
    "Laboratory F137":room_lab,
    "Inner Corridor":room_trappedRoom,
    "Vault locked":room_vault_locked,
    "Vault unlocked":room_vault_unlocked,
    "Secret Laboratory":room_secret_lab,
    "deathroom":room_deathroom
}
