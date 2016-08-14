These are little scripts I've written in the process of trying to obtain all of the achievements in Stardew Valley. They are written to be entirely independent of one another.

+ **achievement_checker.py**: Checks which achievements the selected save file has obtained, and what's missing to complete them. Which crops have had less than 15 shipped, which fish haven't been caught, etc.

      ![achievement_checker](https://github.com/skatje-myers/stardewscripts/blob/master/screenshots/achievement_checker.png)
+ **crafting.py**: For each recipe that has not yet been crafted, it prints out the required ingredients and how many the player has of them in their inventory, fridge, and chests combined.

      ![crafting](https://github.com/skatje-myers/stardewscripts/blob/master/screenshots/crafting.png)
+ **artifact_locations.py**: This prints the locations of the artifact dig spots ("worms"/"roots") for the day. It just prints "Desert", "BusStop", etc., but if you could uncomment the alternative print statements, it'll print the X,Y coordinates. You know, if you want to be even more of cheater.

      ![artifact_locations](https://github.com/skatje-myers/stardewscripts/blob/master/screenshots/artifact_locations.png)

All files can take as an argument the path to your save file, but if no arguments are given, it'll provide a menu to specify.

Please report bugs!
