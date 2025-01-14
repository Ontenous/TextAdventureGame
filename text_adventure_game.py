"""
Name: William Nathan
Date: 1/10/24
Description: text adventure game based off of a dnd session
"""
import random
import time

#------------ List of functions behind the scenes--------------
def roll():
    roll = random.randrange(1,21)
    print(f"You rolled a {roll}")
    return roll

# Variable count before Golden Ram shows up, they go to 3 different places before it does that
golden_ram = 0

# Underbelly Scene
def underbelly():
    print(underbelly_dialogue["Entrance"])
    if dnd_class == "Kinsuna" or dnd_class == "Pollux" or dnd_class == "Mirajane" or dnd_class == "Erza":
        print(underbelly_dialogue["Xuri Introduction"])
        xuri_dialogue_1 = input("Would you like to talk to them? ")
        if xuri_dialogue_1 == "No" or xuri_dialogue_1 == "no":
            return False
        if xuri_dialogue_1 == "Yes" or xuri_dialogue_1 == "yes":
            while True:
                print(f"""
    {dnd_class}:
    > What are you doing down here?
    > What is your name?
    > Hi
    > How's that book you're reading?
    > Leave                 """)
                xuri_dialogue_2 = input(" ")
                if xuri_dialogue_2 == "What are you doing down here?" or xuri_dialogue_2 == "What are you doing down here":
                    print(underbelly_dialogue["What are you doing down here?"])
                if xuri_dialogue_2 == "What is your name?" or xuri_dialogue_2 == "What is your name":
                    print(underbelly_dialogue["What is your name?"])
                if xuri_dialogue_2 == "Hi" or xuri_dialogue_2 == "hi":
                    print(underbelly_dialogue["Hi"])
                if xuri_dialogue_2 == "How's that book you're reading?" or xuri_dialogue_2 == "Hows that book youre reading":
                    print(underbelly_dialogue["How's that book you're reading?"])
                if xuri_dialogue_2 == "Leave" or xuri_dialogue_2 == "leave":
                    break
            return False
    elif dnd_class == "Xuri" or dnd_class == "Xuri Volk":  # They can't talk to themself
        return False

#Specifically Kinsuna's dialogue in the tween deck
def Kinsuna_Tween():
    kdo1 = 0
    print("The angry man begins to storm away, as the gold dragonborn leans back in their chair")
    while True:
        print(f"""
{dnd_class}:
> Hello!
> What are you doing?
> What's your name?
> That guy seems mad
> Leave                      """)
        if kdo1 == 1:  # check to add to dialogue list, looks cool :D
            print("> I'm pretty good, how are you?")
        kinsuna_dialogue_1 = input("")
        kinsuna_dialogue_1 = kinsuna_dialogue_1.lower()
        if kinsuna_dialogue_1 == "hello!" or kinsuna_dialogue_1 == "hello":
            print(kinsuna_dialogues["Hello"])
            kdo1 = 1
            continue
        if kinsuna_dialogue_1 == "what are you doing?" or kinsuna_dialogue_1 == "what are you doing":
            print(kinsuna_dialogues["What are you doing?"])
            kinsuna_optional = input("")
            if kinsuna_optional == "Yes" or kinsuna_optional == "yes":
                print(kinsuna_dialogues["Fortune Telling"])
                continue
            if kinsuna_optional == "No" or kinsuna_optional == "no":
                continue
        if kinsuna_dialogue_1 == "what's your name?" or kinsuna_dialogue_1 == "whats your name" or kinsuna_dialogue_1 == "what's your name" or kinsuna_dialogue_1 == "whats your name?":
            print(kinsuna_dialogues["What's your name?"])
            continue
        if kinsuna_dialogue_1 == "that guy seems mad":
            print("""
    Kinsuna:Wasn't a big fan of his fortune, kinda uptight. Was pretty funny 
            though to seem him fall back and storm off like that.""")
            continue
        if kinsuna_dialogue_1 == "i'm pretty good, how are you?" or kinsuna_dialogue_1 == "im pretty good, how are you" or kinsuna_dialogue_1 == "i'm pretty good how are you" or kinsuna_dialogue_1 == "im pretty good how are you?":
            print("""
    Kinsuna: I'm doing alright, least we're close to ending this trip,
             I have been on here for WAY too long.""")
        if kinsuna_dialogue_1 == "leave":
            return False

