#!/usr/bin/env python

""" crafting.py:
	Print requirements for items that haven't been crafted yet, comparing with items owned.
	Author: Skatje Myers (sk@tjemye.rs)
	https://github.com/skatje-myers/stardewscripts """

import sys
import os
import xml.etree.ElementTree as ET

RED = '\033[31m'
GREEN = '\033[32m'
END = '\033[0m'


def save_location():
	if os.name == 'posix':
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
			print('Choose save file [0-' + str(len(saves) - 1) + ']:')
			i = int(input(options))
		return path + '/' + saves[i] + '/' + saves[i]
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
			print('Choose save file [0-' + str(len(saves) - 1) + ']:')
			i = int(input(options))
		return path + '\\' + saves[i] + '\\' + saves[i]


def print_missing(missing, craftable_items, owned_items):
	for item in missing:
		can_craft = True
		missing_ingredients = dict()
		owned_ingredients = dict()
		ingredients = craftable_items[item]
		for ingredient in ingredients:
			if ingredient not in owned_items:
				can_craft = False
				missing_ingredients[ingredient] = '0/' + str(ingredients[ingredient])
			elif owned_items[ingredient] < ingredients[ingredient]:
				can_craft = False
				missing_ingredients[ingredient] = str(owned_items[ingredient]) + '/' + str(ingredients[ingredient])
			else:
				owned_ingredients[ingredient] = str(owned_items[ingredient]) + '/' + str(ingredients[ingredient])
		if can_craft:
			print(GREEN + '\t' + item + ': ' + END, end='')
			for i in range(0, len(owned_ingredients)):
				name = list(owned_ingredients.keys())[i]
				num = owned_ingredients[name]
				print(name + ' (' + num + ')', end='')
				if i == len(owned_ingredients) - 1:
					print('')
				else:
					print(', ', end='')
		else:
			print(RED + '\t' + item + ': ' + END, end='')
			for i in range(0, len(owned_ingredients)):
				name = list(owned_ingredients.keys())[i]
				num = owned_ingredients[name]
				print(name + ' (' + num + ')', end='')
				if i == len(owned_ingredients) - 1:
					print(', ' + END, end='')
				else:
					print(', ', end='')
			for i in range(0, len(missing_ingredients)):
				name = list(missing_ingredients.keys())[i]
				num = missing_ingredients[name]
				print(RED + name + ' (' + num + ')', end='')
				if i == len(missing_ingredients) - 1:
					print('' + END)
				else:
					print(', ', end='')

