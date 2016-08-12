#!/usr/bin/env python
"""achievement_checker.py: Check a Stardew Valley save file for progress towards achievements. """

__author__ = "Skatje Myers"

import sys
import xml.etree.ElementTree as ET
import math
import os

args = sys.argv
if len(args) == 2:
	tree = ET.parse(args[1])
elif os.name == 'posix':
	path = os.path.expanduser('~/.config/StardewValley/Saves/')
	saves = [x for x in os.listdir(path) if os.path.isdir(path + '/' + x)]
	if len(saves) == 0:
		print('ERROR: No save files found in ' + path)
		sys.exit()
	i = 0
	if len(saves) > 1:
		options = ''
		for j in range(0, len(saves)):
			options += '[' + str(j) + '] ' + saves[j] + '\n'
		print('Choose save file [0-' + str(len(saves)-1) + ']:')
		i = int(input(options))
	tree = ET.parse(path + '/' + saves[i] + '/' + saves[i])
else:
	path = os.path.expanduser('~\\AppData\\Roaming\\StardewValley\\Saves')
	saves = [x for x in os.listdir(path) if os.path.isdir(path + '\\' + x)]
	if len(saves) == 0:
		print('ERROR: No save files found in ' + path)
		sys.exit()
	i = 0
	if len(saves) > 1:
		options = ''
		for j in range(0, len(saves)):
			options += '[' + str(j) + '] ' + saves[j] + '\n'
		print('Choose save file [0-' + str(len(saves)-1) + ']:')
		i = int(input(options))
	tree = ET.parse(path + '\\' + saves[i] + '\\' + saves[i])


player = tree.find('player')
RED = '\033[31m'
END = '\033[0m'

print('\n############### Money ###############')
earned = int(player.find('totalMoneyEarned').text)
if earned < 10000000:
	print(str(earned) + ' earned. Achievement(s) at:')
	print(RED + '\t*** 10,000,000 ***' + END)
	if earned < 1000000:
		print(RED + '\t*** 1,000,000 ***' + END)
		if earned < 250000:
			print(RED + '\t*** 250,000 ***' + END)
			if earned < 50000:
				print(RED + '\t*** 50,000 ***' + END)
				if earned < 15000:
					print(RED + '\t*** 15,000 ***' + END)

print('\n############# Friendship #############')
npcs = player.find('friendships').findall('item')
num_5 = 0
num_10 = 0
for npc in npcs:
	points = int(npc.find('value').find('ArrayOfInt').find('int').text)
	if points >= 2500:
		num_10 += 1
	if points >= 1250:
		num_5 += 1
if num_10 < 8:
	if num_5 < 20:
		print('Have ' + str(num_5) + ' 5-heart relationships. Achievement(s) at:')
		print(RED + '\t*** 5-heart friendship with 20 people ***' + END)
		if num_5 < 10:
			print(RED + '\t*** 5-heart friendship with 10 people ***' + END)
			if num_5 == 0:
				print(RED + '\t*** 5-heart friendship with 1 person***' + END)
	print('Have ' + str(num_10) + ' 10-heart relationships. Achievement(s) at:')
	print(RED + '\t*** 10-heart friendship with 8 people ***' + END)
	if num_10 == 0:
		print(RED + '\t*** 10-heart friendship with 1 person ***' + END)

else:
	print('All friendship achievements obtained.')

