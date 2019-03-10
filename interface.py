def creative_print(str):
    '''
    Just print str in a beautiful way
    '''
    print('-' * 45, "\\ (•◡•) /" * 5, str, '-' * 45, sep='\n', end='\n')


def show_interface(path, status):
    '''
    Show location info , status and list of options
    :param path: Path to the location
    :return: Nothing, but print all the input parameters in cool way using CreativePrint()
    '''
    description = path + 'description.txt'
    options = path + 'options.txt'

    creative_print('LOCATION DESCRIPTION')
    with open(description) as file:
        for line in file:
            print(line, end='')
        print('\n')
    creative_print('CHARACTER STATUS')
    for field, value in status.items():
        print(field, ':: ', value)
    creative_print('OPTIONS')
    with open(options) as file:
        i = 1
        for line in file:
            print(i, ': ', line, end='')
            i += 1
        if i==1:
            print('Seems we don`t have options here. Probably it is a final scene?\nYou know, in this case you don`t need options.')
        print('\n')
    print('-' * 45, '-' * 45, sep='\n')

