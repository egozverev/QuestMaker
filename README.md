# QuestMaker project
MIPT, 2nd term
This simple project allows everybody to create text quests.
Instruction how to run scenario:
- If u have not done it yet, install python3 on your device.
- Download a project and remember where main.py is placed.
- Open you console( you are under windows) / terminal (you are under linux or whatever).
- Run this: python {path_to_main.py}/main.py {path_to_scenario}

Instruction how to create a scenario:
- Create a new folder for your scenario.
- Create following folders and files:
- - locations
- - state_changes
- - states
- - basic_check.txt
- - default_status.txt
- Create locations, state changes and states, fill basic_check.txt and default_status.txt. Follow instructions down.

Default status:
This file contains information about status of you character in the beginning of the game.
Just put the name of status_parametr and then its value
> Note: Don`t use whitespaces in your name, use '_' instead <

States:
For each state create a file, for example, name.txt
Each string in this file chekcs some conditions:
`parameter operator value`
Operator may be one of these:
- is : check if parameter = value
- less: check if parameter < value
- more: check if parameter > value

>Note: If parametr doesn`t exist, statement is always false

State changes:
Each file causes changes of the status.
Each string should look like this:
`parameter operator value`
Operator may be one of these:
- make: parameter becomes value
- +: parameter increases on value
- -: parameter decreases on value

> Note: If parametr doesn`t exist, operator is automatically make

Locations:
Each location should be a folder containing following files:
- description.txt
Just a description which the player see when the character enters the location
- options.txt
List of options player may choose. Just strings with some text.
> Note: There is a rule here: one string - one option

- required.txt
For each option set the required state. If there are not states, put string 'nothing' there.
If the state is false, player will get a notification.
> Note: There is still a rule here: one string - one requirement. If you have to check multiple requirements then write them all in checking file

- changes.txt
List of changes caused by each option.  Each strhing contains change_name.txt ( or not txt) file

> Note: There is always  a rule here: one string - one change.

- messages.txt
Just show player some messages depending on the option he has chosen.
> Note: Again, one string - one message for each option

- next_locations.txt
Contains the name of locations player will be moved depending on the option he has chosen. 
> Note: I won`t get tired repeating this, one string - one location for each option


Basic check:
After each changing status programme will check all the states written here and if it succeed in one of them, it reacts.
Each string should be like that:
'check.txt location_name'
> Tip: If you want, for example, check health of the character and send a player to the death-location specailly made for this case,  use this option.

> Warning: Never in your life leave empty strings in configuration files.


