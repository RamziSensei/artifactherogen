import random

heroList = [

    ["Black"	,[	"Bloodseeker, Attack 7, Health 6",	
		"Bounty Hunter, Attack 7, Health 7",	
		"Lich, Attack 6, Health 9",	
		"Lion, Attack 6, Health 5",	
		"Necrophos, Attack 5, Health 6"	,
		"Phantom Assassin, Attack 6, Health 8",	
		"Riley the Cunning, Attack 7, Health 5"	,
		"Sniper, Attack 5, Health 6",	
		"Sorla Khan, Attack 8, Health 6",	
		"Tinker, Attack 7, Health 5",	
		"Winter Wyvern, Attack 6, Health 6"	]]

       ,

    ["Blue",	[	"Crystal Maiden, Attack 2, Health 5",	
		"Earthshaker, Attack 2, Health 7",	
		"J'Muy the Wise, Attack 3, Health 8"	,
		"Kanna, Attack 2, Health 12",	
		"Luna, Attack 3, Health 8",	
		"Meepo, Attack 4, Health 5",	
		"Ogre Magi, Attack 3, Health 7"	,
		"Outworld Devourer, Attack 4, Health 6"	,
		"Skywrath Mage, Attack 3, Health 6",	
		"Prellex, Attack 3, Health 5"	,
		"Venomancer, Attack 2, Health 6",	
		"Zeus, Attack 3, Health 7"	]]
    ,

    ["Green",	[	"Abaddon, Attack 4, Health 9"	,
		"Chen, Attack 4, Health 9"	,
		"Dark Seer, Attack 5, Health 9"	,
		"Drow Ranger, Attack 4, Health",	
		"Enchantress, Attack 4, Health 8",	
		"Fahrvhan the Dreamer, Attack 4, Health 10"	,
		"Lycan, Attack 4, Health 10",	
		"Magnus, Attack 4, Armor 1, Health 9"	,
		"Omniknight, Attack 5, Health 12",	
		"Treant Protector, Attack 4, Health 10"	,
		"Viper, Attack 4, Health 10"	]]

    ,

    ["Red",	[	"Axe, Attack 7, Armor 2, Health 11",	
		"Beastmaster, Attack 5, Health 12"	,
		"Bristleback, Attack 8, Health 12",	
		"Centaur Warrunner, Attack 4, Health 14",	
		"Keefe the Bold, Attack 6, Armor 1, Health 11"	,
		"Legion Commander, Attack 6, Armor 1, Health 8",	
		"Mazzie, Attack 6, Armor 3, Health 6",	
		"Pugna, Attack 6, Health 9",	
		"Sven, Attack 5, Health 11",	
		"Tidehunter, Attack 2, Armor 1, Health 18"	,
		"Timbersaw, Attack 4, Health 11",	
		"Ursa, Attack 7, Health 10"	]]


       ]

def getRandHero(colour):
    colour = colour.lower()
    foundColour = False
    
    for i in range(len(heroList)):
        if colour == heroList[i][0].lower():
            return random.choice(heroList[i][1])
            foundColour = True
        
    if foundColour == False:
        return int("boo!")
