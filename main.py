import interface
import sys


def check_state(path, status):
    '''
    Check if character`s status matches the state
    :param path: str, path to the state which has to be checked
    :param status: dict, contains current character status
    :return: True if status matсhes requirements, false otherwise.
    '''
    with open(path) as file:
        for line in file:
            line = line.split()
            key = line[0]
            operator = line[1]
            value = line[2]
            if value.isdigit():
                value = int(value)
            if key not in status:
                return False
            if operator == 'is' and not status[key] == value:
                return False
            if operator == 'less' and not status[key] < value:
                return False
            if operator == 'more' and not status[key] > value:
                return False
    return True


def change_state(path, status):
    '''
    Change character`s status
    :param path: str, path to the state which has to be checked
    :param status: dict, contains current character status
    :return: nothing
    '''
    with open(path) as file:
        for line in file:
            line = line.split()
            key = line[0]
            operator = line[1]
            value = line[2]
            if value.isdigit():
                value = int(value)
            if key not in status or operator == 'make':
                status[key] = value
            if operator == '+':
                status[key] += value
            if operator == '-':
                status[key] -= value


def play_location(path, name, status):
    '''
    Does everyhing is necessary to interact with the new location.
    :param path: str, path to the scenario ( MENTION: not the location name )
    :param name: str, name of the location
    :param status: dict, contains current character status
    :return:
    '''
    interface.show_interface(path + 'locations/' + name + '/', status)
    number_of_choices = sum(1 for _ in open(path + 'locations/' + name + '/options.txt'))
    if not number_of_choices:
        return
    while True:
        choice = int(input())
        if 1 <= choice <= number_of_choices:
            required = str()
            with open(path + 'locations/' + name + '/required.txt') as file:
                for i, line in enumerate(file):
                    if i + 1 == choice:
                        required = line.strip()
            if required != 'nothing':
                if not check_state(path + 'states/' + required, status):
                    print("It is not possible to do it. (>﹏<) ")
                    continue

            change = str()
            with open(path + 'locations/' + name + '/changes.txt') as file:
                for i, line in enumerate(file):
                    if i + 1 == choice:
                        change = line.strip()
            if (change != 'nothing'):
                change_state(path + 'state_changes/' + change, status)
            stop_flag = False  # True if we don`t need to go to location
            with open(path + 'basic_check.txt') as file:
                for line in file:
                    line = line.split()
                    condition = line[0]
                    location = line[1].strip()
                    if check_state(path + 'states/' + condition, status) and not stop_flag:
                        stop_flag = True
                        play_location(path, location, status)
            if stop_flag:
                return
            location = str()
            with open(path + 'locations/' + name + '/next_locations.txt') as file:
                for i, line in enumerate(file):
                    if i + 1 == choice:
                        location = line.strip()
            message = str()
            with open(path + 'locations/' + name + '/messages.txt') as file:
                for i, line in enumerate(file):
                    if i + 1 == choice:
                        message = line.strip()
            print('|' * 45, message, '|' * 45, sep='\n')
            play_location(path, location, status)
            break
        print('(>_<) Paaardon?? There is no such an option. (>_<)')


def play_scenario(path):
    '''
    Start the scenario
    :param path: path to the scenario
    :return:
    '''
    status = dict()
    with open(path + 'default_status.txt') as file:
        for line in file:
            line = line.split()
            if line[1].isdigit():
                line[1] = int(line[1])
            status[line[0]] = line[1]
    play_location(path, 'start', status)


if __name__ == '__main__':
    scenario_dir = sys.argv[1]
    play_scenario(scenario_dir)
