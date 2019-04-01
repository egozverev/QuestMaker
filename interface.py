def creative_print(str):
    '''
    Just print str in a beautiful way
    '''
    print('-' * 45, "\\ (•◡•) /" * 5, str, '-' * 45, sep='\n', end='\n')


def show_interface(config, name):
    '''
    Print everything is needed for 'name' location
    :param config: dict, scenario file
    :param name: name of the location
    :return:
    '''
    description = config["locations"][name]["description"]
    creative_print('LOCATION DESCRIPTION')
    print(description)
    creative_print('CHARACTER STATUS')
    for field, value in config["status"].items():
        print(field, ':: ', value)
    creative_print('OPTIONS')
    for i, line in enumerate(config["locations"][name]["option"]):
        print(i + 1, ': ', line)
    if (not len(config["locations"][name]["option"])):
        print(
            'Seems we don`t have options here. Probably it is a final scene?\nYou know, in this case you don`t need options.')
    print('-' * 45, '-' * 45, sep='\n')
