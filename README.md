# QuestMaker project
> MIPT, 2nd term

This simple project allows everybody to create text quests.
Instruction how to run scenario:
- If you have not done it yet, install python3 on your device.
- Download a project and remember where main.py is placed.
- Open your console( you are under windows) / terminal (you are under linux or whatever).
- Run this: python {path_to_main.py}/main.py {path_to_scenario}

Instruction how to create a scenario:
- Create a new .json file for your scenario.
- Create following objects:
- - loc_descriptions
- - loc_changes
- - loc_messages
- - loc_next
- - loc_options
- - loc_required
- - state_changes
- - states
- - basic_check
- - default_status
- Fill each object. Follow instructions down.

Default status:
It contains information about status of you character in the beginning of the game.
Just put the name of status_parametr and then its value

States:
Each string here checks some conditions:
`parameter operator value`
Operator may be one of these:
- is : check if parameter = value
- less: check if parameter < value
- more: check if parameter > value

>Note: If parametr doesn`t exist, statement is always false

State changes:
They cause changes of the status.
Each string should look like this:
`parameter operator value`
Operator may be one of these:
- make: parameter becomes value
- +: parameter increases on value
- -: parameter decreases on value

> Note: If parametr doesn`t exist, operator is automatically make

Locations:
- descriptions
Just a description which the player see when the character enters the location
- optionss
List of options player may choose. Just strings with some text.

- required
For each option set the required state. If there are not states, put string 'nothing' there.
If the state is false, player will get a notification.

- changes
List of changes caused by each option.  Each strhing contains change_name


- messages
Just show player some messages depending on the option he has chosen.

- next
Contains the name of locations player will be moved depending on the option he has chosen.

Basic check:
After each changing status programme will check all the states written here and if it succeed in one of them, it reacts.
Each field should be like that:
'check': 'location_name'
> Tip: If you want, for example, check health of the character and send a player to the death-location specailly made for this case,  use this option.

>Tip: If something is not clear, check the example project