def main():
	args = sys.argv
	if len(args) == 2:
		tree = ET.parse(args[1])
	else:
		tree = ET.parse(save_location())
	player = tree.find('player')

	fish = ['Albacore', 'Anchovy', 'Angler', 'Bream', 'Bullhead', 'Bullhead', 'Carp', 'Catfish', 'Cockle', 'Crab', 'Crayfish', 'Crimsonfish', 'Dorado', 'Eel', 'Ghostfish', 'Glacierfish', 'Halibut', 'Herring', 'Ice Pip', 'Largemouth Bass', 'Lava Eel', 'Legend', 'Lingcod', 'Lobster', 'Mussel', 'Mutant Carp', 'Octopus', 'Oyster', 'Perch', 'Periwinkle', 'Pike', 'Pufferfish', 'Rainbow Trout', 'Red Mullet', 'Red Snapper', 'Salmon', 'Sandfish', 'Sardine', 'Scorpion Carp', 'Sea Cucumber', 'Shad', 'Shrimp', 'Smallmouth Bass', 'Snail', 'Squid', 'Stonefish', 'Sturgeon', 'Sunfish', 'Super Cucumber', 'Tiger Trout', 'Tilapia', 'Tuna', 'Walleye', 'Woodskip']
	craftable_items = {'Bomb': {'Iron Ore' : 4, 'Coal' : 1},'Cherry Bomb': {'Copper Ore' : 4, 'Coal' : 1},'Crab Pot': {'Wood' : 40, 'Iron Bar' : 3},'Explosive Ammo': {'Iron Bar' : 1, 'Coal' : 2},'Field Snack': {'Acorn' : 1, 'Maple Seed' : 1, 'Pine Cone' : 1},'Gate': {'Wood' : 10},'Hardwood Fence': {'Hardwood' : 1},'Iridium Sprinkler': {'Gold Bar' : 1, 'Iridium Bar' : 1, 'Battery Pack' : 1},'Iron Fence': {'Iron Bar' : 1},'Jack-O-Lantern': {'Pumpkin' : 1 , 'Torch' : 1},'Mega Bomb': {'Gold Ore' : 4, 'Solar Essence' : 1, 'Void Essence' : 1},'Quality Sprinkler': {'Iron Bar' : 1, 'Gold Bar' : 1, 'Refined Quartz' : 1},'Sprinkler': {'Copper Bar' : 1, 'Iron Bar' : 1},'Stone Fence': {'Stone' : 2},'Torch': {'Wood' : 1, 'Sap' : 2},'Wood Fence': {'Wood' : 2},'Cobblestone Path': {'Stone' : 1},'Crystal Floor': {'Refined Quartz' : 1},'Crystal Path': {'Refined Quartz' : 1},'Drum Block': {'Stone' : 10, 'Copper Ore' : 2, 'Fiber' : 20},'Flute Block': {'Stone' : 10, 'Copper Ore' : 2, 'Fiber' : 20},'Gravel Path': {'Stone' : 1},'Stepping Stone Path': {'Stone' : 1},'Stone Floor': {'Stone' : 1},'Straw Floor': {'Wood' : 1, 'Fiber' : 1},'Weathered Floor': {'Wood' : 1},'Wood Floor': {'Wood' : 1},'Wood Path': {'Wood' : 1},'Basic Fertilizer': {'Sap' : 2},'Basic Retaining Soil': {'Stone' : 2},'Deluxe Speed-Gro': {'Oak Resin' : 1, 'Coral' : 1},'Quality Fertilizer': {'Sap' : 2, 'Fish' : 1},'Quality Retaining Soil': {'Stone' : 3, 'Clay' : 1}, 'Bee House': {'Wood' : 40, 'Coal' : 8, 'Iron Bar' : 1, 'Maple Syrup': 1}, 'Oil Maker': {'Slime' : 50, 'Hardwood' : 20, 'Gold Bar' : 1}, 'Preserves Jar': {'Wood' : 50, 'Stone' : 40, 'Coal' : 8}, 'Staircase': {'Stone' : 99}, 'Loom': {'Wood' : 60, 'Fiber' : 30, 'Pine Tar' : 1}, 'Mayonnaise Machine': {'Wood' : 15, 'Stone' : 15, 'Earth Crystal' : 1, 'Copper Bar' : 1}, 'Seed Maker': {'Wood' : 25, 'Coal' : 10, 'Gold Bar' : 1}, 'Transmute (Fe)': {'Copper Bar' : 3}, 'Cheese Press': {'Wood' : 45, 'Stone' : 45, 'Hardwood' : 10, 'Copper Bar' : 1}, 'Scarecrow': {'Wood' : 50, 'Coal' : 1, 'Fiber' : 20}, 'Furnace': {'Copper Ore' : 20, 'Stone' : 25}, 'Chest': {'Wood' : 50}, 'Tapper': {'Wood' : 40, 'Copper Bar' : 2}, 'Keg': {'Wood' : 30, 'Clay' : 1, 'Copper Bar' : 1, 'Iron Bar' : 1, 'Oak Resin' : 1}, 'Rain Totem': {'Hardwood' : 1, 'Truffle Oil' : 1, 'Pine Tar' : 5}, 'Wild Seeds (Fa)': {'Common Mushroom' : 1, 'Wild Plum' : 1, 'Hazelnut' : 1, 'Blackberry' : 1}, 'Marble Brazier': {'Marble' : 1, 'Aquamarine' : 1, 'Stone' : 100}, 'Iridium Band': {'Iridium Bar' : 5, 'Solar Essence' : 50, 'Void Essence' : 50}, 'Life Elixir': {'Red Mushroom' : 1, 'Purple Mushroom' : 1, 'Morel' : 1, 'Chanterelle' : 1}, 'Trap Bobber': {'Copper Bar' : 1, 'Sap' : 10}, 'Slime Incubator': {'Iridium Bar' : 2, 'Slime' : 100}, 'Sturdy Ring': {'Copper Bar' : 10, 'Refined Quartz' : 5, 'Earth Crystal' : 10}, 'Dressed Spinner': {'Iron Bar' : 2, 'Cloth' : 1}, 'Lightning Rod': {'Iron Bar' : 1, 'Refined Quartz' : 1, 'Bat Wing' : 5}, 'Speed-Gro': {'Pine Tar' : 1, 'Clam' : 1}, 'Wooden Brazier': {'Wood' : 10, 'Coal' : 1, 'Fiber' : 5}, 'Wood Lamp-post': {'Wood' : 50, 'Battery Pack' : 1}, 'Bait': {'Bug Meat' : 1}, 'Campfire': {'Stone' : 10, 'Wood' : 10, 'Fiber' : 10}, "Tub o' Flowers": {'Wood' : 15, 'Tulip Seeds' : 1, 'Blue Jazz Seeds' : 1, 'Poppy Seeds' : 1, 'Summer Spangle Seeds' : 1}, 'Iron Lamp-post': {'Iron Bar' : 1, 'Battery Pack' : 1}, 'Stump Brazier': {'Hardwood' : 10, 'Coal' : 1}, 'Slime Egg-Press': {'Coal' : 25, 'Fire Quartz' : 1, 'Battery Pack' : 1}, 'Wild Seeds (Wi)': {'Winter Root' : 1, 'Crystal Fruit' : 1, 'Snow Yam' : 1, 'Crocus' : 1}, 'Ring of Yoba': {'Gold Bar' : 5, 'Iron Bar' : 5, 'Diamond' : 1}, 'Transmute (Au)': {'Iron Bar' : 2}, 'Skull Brazier': {'Hardwood' : 10, 'Solar Essence' : 1, 'Coal' : 1}, 'Wild Seeds (Su)': {'Spice Berry' : 1, 'Grape' : 1, 'Sweet Pea' : 1}, 'Crystalarium': {'Stone' : 99, 'Gold Bar' : 5, 'Iridium Bar' : 2, 'Battery Pack' : 1}, 'Warp Totem: Mountains': {'Hardwood' : 1, 'Iron Bar' : 1, 'Stone' : 25}, 'Barbed Hook': {'Copper Bar' : 1, 'Iron Bar' : 1, 'Gold Bar' : 1}, 'Carved Brazier': {'Hardwood' : 10, 'Coal' : 1}, 'Magnet': {'Iron Bar' : 1}, 'Worm Bin': {'Hardwood' : 25, 'Gold Bar' : 1, 'Iron Bar' : 1, 'Fiber' : 50}, 'Stone Brazier': {'Stone' : 10, 'Coal' : 1, 'Fiber' : 5}, 'Oil Of Garlic': {'Garlic' : 10, 'Oil' : 1}, 'Cork Bobber': {'Wood' : 10, 'Hardwood' : 5, 'Slime' : 10}, 'Recycling Machine': {'Wood' : 25, 'Stone' : 25, 'Iron Bar' : 1}, 'Charcoal Kiln': {'Wood' : 20, 'Gold Bar' : 1}, 'Spinner': {'Iron Bar' : 2}, 'Wild Seeds (Sp)': {'Wild Horseradish' : 1, 'Daffodil' : 1, 'Leek' : 1, 'Dandelion' : 1}, 'Gold Brazier': {'Gold Bar' : 1, 'Coal' : 1, 'Fiber' : 1}, 'Barrel Brazier': {'Wood' : 50, 'Solar Essence' : 1, 'Coal' : 1}, 'Warrior Ring': {'Iron Bar' : 10, 'Coal' : 25, 'Frozen Tear' : 10}, 'Ancient Seeds': {'Ancient Seed' : 1}, 'Treasure Hunter': {'Gold Bar' : 2}, 'Warp Totem: Beach': {'Hardwood' : 1, 'Coral' : 2, 'Fiber' : 10}, 'Wicked Statue': {'Stone' : 25, 'Coal' : 5}, 'Warp Totem: Farm' : {'Hardwood' : 1, 'Honey' : 1, 'Fiber' : 20}, 'Wild Bait': {'Fiber' : 10, 'Bug Meat' : 5, 'Slime' : 5}, 'Cask': {'Wood' : 20, 'Hardwood' : 1}}
	crafted = set()
	known_recipes = set()
	for item in player.find('craftingRecipes').findall('item'):
		name = item.find('key').find('string').text
		known_recipes.add(name)
		if int(item.find('value').find('int').text) > 0:
			crafted.add(name)
	if len(crafted) == len(craftable_items):
		print('All items have been crafted.')
		return

	owned_items = dict()  # name : number

	for item in player.find('items').findall('Item'):
		try:
			name = item.find('Name').text
			num = int(item.find('Stack').text)
		except AttributeError:
			continue
		if name not in owned_items:
			owned_items[name] = 0
		owned_items[name] += num

	locations = tree.find('locations').findall('GameLocation')
	for location in locations:
		if location.get('{http://www.w3.org/2001/XMLSchema-instance}type') == 'FarmHouse':
			items = location.find('fridge').find('items').findall('Item')
			for item in items:
				name = item.find('Name')
				if name is None:
					continue
				name = name.text
				num = int(item.find('stack').text)
				if name not in owned_items:
					owned_items[name] = 0
				owned_items[name] += num
		items = location.find('objects').findall('item')
		for item in items:
			obj = item.find('value').find('Object')
			if obj.get('{http://www.w3.org/2001/XMLSchema-instance}type') == 'Chest':
				for item in obj.find('items').findall('Item'):
					name = item.find('Name')
					if name is None:
						continue
					name = name.text
					if name in fish:
						name = 'Fish'
					num = int(item.find('Stack').text)
					if name not in owned_items:
						owned_items[name] = 0
					owned_items[name] += num

	missing = craftable_items.keys() - crafted
	unknown_missing = missing - known_recipes
	known_missing = list(missing - unknown_missing)
	unknown_missing = list(unknown_missing)

	if len(unknown_missing) > 0:
		print('Recipe unknown:')
		print_missing(sorted(unknown_missing), craftable_items, owned_items)

	if len(known_missing) > 0:
		print('Recipe known:')
		print_missing(sorted(known_missing), craftable_items, owned_items)


if __name__ == "__main__":
	main()
