#!/usr/bin/env python

""" artifact_locations.py:
	Check a Stardew Valley save file for how many dig spots are in each location.
	Author: Skatje Myers (sk@tjemye.rs)
	https://github.com/skatje-myers/stardewscripts """

import sys
import os
import xml.etree.ElementTree as ET

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
			print('Choose save file [0-' + str(len(saves)-1) + ']:')
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
			print('Choose save file [0-' + str(len(saves)-1) + ']:')
			i = int(input(options))
		return path + '\\' + saves[i] + '\\' + saves[i]

def main():
	args = sys.argv
	if len(args) == 2:
		tree = ET.parse(args[1])
	else:
		tree = ET.parse(save_location())

	locations = tree.find('locations').findall('GameLocation')
	for location in locations:
		items = location.find('objects').findall('item')
		for item in items:
			obj = item.find('value').find('Object')
			if obj.find('name').text == 'Artifact Spot':
				name = location.find('name').text
				print(name)
				# You could print this out instead of you want the actual X,Y coordinates:
				# x = obj.find('tileLocation').find('X').text
				# y = obj.find('tileLocation').find('Y').text
				# print(name + ': (' + x + ', '  + y + ')')

if __name__ == "__main__":
	main()
