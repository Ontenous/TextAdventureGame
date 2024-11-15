
print(f"""
       __             _,-"~^"-. 
     _// )      _,-"~`         `. 
   ." ( /`"-,-"`                 ; 
  / 6                             ; 
 /           ,             ,-"     ; 
(,__.--.      \           /        ; 
 //'   /`-.\   |          |        `._________ 
   _.-'_/`  )  )--...,,,___\     \-----------,) 
 ((("~` _.-'.-'           __`-.   )         // 
   jgs ((("`             (((---~"`         // 
                                          ((________________  
      """)

print(f"""
          Before we begin your adventure, there is a few things you should know. 
          There are 5 Adventurers to choose from, each with their own story, 
          class, and more. Kinsuna, Mirajane, Xuri Volk, Pollux, and Erza. You 
          may choose immediately, or you can put 'info' before the character's name 
          to get more information. Thank you for reading.""")
print()

while True:
    dnd_class = input("Who would you like to be? ")
    dnd_class = dnd_class.title()
    if dnd_class == "Kinsuna":
        break
    if dnd_class == "Xuri" or dnd_class == "Xuri Volk":
        break
    if dnd_class == "Mirajane":
        break
    if dnd_class == "Pollux":
        break
    if dnd_class == "Erza":
        break
    if dnd_class == "Info Kinsuna":
        print(f"""
Born in Rileuda's Kingdom, Kinsuna is a half Gold Dragonborn 
half Tiefling. Adept at Divination, this wizard has traveled all 
across the lands of Quenya, though the past few years been aiding 
tieflings, victims of a poaching crisis for their horns are a 
powerful tool for spellcasting. On his latest adventure, he has 
chosen to undertake the pilgramage to Mount Orion so that his 
capabillities may grow, and for the dominoes to fall for a 
better future for the tieflings of Ulc.
              """)
    if dnd_class == "Info Xuri" or dnd_class == "Info Xuri Volk":
      print(f"""
Olath Delmah, a kingdom miles below the surface, known as the 
underdark is where Xuri hails from. Princess of the Kingdom, 
She fled to the surface to see the stars. Before she was born,
Her family worried if she would be alive, so they imbued her with
magic from the Shadowfell, which has been clawing it's way into
the streets. This gives Xuri Volk her supernatural strength, which
she used to flee on the night of the 8000th year of the kingdom.
She now seeks to venture to Mount Orion, So she may gaze at the
stars denied to her. 
              """)
    if dnd_class == "Info Mirajane":
      print(f"""
Mirajane is from the Forests of Ithe, home to many avian races. 
Born as an Air Elemental though, she has always struggled to fit
in, despite the warming community. Long ago, their people used to 
migrate to Mount Orion, and so to truly be a part of the community, 
she set out to join the pilgramage. Though now, her innate magic 
allowing her to cast spells as a sorcereris poisoning her, a 
condition known as Tempestual Collapse, where her body slowly 
begins to form rock and lightning. Her only hope of a cure is  
a Black lotus, which she so desperately hopes to find. 
            """)
    if dnd_class == "Info Pollux":
        print(f"""
Born in the Nelithralvi Desert, Pollux has traveled hundreds
of miles across Quenya for his pilgrimage. Deep within the desert
was his village, a small underground place to hide from the 
violent magnetic storm above, where the dead do not remain
docile. Pollux lost his twin brother to these creatures, deemed
'The Lonely' and all he has to remember him is a Black Lotus flower.
He is a rogue, and is used to having to slink around the desert
and remain unseen. Now he goes to Mount Orion, to honor his brother,
and to visit more of the world.
              """)
    if dnd_class == "Info Erza":
        print(f"""
A siren, born from the sea foam, lived the average life. She sung
and lured in sailors, but eventually over the endless blue horizon, 
she saw a dryad, named Ambrosia, and they promised each other their
lives. Erza eventually became a pirate for a notable crew, being the 
bard and cook of the ship. Her lover was unfortunately killed in a 
battle. She now travels on the pilgrimage to Mount Orion, so that she
may see more of the world, hear and tell more stories, and make
some new friends. 
              """)

print()
print()
print()

