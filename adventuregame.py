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

print("took you long enough")