print('\n################ Fish ################')
fish_ids = {'153' : 'Green Algae', '157' : 'White Algae', '152' : 'Seaweed','372' : 'Clam','705': 'Albacore','129': 'Anchovy','160': 'Angler','132': 'Bream','700': 'Bullhead','702': 'Bullhead','142': 'Carp','143': 'Catfish','718': 'Cockle','717': 'Crab','716': 'Crayfish','159': 'Crimsonfish','704': 'Dorado','148': 'Eel','156': 'Ghostfish','775': 'Glacierfish','708': 'Halibut','147': 'Herring','161': 'Ice Pip','137': 'Largemouth Bass','162': 'Lava Eel','163': 'Legend','707': 'Lingcod','715': 'Lobster','719': 'Mussel','682': 'Mutant Carp','149': 'Octopus','723': 'Oyster','141': 'Perch','722': 'Periwinkle','144': 'Pike','128': 'Pufferfish','138': 'Rainbow Trout','146': 'Red Mullet','150': 'Red Snapper','139': 'Salmon','164': 'Sandfish','131': 'Sardine','165': 'Scorpion Carp','154': 'Sea Cucumber','706': 'Shad','720': 'Shrimp','136': 'Smallmouth Bass','721': 'Snail','151': 'Squid','158': 'Stonefish','698': 'Sturgeon','145': 'Sunfish','155': 'Super Cucumber','699': 'Tiger Trout','701': 'Tilapia','130': 'Tuna','140': 'Walleye','734': 'Woodskip'}
caught_ids = set()
num_caught = 0
for item in player.find('fishCaught').findall('item'):
	caught_ids.add(item.find('key').find('int').text)
	num_caught += int(item.find('value').find('ArrayOfInt').find('int').text)
if num_caught < 100:
	print(RED + '\t*** ' + str(num_caught) + '/100 fish caught ***' + END)
if len(caught_ids) < len(fish_ids.keys()):
	print(str(len(caught_ids)) + ' kinds of fish caught. Achievement(s) at:')
	print(RED + '\t*** Catch all fish types ***' + END)
	if len(caught_ids) < 24:
		print(RED + '\t*** Catch 24 different fish types **' + END)
		if len(caught_ids) < 10:
			print(RED + '\t*** Catch 10 different fish types ***' + END)
	print('\t\tMissing:')
	missing = list(fish_ids.keys() - caught_ids)
	missing = [fish_ids[id] for id in missing]
	split = [missing[i:math.ceil(i + len(missing) / 4)] for i in range(0, len(missing), math.ceil(len(missing) / 4))]
	blanks = len(split[0]) - len(split[-1])
	if blanks > 0:
		split[3].extend([' ' for i in range(blanks)])
	for row in zip(*split):
		print('\t\t\t' + ''.join(str.ljust(item, 20) for item in row))
if num_caught >= 100 and len(caught_ids) == len(fish_ids.keys()):
	print('All fishing achievements obtained.')

print('\n############### Recipes ###############')
recipe_ids = {'226' : 'Spicy Eel','218' : 'Tom Kha Soup','456' : 'Algae Soup','605' : 'Artichoke Dip','235' : 'Autumn\'s Bounty','198' : 'Baked Fish','207' : 'Bean Hotpot','611' : 'Blackberry Cobbler','234' : 'Blueberry Tart','216' : 'Bread','618' : 'Bruschetta','209' : 'Carp Surprise','197' : 'Cheese Cauliflower','220' : 'Chocolate Cake','727' : 'Chowder','648' : 'Coleslaw','201' : 'Complete Breakfast','223' : 'Cookie','732' : 'Crab Cakes','612' : 'Cranberry Candy','238' : 'Cranberry Sauce','214' : 'Crispy Bass','242' : 'Dish O\' The Sea','231' : 'Eggplant Parmesan','729' : 'Escargot','240' : 'Farmer\'s Lunch','649' : 'Fiddlehead Risotto','728' : 'Fish Stew','213' : 'Fish Taco','202' : 'Fried Calamari','225' : 'Fried Eel','194' : 'Fried Egg','205' : 'Fried Mushroom','610' : 'Fruit Salad','208' : 'Glazed Yams','210' : 'Hashbrowns','233' : 'Ice Cream','730' : 'Lobster Bisque','204' : 'Lucky Lunch','228' : 'Maki Roll','731' : 'Maple Bar','243' : 'Miner\'s Treat','195' : 'Omelet','457' : 'Pale Broth','211' : 'Pancakes','199' : 'Parsnip Soup','215' : 'Pepper Poppers','221' : 'Pink Cake','206' : 'Pizza','604' : 'Plum Pudding','651' : 'Poppyseed Muffin','608' : 'Pumpkin Pie','236' : 'Pumpkin Soup','609' : 'Radish Salad','230' : 'Red Plate','222' : 'Rhubarb Pie','232' : 'Rice Pudding','607' : 'Roasted Hazelnuts','244' : 'Roots Platter','196' : 'Salad','212' : 'Salmon Dinner','227' : 'Sashimi','224' : 'Spaghetti','606' : 'Stir Fry','203' : 'Strange Bun','239' : 'Stuffing','237' : 'Super Meal','241' : 'Survival Burger','480' : 'Tomato Seeds','229' : 'Tortilla','219' : 'Trout Soup','200' : 'Vegetable Medley'}
#known_recipes = set()
cooked_recipes = set()
for item in player.find('recipesCooked').findall('item'):
	cooked_recipes.add(item.find('key').find('int').text)
