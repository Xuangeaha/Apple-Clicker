# Apple-Clicker
Are you tired of clicking cookies? Let's try to create an Apple Ckicker by python!

## What is Cookie Clicker?
Cookie Clicker is a Javascript game released by Orteil on August 8, 2013.

It is an "incrementer" game, as proclaimed by Orteil. The point of the game is to bake cookies by clicking on a giant cookie until you have enough cookies to buy upgrades. The seemingly endless gameplay makes it a game that can last an indefinite amount of time, or at least until your device can no longer run it.

It can be found at https://orteil.dashnet.org/cookieclicker/
It can also be found on Steam.
The wiki can be found at https://cookieclicker.fandom.com/wiki/Cookie_Clicker_Wiki.

## Progress
The Apple Cicker's main gaming logic has been finished in alpha.

Now I'm focusing on beautifing the interface.
 
## Tips
The latest version of Apple Clicker is open source.

Older versions's source is closed (packed by Pyinstaller).

# Update logs

## Beta 0.2.0  2022-06-29
    ·Using ttkbootstrap to make the tkinter window more beutiful!
    ·Fix bugs:
        ·The part of update log textbox sometimes not displaying all. (AC-8)

## Beta 0.1.0  2022-06-29
    ·Add "Update log" module in the about window.
    ·Fix bugs:
        ·The price of the buildings don't change when the save was uploaded. (AC-6)
        ·The dynamic update of information grid sometimes go flashing. (AC-7)
        
## Alpha 0.5.0  2022-06-28
    ·Add the function of save & upload.
    ·Add the note in the file (in Chinese).
    ·Add the "__pycache__", "dist", "build" folder into the package.
    ·Add the .spec file into the package.
    ·Fix bugs:
        ·The dynamic update of apple amount sometimes go flashing. (AC-5)

## Alpha 0.4.1  2022-06-24
    ·Add the progress bar of level.
    ·Add the update log into the package.
    ·Add the ".idea" folder into the package.
    ·Fix bugs:
        ·The increase of apples per second by update goes up too fast. (AC-3)
        ·The increase of update price goes up too fast. (AC-4)
        
## Alpha 0.4.0  2022-06-23
    ·Add "Statistics" module.
    ·Add "Upgrades" module.
    ·Change some game logical data(price, speed, etc.) to adjust the game's difficulty.
    ·Delete the "Upgrades" button as it has now no use.
    ·Fix bugs:
        ·The increase of apples per click goes up too fast. (AC-1)
        ·The dynamic amount, price, speed of the building "Basket". (AC-2)

## Alpha 0.3.1  2022-06-22
    ·English translation all done!
    ·A big juicy apple takes the place of "Click!". (PNG Copyright: [.minecraft/assets/textures/item/apple] Minecraft/Mojang™)
    ·Add tkinter window icon.
    ·Add a logic that the price of a building will grow gradually as the amount of it grows.
    ·Add the logic of the increase of apples per click as the amount of buildings increases.
    ·Add the about tkinter window.
    ·Change some game logical data(price, speed, etc.) to increase the game's difficulty.
    ·Change the circulate time of recursion, so as to make the game more smoothly.
    
## Alpha 0.3.0  2022-06-21
    ·English translation half done.

## Alpha 0.2.0  2022-06-21
    ·Add the information section's dynamic display, buttons of upgrade, save, upload and about(all no use).
    ·Change the location of some frames to make the tkinter window look better.
    ·Change some game logical data(price, speed, etc.) to increase the game's difficulty.
    ·Change the circulate time of recursion, so as to make the game more smoothly.
    ·The extension name of the file is changed from .py to .pyw.

## Alpha 0.1.0  2022-06-20
    ·Add the basic game logic.
    ·Add the tkinter window which has information section(no use), information grid, achievement text(no use).