#-------- List of dictionaries before game starts-----------
# Dictionary for character choice
character_choice = {
    "text":"""
Before we begin your adventure, there is a few things you should know. 
There are 5 Adventurers to choose from, each with their own story, 
class, and more. Kinsuna, Mirajane, Xuri Volk, Pollux, and Erza. You 
may choose immediately, or you can put 'info' before the character's name 
to get more information. Also, for future notes, please try and write your
response close to the text, I am kinda bad at programming.
Thank you for reading and have fun!
          """,
    "Kinsuna":"""
Born in Rileuda's Kingdom, Kinsuna is a half Gold Dragonborn 
half Tiefling. Adept at Divination, this wizard has traveled all 
across the lands of Quenya, though the past few years been aiding 
tieflings, victims of a poaching crisis for their horns are a 
powerful tool for spellcasting. On his latest adventure, he has 
chosen to undertake the pilgramage to Mount Orion so that his 
capabillities may grow, and for the dominoes to fall for a 
better future for the tieflings of Ulc.""",
    "Xuri":"""
Olath Delmah, a kingdom miles below the surface, known as the 
underdark is where Xuri hails from. Princess of the Kingdom, 
She fled to the surface to see the stars. Before she was born,
Her family worried if she would be alive, so they imbued her with
magic from the Shadowfell, which has been clawing it's way into
the streets. This gives Xuri Volk her supernatural strength, which
she used to flee on the night of the 8000th year of the kingdom.
She now seeks to venture to Mount Orion, So she may gaze at the
stars denied to her. 
              """,
    "Mirajane":"""
Mirajane is from the Forests of Ithe, home to many avian races. 
Born as an Air Elemental though, she has always struggled to fit
in, despite the warming community. Long ago, their people used to 
migrate to Mount Orion, and so to truly be a part of the community, 
she set out to join the pilgramage. Though now, her innate magic 
allowing her to cast spells as a sorcereris poisoning her, a 
condition known as Tempestual Collapse, where her body slowly 
begins to form rock and lightning. Her only hope of a cure is  
a Black lotus, which she so desperately hopes to find. 
            """,
    "Pollux":"""
Born in the Nelithralvi Desert, Pollux has traveled hundreds
of miles across Quenya for his pilgrimage. Deep within the desert
was his village, a small underground place to hide from the 
violent magnetic storm above, where the dead do not remain
docile. Pollux lost his twin brother to these creatures, deemed
'The Lonely' and all he has to remember him is a Black Lotus flower.
He is a rogue, and is used to having to slink around the desert
and remain unseen. Now he goes to Mount Orion, to honor his brother,
and to visit more of the world.
              """,
    "Erza":"""
A siren, born from the sea foam, lived the average life. She sung
and lured in sailors, but eventually over the endless blue horizon, 
she saw a dryad, named Ambrosia, and they promised each other their
lives. Erza eventually became a pirate for a notable crew, being the 
bard and cook of the ship. Her lover was unfortunately killed in a 
battle. She now travels on the pilgrimage to Mount Orion, so that she
may see more of the world, hear and tell more stories, and make
some new friends. 
              """
}

# Dictionary for Opening dialogue
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

# All dialogue within underbelly (that makes sense to have here)
underbelly_dialogue = {
    "Entrance": """
Scattered barrels, occasionally leaking mead are strewn about,
as well as various spices, and ship supplies.
            """,
    "Xuri Introduction": """
A small drow woman sits upon a barrel in the underbelly of the ship. Her once 
finely crafted and embellished with silvers and gems mildly scraped, torn from 
various adventures.
                """,
    "What are you doing down here?":"""
Xuri: Reading. It's pretty loud up there, so uh, could you leave?
    """,
    "What is your name?":"Xuri: Xuri.",
    "Hi":"Xuri: Hello? ...",
    "How's that book you're reading?": "Xuri: It's alright, a little damp right now.",
}