if len(cooked_recipes) < len(recipe_ids.keys()):
	print('Have cooked ' + str(len(cooked_recipes)) + ' different recipes. Achievement(s) at:')
	print(RED + '\t*** All recipes ***' + END)
	if len(cooked_recipes) < 25:
		print(RED + '\t*** 25 different recipes ***' + END)
		if len(cooked_recipes) < 10:
			print(RED + '\t*** 10 different recipes ***' + END)
	print('\t\tMissing:')
	missing = list(recipe_ids.keys() - cooked_recipes)
	missing = [recipe_ids[id] for id in missing]
	split = [missing[i:math.ceil(i + len(missing) / 4)] for i in range(0, len(missing), math.ceil(len(missing) / 4))]
	blanks = len(split[0]) - len(split[-1])
	if blanks > 0:
		split[3].extend([' ' for i in range(blanks)])
	for row in zip(*split):
		print('\t\t\t' + ''.join(str.ljust(item, 20) for item in row))

print('\n############## Craftables ##############')
craftable_items = {'Bomb','Cherry Bomb','Crab Pot','Explosive Ammo','Field Snack','Gate','Hardwood Fence','Iridium Sprinkler','Iron Fence','Jack-O-Lantern','Mega Bomb','Quality Sprinkler','Sprinkler','Stone Fence','Torch','Wood Fence','Cobblestone Path','Crystal Floor','Crystal Path','Drum Block','Flute Block','Gravel Path','Stepping Stone Path','Stone Floor','Straw Floor','Weathered Floor','Wood Floor','Wood Path','Basic Fertilizer','Basic Retaining Soil','Deluxe Speed-Gro','Quality Fertilizer','Quality Retaining Soil', 'Bee House', 'Oil Maker', 'Preserves Jar', 'Staircase', 'Loom', 'Mayonnaise Machine', 'Seed Maker', 'Transmute (Fe)', 'Cheese Press', 'Scarecrow', 'Furnace', 'Chest', 'Tapper', 'Keg', 'Rain Totem', 'Wild Seeds (Fa)', 'Marble Brazier', 'Iridium Band', 'Life Elixir', 'Trap Bobber', 'Slime Incubator', 'Sturdy Ring', 'Dressed Spinner', 'Lightning Rod', 'Speed-Gro', 'Wooden Brazier', 'Wood Lamp-post', 'Bait', 'Campfire', "Tub o' Flowers", 'Iron Lamp-post', 'Stump Brazier', 'Slime Egg-Press', 'Wild Seeds (Wi)', 'Ring of Yoba', 'Transmute (Au)', 'Skull Brazier', 'Wild Seeds (Su)', 'Crystalarium', 'Warp Totem: Mountains', 'Barbed Hook', 'Carved Brazier', 'Magnet', 'Worm Bin', 'Stone Brazier', 'Oil Of Garlic', 'Cork Bobber', 'Recycling Machine', 'Charcoal Kiln', 'Spinner', 'Wild Seeds (Sp)', 'Gold Brazier', 'Barrel Brazier', 'Warrior Ring', 'Ancient Seeds', 'Treasure Hunter', 'Warp Totem: Beach', 'Wicked Statue', 'Warp Totem: Farm'}
crafted = set()
#known_recipes = set()
for item in player.find('craftingRecipes').findall('item'):
	name = item.find('key').find('string').text
	#known_recipes.add(name)
	if int(item.find('value').find('int').text) > 0:
		crafted.add(name)
