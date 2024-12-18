#Ascii art for title screen
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
# Pre-Game Choices
print(f"""
          Before we begin your adventure, there is a few things you should know. 
          There are 5 Adventurers to choose from, each with their own story, 
          class, and more. Kinsuna, Mirajane, Xuri Volk, Pollux, and Erza. You 
          may choose immediately, or you can put 'info' before the character's name 
          to get more information. Also, for future notes, please try and write your
          response close to the text, I am kinda bad at programming.
          Thank you for reading and have fun!""")
print()
# Character choice, as well as Info
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
#Dictionary for Opening dialogue
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
# Checks to see if they match up with a character
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
# Variable count before Golden Ram shows up, they go to 3 different places before it does that
golden_ram = 0

# Naming Scheme: first letter = first letter of character name, second is d for dialogue or loc for location
# third letter is for the number that the dialogue is, as multiple sections of the game will have dialogue

while True:
    op_loc = input("""
Upon this ship lies 3 different decks, the Underbelly, The Tween Deck,
and above deck. Where would you like to go?
    """) # Allows them to decide, though they know where they started
    op_loc = op_loc.title()
    if op_loc == "The Underbelly" or op_loc == "Underbelly":
        print("""
Scattered barrels, occasionally leaking mead are strewn about,
as well as various spices, and ship supplies.
        """)
        golden_ram = golden_ram+1 # Made choice to go here, count increases
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
                        print("Xuri: Reading. It's pretty loud up there, so uh, could you leave?")
                    if xd1 == "What is your name?" or xd1 == "What is your name":
                        print("Xuri: Xuri.")
                    if xd1 == "Hi" or xd1 == "hi":
                        print("Xuri: Hello? ...")
                    if xd1 == "How's that book you're reading?" or xd1 == "Hows that book youre reading":
                        print("Xuri: It's alright, a little damp right now.")
                    if xd1 == "Leave" or xd1 == "leave":
                        break

        elif dnd_class == "Xuri" or dnd_class == "Xuri Volk": # They can't talk to themself
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
        The man falls out of his chair, as the other bellows a hearty laugh
        """)
        golden_ram = golden_ram+1 # ooh it's approaching!
        if dnd_class == "Kinsuna" or dnd_class == "Erza": # Can't talk to self or each other :/
            continue
        if dnd_class == "Xuri" or dnd_class == "Xuri Volk" or dnd_class == "Pollux" or dnd_class == "Erza":
            while True:
                tdd1 = input("Would you like to talk to the Dragonborn or the Bard? (Y/N) ")
                tdd1 = tdd1.title()
                kdo1 = 0 # meant to be hidden variable to open up new dialogue interactions
                if tdd1 == "Yes":
                    tdd1 = input("The Dragonborn or the Bard? ")
                    if tdd1 == "The Dragonborn" or tdd1 == "Dragonborn" or md1s == "Yes":
                        print("The angry man begins to storm away, as the gold dragonborn leans back in their chair")
                        while True:
                            print(f"""
{dnd_class}:
> Hello!
> What are you doing?
> What's your name?
> That guy seems mad
> Leave                      """)
                            if kdo1 == 1: # check to add to dialogue list, looks cool :D
                                print("> I'm pretty good, how are you?")
                            kd1 = input("")
                            kd1 = kd1.lower()
                            if kd1 == "hello!" or kd1 == "hello":
                                print("Kinsuna: Hey there, how are you?")
                                kdo1 = 1
                                continue
                            if kd1 == "what are you doing?" or kd1 == "what are you doing":
                                print("Kinsuna: Ha, telling fortunes, would you like yours read? (Y/N) ")
                                kdof = input("")
                                if kdof ==  "Yes" or kdof == "yes":
                                    print("""
Kinsuna takes out another pile of dust. They get close and let out a small spark of fire.
The smoke twists and turns into a five pointed star, then dissapates.
Kinsuna: Looks like we might have a bit of turbulence on this boat... huh.
                                """)
                                    continue
                                if kdof == "No" or kdof == "no":
                                    continue
                            if kd1 == "what's your name?" or kd1 == "whats your name" or kd1 == "what's your name" or kd1 == "whats your name?":
                                print("Kinsuna: My name's Kinsuna, nice to meet you")
                                continue
                            if kd1 == "that guy seems mad":
                                print("""
Kinsuna:Wasn't a big fan of his fortune, kinda uptight. Was pretty funny 
        though to seem him fall back and storm off like that.""")
                                continue
                            if kd1 == "i'm pretty good, how are you?" or kd1 == "im pretty good, how are you" or kd1 == "i'm pretty good how are you" or kd1 == "im pretty good how are you?":
                                print("""
Kinsuna: I'm doing alright, least we're close to ending this trip,
         I have been on here for WAY too long.""")
                            if kd1 == "leave":
                                print("Before you go, would you like to talk to the bard? (Y/N)")
                                md1s = input("")
                                break
# I am so glad that mess of a dialogue is done, they either can leave, or talk to Erza
                if tdd1 == "The Bard" or tdd1 == "Bard" or md1s == "Yes":
                    print("The bard begins to leave the stage, and you approach them.")
                    while True:
                        print(f"""
    {dnd_class}:
    > What's your name?
    > Loved the song!
    > How are you?
    > Leave
    """)
                        ed1 = input("")
                        ed1 = ed1.lower()
                        if ed1 == "what's your name?" or ed1 == "whats your name" or ed1 == "whats your name?":
                            print("Erza: Erza, Nice to meet ya")
                            continue
                        if ed1 == "loved the song!" or ed1 == "loved the song":
                            print("Erza: Thanks! I appreciate it")
                            continue
                        if ed1 == "how are you?" or ed1 == "how are you":
                            print("Erza: Bit winded, but just need to have a sit down")
                            continue
                        if ed1 == "leave":
                            print("Before you go, would you like to talk to the Dragonborn? (Y/N)")
                            md1s = input("")
                            break
                if tdd1 == "No":
                    break