opening_dialogue = {
    "Kinsuna":"""
Amidst the large crowds and bellowing laughter, the stench of grog, smoke,
and sweat blasts you as you head up the stairs. People cheer and sing along 
with the bard currently on stage, tankard's slosh around mead all over the floor, 
and the bard’s bright colors and loose fabric grab your attention. Somewhere 
in the seating area is a slightly peculiarly dark corner you notice, where a… 
dragonborn(?) has small piles of dust scattered around the table, looking smugly 
at the person across. He taps his lanterns onto the pile closest to the man, 
sparkling with bright colors. The man falls out of his chair, as the man bellows a hearty laugh""",
    "Xuri":"""
A small drow woman sits upon a barrel in the underbelly of the ship. Her once 
finely crafted and embellished with silvers and gems mildly scraped, torn from 
various adventures. You sit amongst the mead, needing a break from the constant 
crowds of people, their pungent odors being a new sensation to adapt to. 
Deciding you have been down here for quite the while, as well as a sore butt,
you close your book and stand up.""",
    "Mirajane":"""
Chilling mists breeze across your face, overcast clouds block the sun 
and fresh rain coats the slick deck. A few ship members yell and carry out their 
daily duties, though you also notice 2 of the passengers of the ship staring off of 
the boat. One’s wispy body melting into the sky stares off at the shore, the other 
dressed in thinner clothes wrapped around on all sides gazes across the sea, the 
Sea Dragon’s Scales peaking over the crashing waves.""",
    "Pollux":"""
Chilling mists breeze across your face, overcast clouds block the sun 
and fresh rain coats the slick deck. A few ship members yell and carry out their 
daily duties, though you also notice 2 of the passengers of the ship staring off of 
the boat. One’s wispy body melting into the sky stares off at the shore, the other 
dressed in thinner clothes wrapped around on all sides gazes across the sea, the 
Sea Dragon’s Scales peaking over the crashing waves.""",
    "Erza":"""
Amidst the large crowds and bellowing laughter, the stench of grog, smoke,
and sweat blasts you as you head up the stairs. People cheer and sing along 
with the bard currently on stage, tankard's slosh around mead all over the floor, 
and the bard’s bright colors and loose fabric grab your attention."""

}

if dnd_class == "Xuri" or dnd_class == "Xuri Volk":
    print(opening_dialogue["Xuri"])
if dnd_class == "Kinsuna":
    print(opening_dialogue["Kinsuna"])
if dnd_class == "Mirajane":
    print(opening_dialogue["Mirajane"])
if dnd_class == "Pollux":
    print(opening_dialogue["Pollux"])
if dnd_class == "Erza":
    print(opening_dialogue["Erza"])

while True:
    op_loc = input("""
Upon this ship lies 3 different decks, the Underbelly, The Tween Deck,
and above deck. Where would you like to go?
    """)
    op_loc = op_loc.title()
    if op_loc == "The Underbelly" or op_loc == "Underbelly":
        print("""
Scattered barrels, occasionally leaking mead are strewn about,
as well as various spices, and ship supplies.
        """)
        if dnd_class == "Kinsuna" or dnd_class == "Pollux" or dnd_class == "Mirajane" or dnd_class == "Erza":
            print("""
A small drow woman sits upon a barrel in the underbelly of the ship. Her once 
finely crafted and embellished with silvers and gems mildly scraped, torn from 
various adventures.
            """)
            xd1 = input("Would you like to talk to them? ")
            if xd1 == "No" or xd1 == "no":
                continue
            if xd1 == "Yes" or xd1 == "yes":
                while True:
                    print(f"""
{dnd_class}:
> What are you doing down here?
> What is your name?
> Hi
> How's that book you're reading?
> Leave                 """)
                    xd1 = input(" ")
                    if xd1 == "What are you doing down here?" or xd1 == "What are you doing down here":
                        print("Reading. It's pretty loud up there, so uh, could you leave?")
                    if xd1 == "What is your name?" or xd1 == "What is your name":
                        print("Xuri.")
                    if xd1 == "Hi" or xd1 == "hi":
                        print("Hello? ...")
                    if xd1 == "How's that book you're reading?" or xd1 == "Hows that book youre reading":
                        print("It's alright, a little damp right now.")
                    if xd1 == "Leave" or xd1 == "leave":
                        break

        elif dnd_class == "Xuri" or dnd_class == "Xuri Volk":
            continue

    if op_loc == "The Tween Deck" or op_loc == "Tween Deck":
        print("""
        Amidst the large crowds and bellowing laughter, the stench of grog, smoke,
        and sweat blasts you as you head up the stairs. People cheer and sing along with 
        the bard currently on stage, tankard's slosh around mead all over the floor, 
        and the bard’s bright colors and loose fabric grab your attention. Somewhere in 
        the seating area is a slightly peculiarly dark corner you notice, where a… dragonborn(?) 
        has small piles of dust scattered around the table, looking smugly at the person across. 
        He taps his lanterns onto the pile closest to the man, sparkling with bright colors. 
        The man falls out of his chair, as the man bellows a hearty laugh
        """)