if len(crafted) < len(craftable_items):
	print('Have crafted ' + str(len(crafted)) + ' different items. Achievement(s) at:')
	print(RED + '\t*** Craft all items. ***' + END)
	if len(crafted) < 30:
		print(RED + '\t*** Craft 30 different items. ***' + END)
		if len(crafted) < 15:
			print(RED + '\t*** Craft 15 different items. ***' + END)
	print('\t\tMissing:')
	missing = list(craftable_items - crafted)
	split = [missing[i:math.ceil(i + len(missing) / 4)] for i in range(0, len(missing), math.ceil(len(missing) / 4))]
	blanks = len(split[0]) - len(split[-1])
	if blanks > 0:
		split[3].extend([' ' for i in range(blanks)])
	for row in zip(*split):
		print('\t\t\t' + ''.join(str.ljust(item, 20) for item in row))

print('\n############### Museum ###############')
museum_ids = {'541' : 'Aerinite','538' : 'Alamite','66' : 'Amethyst','62' : 'Aquamarine','540' : 'Baryte','570' : 'Basalt','539' : 'Bixite','542' : 'Calcite','566' : 'Celestine','72' : 'Diamond','543' : 'Dolomite','86' : 'Earth Crystal','60' : 'Emerald','544' : 'Esperite','577' : 'Fairy Stone','565' : 'Fire Opal','82' : 'Fire Quartz','545' : 'Fluorapatite','84' : 'Frozen Tear','546' : 'Geminite','561' : 'Ghost Crystal','569' : 'Granite','547' : 'Helvite','573' : 'Hematite','70' : 'Jade','549' : 'Jagoite','548' : 'Jamborite','563' : 'Jasper','550' : 'Kyanite','554' : 'Lemon Stone','571' : 'Limestone','551' : 'Lunarite','552' : 'Malachite','567' : 'Marble','574' : 'Mudstone','555' : 'Nekoite','553' : 'Neptunite','575' : 'Obsidian','560' : 'Ocean Stone','564' : 'Opal','556' : 'Orpiment','557' : 'Petrified Slime','74' : 'Prismatic Shard','559' : 'Pyrite','80' : 'Quartz','64' : 'Ruby','568' : 'Sandstone','576' : 'Slate','572' : 'Soapstone','578' : 'Star Shards','558' : 'Thunder Egg','562' : 'Tigerseye','68' : 'Topaz','587' : 'Amphibian Fossil','117' : 'Anchor','103' : 'Ancient Doll','123' : 'Ancient Drum','114' : 'Ancient Seed','109' : 'Ancient Sword','101' : 'Arrowhead','119' : 'Bone Flute','105' : 'Chewing Stick','113' : 'Chicken Statue','100' : 'Chipped Amphora','107' : 'Dinosaur Egg','116' : 'Dried Starfish','122' : 'Dwarf Gadget','96' : 'Dwarf Scroll I','97' : 'Dwarf Scroll II','98' : 'Dwarf Scroll III','99' : 'Dwarf Scroll IV','121' : 'Dwarvish Helm','104' : 'Elvish Jewelry','118' : 'Glass Shards','124' : 'Golden Mask','125' : 'Golden Relic','586' : 'Nautilus Shell','106' : 'Ornamental Fan','588' : 'Palm Fossil','120' : 'Prehistoric Handaxe','583' : 'Prehistoric Rib','579' : 'Prehistoric Scapula','581' : 'Prehistoric Skull','580' : 'Prehistoric Tibia','115' : 'Prehistoric Tool','584' : 'Prehistoric Vertebra','108' : 'Rare Disc','112' : 'Rusty Cog','110' : 'Rusty Spoon','111' : 'Rusty Spur','582' : 'Skeletal Hand','585' : 'Skeletal Tail','126' : 'Strange Doll','127' : 'Strange Doll','589' : 'Trilobite'}
donated = set()
locations = tree.find('locations').findall('GameLocation')
for location in locations:
	if location.get('{http://www.w3.org/2001/XMLSchema-instance}type') == 'LibraryMuseum':
		items = location.find('museumPieces')
		for item in items:
			donated.add(item.find('value').find('int').text)
		break
