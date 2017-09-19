#!/usr/bin/env python

""" cooking.py:
	Print requirements for items that haven't been crafted yet.
	Author: Skatje Myers (sk@tjemye.rs) """

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


def print_missing(missing, recipes, owned_items):
	for item in missing:
		can_craft = True
		missing_ingredients = dict()
		owned_ingredients = dict()
		ingredients = recipes[item]
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
	recipes = {'Algae Soup' :  {'Green Algae': 4},'Artichoke Dip' :  {'Artichoke ': 1, 'Milk':1},'Autumn\'s Bounty' :  {'Yam': 1, 'Pumpkin' :1},'Baked Fish' :  {'Sunfish': 1, 'Bream': 1, 'Wheat Flour': 1},'Bean Hotpot' :  {'Green Bean': 1},'Blackberry Cobbler' :  {'Blackberry': 1, 'Sugar': 1, 'Wheat Flour': 1},'Blueberry Tart' :  {'Blueberry': 1, 'Sugar': 1, 'Wheat Flour': 1},'Bread' :  {'Wheat Flour': 1},'Bruschetta' :  {'Tomato': 1, 'Bread': 1, 'Oil': 1},'Cheese Cauliflower' :  {'Cauliflower': 1, 'Cheese': 1},'Carp Surprise' :  {'Carp': 4},'Chocolate Cake' :  {'Wheat Flour': 1, 'Sugar': 1, 'Egg': 1},'Chowder' :  {'Clam': 1, 'Milk': 1},'Coleslaw' :  {'Red Cabbage': 1, 'Vinegar': 1, 'Mayonnaise': 1},'Complete Breakfast' :  {'Hashbrowns': 1, 'Fried Egg': 1, 'Milk': 1, 'Pancakes': 1},'Cookie' :  {'Wheat Flour': 1, 'Sugar': 1, 'Egg': 1},'Crab Cakes' :  {'Crab': 1, 'Wheat Flour': 1, 'Egg': 1, 'Oil': 1},'Cranberry Candy' :  {'Cranberries': 1, 'Apple': 1, 'Sugar': 1},'Cranberry Sauce' :  {'Cranberries': 1, 'Sugar': 1},'Crispy Bass' :  {'Largemouth Bass': 1, 'Wheat Flour': 1, 'Oil': 1},'Dish O\' The Sea' :  {'Sardine': 2, 'Hashbrowns': 1},'Eggplant Parmesan' :  {'Tomato': 1, 'Eggplant': 1},'Escargot' :  {'Garlic': 1, 'Snail': 1},'Farmer\'s Lunch' :  {'Parsnip': 1, 'Omelet': 1},'Fiddlehead Risotto' :  {'Garlic': 1, 'Fiddlehead Fern': 1, 'Oil': 1},'Fish Stew' :  {'Tomato': 1, 'Crayfish': 1, 'Mussel': 1, 'Periwinkle': 1},'Fish Taco' :  {'Tuna': 1, 'Tortilla': 1, 'Red Cabbage': 1, 'Mayonnaise': 1},'Fried Calamari' :  {'Squid': 1, 'Wheat Flour': 1, 'Oil': 1},'Fried Eel' :  {'Eel': 1, 'Oil': 1},'Fried Egg' :  {'Egg': 1},'Fried Mushroom' :  {'Common Mushroom': 1, 'Morel': 1, 'Oil': 1},'Fruit Salad' :  {'Apricot': 1, 'Blueberry': 1, 'Melon': 1},'Glazed Yams' :  {'Yam': 1, 'Sugar': 1},'Hashbrowns' :  {'Potato': 1, 'Oil': 1},'Ice Cream' :  {'Milk': 1, 'Sugar': 1},'Lobster Bisque' :  {'Lobster': 1, 'Milk': 1},'Lucky Lunch' :  {'Blue Jazz': 1, 'Sea Cucumber': 1, 'Tortilla': 1},'Maki Roll' :  {'Fish': 1, 'Seaweed': 1, 'Rice': 1},'Maple Bar' :  {'Maple Syrup': 1, 'Sugar': 1, 'Wheat Flour': 1},'Miner\'s Treat' :  {'Cave Carrot': 1, 'Sugar': 1, 'Milk': 1},'Omelet' :  {'Egg': 1, 'Milk': 1},'Pale Broth' :  {'White Algae': 2},'Pancakes' :  {'Wheat Flour': 1, 'Egg': 1},'Parsnip Soup' :  {'Parsnip': 1, 'Milk': 1, 'Vinegar': 1},'Pepper Poppers' :  {'Hot Pepper': 1, 'Cheese': 1},'Pink Cake' :  {'Melon': 1, 'Wheat Flour': 1, 'Sugar': 1, 'Egg': 1},'Pizza' :  {'Tomato': 1, 'Wheat Flour': 1, 'Cheese': 1},'Plum Pudding' :  {'Wild Plum': 2, 'Wheat Flour': 1, 'Sugar': 1},'Poppyseed Muffin' :  {'Poppy': 1, 'Wheat Flour': 1, 'Sugar': 1},'Pumpkin Pie' :  {'Pumpkin': 1, 'Wheat Flour': 1, 'Milk': 1, 'Sugar': 1},'Pumpkin Soup' :  {'Pumpkin': 1, 'Milk': 1},'Radish Salad' :  {'Radish': 1, 'Oil': 1, 'Vinegar': 1},'Red Plate' :  {'Red Cabbage': 1, 'Radish': 1},'Rhubarb Pie' :  {'Rhubarb': 1, 'Wheat Flour': 1, 'Sugar': 1},'Rice Pudding' :  {'Milk': 1, 'Sugar': 1, 'Rice': 1},'Roasted Hazelnuts' :  {'Hazelnut': 3},'Roots Platter' :  {'Cave Carrot': 1, 'Winter Root': 1},'Salad' :  {'Leek': 1, 'Dandelion': 1, 'Vinegar': 1},'Salmon Dinner' :  {'Kale': 1, 'Salmon': 1, 'Amaranth': 1},'Sashimi' :  {'Fish': 1},'Spaghetti' :  {'Tomato': 1, 'Wheat Flour': 1},'Spicy Eel' :  {'Eel': 1, 'Hot Pepper': 1},'Stir Fry' :  {'Kale': 1, 'Common Mushroom': 1, 'Cave Carrot': 1, 'Oil': 1},'Strange Bun' :  {'Wheat Flour': 1, 'Periwinkle': 1, 'Void Mayonnaise': 1},'Stuffing' :  {'Cranberries': 1, 'Hazelnut': 1, 'Bread': 1},'Super Meal' :  {'Bok Choy': 1, 'Cranberries': 1, 'Artichoke': 1},'Survival Burger' :  {'Cave Carrot': 1, 'Eggplant': 1, 'Bread': 1},'Tom Kha Soup' :  {'Coconut': 1, 'Common Mushroom': 1, 'Shrimp': 1},'Tortilla' :  {'Corn': 1},'Trout Soup' :  {'Rainbow Trout': 1, 'Green Algae': 1},'Vegetable Stew' : {'Tomato' : 1, 'Beet': 1}}
	recipe_ids = {'226': 'Spicy Eel', '218': 'Tom Kha Soup', '456': 'Algae Soup', '605': 'Artichoke Dip', '235': 'Autumn\'s Bounty', '198': 'Baked Fish', '207': 'Bean Hotpot', '611': 'Blackberry Cobbler', '234': 'Blueberry Tart', '216': 'Bread', '618': 'Bruschetta', '209': 'Carp Surprise', '197': 'Cheese Cauliflower', '220': 'Chocolate Cake', '727': 'Chowder', '648': 'Coleslaw', '201': 'Complete Breakfast', '223': 'Cookie', '732': 'Crab Cakes', '612': 'Cranberry Candy', '238': 'Cranberry Sauce', '214': 'Crispy Bass', '242': 'Dish O\' The Sea', '231': 'Eggplant Parmesan', '729': 'Escargot', '240': 'Farmer\'s Lunch', '649': 'Fiddlehead Risotto', '728': 'Fish Stew', '213': 'Fish Taco', '202': 'Fried Calamari', '225': 'Fried Eel', '194': 'Fried Egg', '205': 'Fried Mushroom', '610': 'Fruit Salad', '208': 'Glazed Yams', '210': 'Hashbrowns', '233': 'Ice Cream', '730': 'Lobster Bisque', '204': 'Lucky Lunch', '228': 'Maki Roll', '731': 'Maple Bar', '243': 'Miner\'s Treat', '195': 'Omelet', '457': 'Pale Broth', '211': 'Pancakes', '199': 'Parsnip Soup', '215': 'Pepper Poppers', '221': 'Pink Cake', '206': 'Pizza', '604': 'Plum Pudding', '651': 'Poppyseed Muffin', '608': 'Pumpkin Pie', '236': 'Pumpkin Soup', '609': 'Radish Salad', '230': 'Red Plate', '222': 'Rhubarb Pie', '232': 'Rice Pudding', '607': 'Roasted Hazelnuts', '244': 'Roots Platter', '196': 'Salad', '212': 'Salmon Dinner', '227': 'Sashimi', '224': 'Spaghetti', '606': 'Stir Fry', '203': 'Strange Bun', '239': 'Stuffing', '237': 'Super Meal', '241': 'Survival Burger', '480': 'Tomato Seeds', '229': 'Tortilla', '219': 'Trout Soup', '200': 'Vegetable Stew'}
	cooked = set()
	known_recipes = set()
	for item in player.find('cookingRecipes').findall('item'):
		name = item.find('key').find('string').text
		known_recipes.add(name)
	for item in player.find('recipesCooked').findall('item'):
		cooked.add(recipe_ids[item.find('key').find('int').text])
	if len(cooked) == len(recipes):
		print('All items have been cooked.')
		return

	owned_items = dict()  # name : number
	owned_items['Fish'] = 0
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
					num = int(item.find('Stack').text)
					if name not in owned_items:
						owned_items[name] = 0
					owned_items[name] += num
					if name in fish:
						owned_items['Fish'] += num

	missing = recipes.keys() - cooked
	unknown_missing = missing - known_recipes
	known_missing = list(missing - unknown_missing)
	unknown_missing = list(unknown_missing)

	if len(unknown_missing) > 0:
		print('Recipe unknown:')
		print_missing(sorted(unknown_missing), recipes, owned_items)

	if len(known_missing) > 0:
		print('Recipe known:')
		print_missing(sorted(known_missing), recipes, owned_items)


if __name__ == "__main__":
	main()