#All dialogue for Kinsuna, since there are 2 characters in Tween Deck
kinsuna_dialogues = {
    "Hello":"Kinsuna: Hey there, how are you?",
    "What are you doing?":"Kinsuna: Ha, telling fortunes, would you like yours read? (Y/N) ",
    "Fortune Telling":"""
Kinsuna takes out another pile of dust. They get close and let out a small spark of fire.
The smoke twists and turns into a five pointed star, then dissapates.
Kinsuna: Looks like we might have a bit of turbulence on this boat... huh.
                                    """,
    "What's your name?":"Kinsuna: My name's Kinsuna, nice to meet you",

}





# START OF ACTUAL GAME WHERE YOU CAN JUST SEE THE BLANK SPACE






# Ascii art for title screen
print(r"""
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
for i in range(1,3):
    print("")
    time.sleep(0.5)

# Pre-Game Choices
print(character_choice["text"])
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
        print(character_choice["Kinsuna"])
    if dnd_class == "Info Xuri" or dnd_class == "Info Xuri Volk":
        print(character_choice["Xuri"])
    if dnd_class == "Info Mirajane":
        print(character_choice["Mirajane"])
    if dnd_class == "Info Pollux":
        print(character_choice["Pollux"])
    if dnd_class == "Info Erza":
        print(character_choice)

for i in range(1,4):
    print("")
    time.sleep(0.8)


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



while True:
    op_loc = input("""
Upon this ship lies 3 different decks, the Underbelly, The Tween Deck,
and above deck. Where would you like to go?
    """) # Allows them to decide, though they know where they started
    op_loc = op_loc.title()
    if op_loc == "The Underbelly" or op_loc == "Underbelly":
        golden_ram = golden_ram + 1  # Made choice to go here, count increases
        underbelly()
    if op_loc == "The Tween Deck" or op_loc == "Tween Deck":
        golden_ram = golden_ram+1 # ooh it's approaching!
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
        if dnd_class == "Kinsuna" or dnd_class == "Erza": # Can't talk to self or each other :/
            continue
        if dnd_class == "Xuri" or dnd_class == "Xuri Volk" or dnd_class == "Pollux" or dnd_class == "Erza" or dnd_class == "Mirajane":
            tween_deck_dialogue_1 = input("Would you like to talk to either of them? (Y/N) ")
            tween_deck_dialogue_1 = tween_deck_dialogue_1.title()
            if tween_deck_dialogue_1 == "Yes":
                tween_deck_dialogue_1 = input("The Dragonborn or the Bard? ")
                if tween_deck_dialogue_1 == "The Dragonborn" or tween_deck_dialogue_1 == "Dragonborn":
                    Kinsuna_Tween()
                    flip_flop = input("Before you go, would you like to talk to the bard? (Y/N) ")
                    if flip_flop == "Yes" or flip_flop == "yes":
                        pass
# Different Dialogue choices of who to talk to first
                if tween_deck_dialogue_1 == "The Bard" or tween_deck_dialogue_1 == "Bard":






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
                if tween_deck_dialogue_1 == "No":
                    break
    if op_loc == "Above Deck": # i'm tired, boss
        print("Overtop the ship lies a sea, The Sea Dragon's scales peak over the horizon.")
        golden_ram = golden_ram + 1
# Counter checking to see if they have spent enough time, so that the ship arrives
    if golden_ram == 4:
        print("""
The constant lapping of the waves is suddenly broken. For a moment it fades, 
but a roar of water echoes through the sea, droplets splash 50 feet up and 
rain back down. Gazing across the starboard side, a large ship rocks back 
and forth from breaching the surface. You instantly recognize it as the Golden Ram. 
And before you know it, the ringing of a fired cannonball heads right towards the ship.
The ship screams, the wood breaking like a bone splintering. The crew rushes around, 
panicked and unknowing what to do against the hulking ship.
        """)
        break

time.sleep(27)

# Desert Time!
print(f"""
As you hit the water, you vision goes black. What feels like a dream, you stare up at a blue sky. 
An outline of a wide brimmed hat blots out the sun, as he kneels down besides you. 
You see his charred face get close, inspect you, and then grab your hand and pull you up. 
As you stand, you look towards where the man should be, but he’s gone. {dnd_class}. You 
gaze around the desert sands, water barely in sight, 4 other figures remain on the ground. 
One by one they awake, getting up from the ground, but then seeming to snap into consciousness 
and quickly look around for… something.
The blazing hot desert sun scorches the sand underneath your feet, the burning feeling
radiating through your boots. You don’t know where you are, how you got here, or where to go. 
The only sign of life seemingly is off in the distance, a forest peeking out over the horizon, 
as well as the mountain mildly obscured by sand blowing across the wind.
""")
# Fun gimmick to show it's dnd, not super impactful so I named it Fake Choice
fake_choice = input("Would you like to go to the forest? You would die if you don't: ")
if fake_choice == "No" or fake_choice == "no":
    print("""
DM - 'Really? You are really going to go for the ONE option to die? I thought it
     would be interesting to let you choose, but I am not gonna game over you yet. Let's just...
     *pretend* that didn't happen.'""")
if fake_choice == "Yes" or fake_choice == "yes":
    print("You begin to trek towards the distant forest, your only source of hope.")

print(f"""
The once burning desert day begins to fade, the sun setting over the watery horizon. 
Your boots finally land on the first patch of grass since the last few weeks, 
mists from the nearby river cleanses your sweat, and you begin to set up camp.

Within your makeshift shelter you slowly awake, the pitch black night and mosquitoes still there. 
Wind rustles through the grass, and water continues to roll into the ocean nearby. 
Leaves crunch and breath is sucked in through sharpened teeth. 
They wait around, and then with a snort begin to walk away.

After that slight disturbance, the other 6 day's of travel go fairly smoothly. You awake, and continue
on through the pine forests of New Holman.
""")
time.sleep(18)

# seperate line for clarity, they have now arrived in Cobrock
print(f"""
After 6 days of travel, you stumble into a decently sized city. 
Calves and feet aching, as well as sore muscles make you wish to find shelter for 
at least tonight, in a nice cozy hotel with a drink. You look out towards the cityscape, 
bandaged small homes stand resilient to the past, posters displayed talking about 
anti-colonization spirit are skewn about, and people of various races, whether its 
tabaxi, tortles, lizardfolk, many walk around the town, some carrying their daily 
groceries to their homes for dinner.

You FINALLY rest upon a comfortable bed, its pillowy cradle unweaving the knots in your muscle,
and you sleep calmly.
""")
time.sleep(20)
for i in range(1,4):
    print("")
    time.sleep(0.7)
print(f"""
Waking up and being safe is a feeling you do not take for granted, as you stretch with daylight shining 
through the linen curtains. Your situation for now begins to dawn on you, as you are in an 
unfamiliar country, stranded, almost the farthest from your goals as you could be. Determined 
to continue on though, you can persevere to survive. But to survive, you’ll need money, 
and fast to replace your quickly diminishing stash. Your weapons, clothes, rations, and 
more aren’t in great condition either. But its time to face the day, and this is no time to fall to despair.
""")
# I don't know why necessarily I added this, but they could buy something? doesn't have
# the same impact as playing dnd truly, anyways
gold = 0
# this is a real thing I forgot about when I was playing the session, this is an homage to that
if dnd_class == "Kinsuna":
    print("""
Thankfully, as a fortune teller, you have always had a relatively stable income, and so
while your party goes out to search for adventure, you decide to read a few fortunes for a 
small portion of gold. 
""")
    gold = gold + 2
    print(f"You now have {gold} gold")

print("""
Asking around, many of the people point you towards a singular place.
You head to a grand building, and open up it’s gigantic wooden double doors. 
Inside, hanging chandeliers illuminate the cozy interior. Glancing 
across the walls, you see an ornately smithed symbol decorating 
many of the objects and pieces
""")

rolling = input("Enter Roll to roll a relgion check, to see if you identify the symbol: ")
if rolling == "roll" or rolling == "Roll":
    rolled = roll()
    if rolled >= 17:
        print("Success!")
        print("""
    You recognize the symbol of Trithereon, the god of the proletariat. 
    Often worshiped by revolutionaries, though not common in Quenya
    """)
    else:
        print("Failure...")
#here we go, writing this as the only update to the file