if len(museum_ids.keys() - donated) > 0:
	print(RED + '\t*** Complete the museum collection ***' + END)
	if len(donated) < 40:
		print(RED + '\t*** Donate 40 items to the museum ***' + END)
	print('\t\tMissing:')
	missing = list(museum_ids.keys() - donated)
	missing = [museum_ids[id] for id in missing]
	split = [missing[i:math.ceil(i + len(missing) / 4)] for i in range(0, len(missing), math.ceil(len(missing) / 4))]
	blanks = len(split[0]) - len(split[-1])
	if blanks > 0:
		split[3].extend([' ' for i in range(blanks)])
	for row in zip(*split):
		print('\t\t\t' + ''.join(str.ljust(item, 20) for item in row))
else:
	print('All museum achievements obtained.')

print('\n############### Quests ###############')
num_quests = int(tree.find('stats').find('questsCompleted').text)
if num_quests < 40:
	print('Have done ' + str(num_quests) + ' quests. Achievement(s) at:')
	print(RED + '\t*** 40 quests. ***' + END)
	if num_quests < 10:
		print(RED + '\t*** 10 quests. ***' + END)
else:
	print('All quest achievements obtained.')


print('\n############## Shipping ##############')
shipping_ids = {'300' : 'Amaranth','274' : 'Artichoke','284' : 'Beet','278' : 'Bok Choy','190' : 'Cauliflower','270' : 'Corn','272' : 'Eggplant','259' : 'Fiddlehead Fern','248' : 'Garlic','188' : 'Green Bean','304' : 'Hops','250' : 'Kale','24' : 'Parsnip','192' : 'Potato','276' : 'Pumpkin','264' : 'Radish','266' : 'Red Cabbage','262' : 'Wheat','280' : 'Yam','442' : 'Duck Egg','444' : 'Duck Feather','176' : 'Egg (white)','180' : 'Egg (brown)','436' : 'Goat Milk','438' : 'L. Goat Milk','174' : 'Large Egg','182' : 'Large Egg','186' : 'Large Milk','184' : 'Milk','446' : 'Rabbit\'s Foot','305' : 'Void Egg','440' : 'Wool','346' : 'Beer','424' : 'Cheese','428' : 'Cloth','307' : 'Duck Mayonnaise','426' : 'Goat Cheese','340' : 'Honey','344' : 'Jelly','350' : 'Juice','724' : 'Maple Syrup','306' : 'Mayonnaise','725' : 'Oak Resin','303' : 'Pale Ale','342' : 'Pickles','726' : 'Pine Tar','432' : 'Truffle Oil','348' : 'Wine','597' : 'Blue Jazz','418' : 'Crocus','595' : 'Fairy Rose','376' : 'Poppy','593' : 'Summer Spangle','421' : 'Sunflower','402' : 'Sweet Pea','591' : 'Tulip','78' : 'Cave Carrot','281' : 'Chanterelle','404' : 'Common Mushroom','393' : 'Coral','18' : 'Daffodil','22' : 'Dandelion','408' : 'Hazelnut','283' : 'Holly','20' : 'Leek','257' : 'Morel','422' : 'Purple Mushroom','394' : 'Rainbow Shell','420' : 'Red Mushroom','92' : 'Sap','397' : 'Sea Urchin','416' : 'Snow Yam','399' : 'Spring Onion','430' : 'Truffle','16' : 'Wild Horseradish','406' : 'Wild Plum','412' : 'Winter Root','613' : 'Apple','634' : 'Apricot','410' : 'Blackberry','258' : 'Blueberry','90' : 'Cactus Fruit','638' : 'Cherry','88' : 'Coconut','282' : 'Cranberries','414' : 'Crystal Fruit','398' : 'Grape','260' : 'Hot Pepper','254' : 'Melon','635' : 'Orange','636' : 'Peach','637' : 'Pomegranate','252' : 'Rhubarb','296' : 'Salmonberry','268' : 'Starfruit','400' : 'Strawberry','417' : 'Sweet Gem Berry','787' : 'Battery Pack','330' : 'Clay','382' : 'Coal','334' : 'Copper Bar','378' : 'Copper Ore','771' : 'Fiber','336' : 'Gold Bar','384' : 'Gold Ore','709' : 'Hardwood','337' : 'Iridium Bar','386' : 'Iridium Ore','335' : 'Iron Bar','380' : 'Iron Ore','338' : 'Refined Quartz','390' : 'Stone','388' : 'Wood', '392' : 'Nautilus Shell'}
crop_ids = {'300' : 'Amaranth','274' : 'Artichoke','188' : 'Green Bean','284' : 'Beet','258' : 'Blueberry','278' : 'Bok Choy','190' : 'Cauliflower','270' : 'Corn','282' : 'Cranberries','272' : 'Eggplant','595' : 'Fairy Rose','248' : 'Garlic','398' : 'Grape','304' : 'Hops','597' : 'Blue Jazz','250' : 'Kale','254' : 'Melon','24' : 'Parsnip','260' : 'Hot Pepper','376' : 'Poppy','192' : 'Potato','276' : 'Pumpkin','264' : 'Radish','266' : 'Red Cabbage','252' : 'Rhubarb','593' : 'Summer Spangle','268' : 'Starfruit','400' : 'Strawberry','421' : 'Sunflower','417' : 'Sweet Gem Berry','256' : 'Tomato','591' : 'Tulip','262' : 'Wheat','280' : 'Yam'}
shipped = {}
shipped_crops = {}
for item in player.find('basicShipped'):
	id = item.find('key').find('int').text
	num = int(item.find('value').find('int').text)
	shipped[id] = num
	if id in crop_ids.keys():
		shipped_crops[id] = num
