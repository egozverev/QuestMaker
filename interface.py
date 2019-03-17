def creative_print(str):
    '''
    Just print str in a beautiful way
    '''
    print('-' * 45, "\\ (•◡•) /" * 5, str, '-' * 45, sep='\n', end='\n')


def show_interface(config, name):
    '''
    Show location info , status and list of options
    :param path: Path to the location
    :return: Nothing, but print all the input parameters in cool way using CreativePrint()
    '''
    description = config["loc_descriptions"][name]
    options = config["loc_options"][name]

    creative_print('LOCATION DESCRIPTION')
    print(description)
    creative_print('CHARACTER STATUS')
    for field, value in config["status"].items():
        print(field, ':: ', value)
    creative_print('OPTIONS')
    for i, line in enumerate(config["loc_options"][name]):
        print(i + 1, ': ', line)
    if (not len(config["loc_options"][name])):
        print(
            'Seems we don`t have options here. Probably it is a final scene?\nYou know, in this case you don`t need options.')
    print('-' * 45, '-' * 45, sep='\n')