if len(shipping_ids.keys() - shipped.keys()) > 0:
	print(RED + '\t*** Ship every item ***' + END + '\n\t\tMissing:')
	missing = list(shipping_ids.keys() - shipped)
	missing = [shipping_ids[id] for id in missing]
	split = [missing[i:math.ceil(i + len(missing) / 4)] for i in range(0, len(missing), math.ceil(len(missing) / 4))]
	blanks = len(split[0]) - len(split[-1])
	if blanks > 0:
		split[3].extend([' ' for i in range(blanks)])
	for row in zip(*split):
		print('\t\t\t' + ''.join(str.ljust(item, 20) for item in row))

	if len(crop_ids.keys() - shipped) > 0:
		print(RED + '\t*** Ship 15 of every crop ***' + END + '\n\t\tMissing:')
		for crop in list(shipped_crops):
			if shipped_crops[crop] < 15:
				del shipped_crops[crop]
		missing = list(crop_ids.keys() - shipped)
		missing = [crop_ids[id] for id in missing]
		split = [missing[i:math.ceil(i + len(missing) / 4)] for i in range(0, len(missing), math.ceil(len(missing) / 4))]
		blanks = len(split[0]) - len(split[-1])
		if blanks > 0:
			split[3].extend([' ' for i in range(blanks)])
		for row in zip(*split):
			print('\t\t\t' + ''.join(str.ljust(item, 20) for item in row))
	if len(shipped_crops) == 0:
		print(RED + '\t*** Ship 300 of one crop ***' + END)
	else:
		max_shipped = max(shipped_crops, key=shipped_crops.get)
		if shipped_crops[max_shipped] < 300:
			print(RED + '\t*** Ship 300 of one crop ***' + END)
			print('\t\tHighest number: ' + max_shipped + ' (' + str(shipped_crops[max_shipped]) + ')')
else:
	print('All shipping achievements obtained.')

print('\n############### Skills ###############')
skills = dict()
skills['Farming'] = int(player.find('farmingLevel').text)
skills['Mining'] = int(player.find('miningLevel').text)
skills['Combat'] = int(player.find('combatLevel').text)
skills['Foraging'] = int(player.find('foragingLevel').text)
skills['Fishing'] = int(player.find('fishingLevel').text)
max_skill = max(skills, key=skills.get)
min_skill = min(skills, key=skills.get)
if skills[max_skill] < 10:
	print(RED + '\t*** Level 10 in a skill ***' + END)
	print('\t\tCurrent top skill is ' +  max_skill + ' (' + str(skills[max_skill]) + ')')
if skills[min_skill] < 10:
	print(RED + '\t*** Level 10 in every skill ***' + END)
	print('\t\tMissing:')
	for skill in skills:
		if skills[skill] < 10:
			print('\t\t\t' + skill + ' (' + str(skills[skill]) + ')')
if skills[max_skill] == 10 and skills[min_skill] == 10:
	print('All skill achievements obtained.')


print('\n############### Other ###############')

## Mining
deepestMineLevel = int(player.find('deepestMineLevel').text)
if deepestMineLevel < 100:
	print(RED + '\t*** Level ' + str(deepestMineLevel) + '/100 reached in the mines ***')

## Protector of the Valley
monsters_killed = tree.find('stats').find('specificMonstersKilled').findall('item')
slime = 0
void = 0
bat = 0
skeleton = 0
bug = 0
duggy = 0
dust = 0
for monster in monsters_killed:
	name = monster.find('key').find('string').text
	number = int(monster.find('value').find('int').text)
	if name == 'Green Slime' or name == 'Big Slime':
		slime += number
	if name == 'Bug' or name == 'Fly' or name == 'Grub':
		bug += number
	if name == 'Bat' or name == 'Frost Bat' or name == 'Lava Bat':
		bat += number
	if name == 'Dust Spirit':
		dust += number
	if name == 'Skeleton':
		skeleton += number
	if name == 'Shadow Brute':
		void += number
	if name == 'Duggy':
		duggy += number

if slime < 1000 or void < 150 or bat < 200 or skeleton < 50 or bug < 150 or duggy < 30 or dust < 500:
	print(RED + '\t*** All monster eradication goals. ***' + END)
	print('\t\tMissing:')
	if slime < 1000:
		print('\t\t\t' + str(slime) + '/1000 slimes.')
	if void < 150:
		print('\t\t\t' + str(void) + '/150 void spirits or shadow brutes.')
	if bat < 200:
		print('\t\t\t' + str(bat) + '/200 bats.')
	if skeleton < 50:
		print('\t\t\t' + str(skeleton) + '/50 skeletons.')
	if bug < 150:
		print('\t\t\t' + str(bug) + '/150 bugs, grubs, or flies.')
	if duggy < 30:
		print('\t\t\t' + str(duggy) + '/30 duggies.')
	if dust < 500:
		print('\t\t\t' + str(dust) + '/500 dust spirits.')

## Fullhouse
kids = 0
npcs = tree.find('locations').find('GameLocation').find('characters').findall('NPC')
for npc in npcs:
	if npc.get('{http://www.w3.org/2001/XMLSchema-instance}type') == 'Child':
		kids += 1
if kids < 2:
	print(RED + '\t*** Spouse and two children ***' + END)

## Community Center
locations = tree.find('locations').findall('GameLocation')
for location in locations:
	if location.get('{http://www.w3.org/2001/XMLSchema-instance}type') == 'CommunityCenter':
		if int(location.find('numberOfStarsOnPlaque').text) < 6:
			print(RED + '\t*** Complete all community center bundles. ***' + END)
		break


## Joja Mart


## Stardrops

## Prairie King
# Beat prairie king
# beat prairie king without dying
