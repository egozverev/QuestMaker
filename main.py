# -*- coding: UTF-8 -*-
import interface
import json
import argparse


def check_state(config, status, state):
    '''
    :param config: dict, scenario file
    :param status: dict, status
    :param state: state that has to be checked
    :return:
    '''
    for line in config["states"][state]:
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


def change_state(config, status, change):
    '''
    Change the status according to 'change'
    :param config: dict, scenario file
    :param status: dict, status
    :param change: change that has to be done
    :return:
    '''
    for line in config["state_changes"][change]:
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


def play_location(config, status, name):
    '''
    Does everyhing is necessary to interact with the new location.
    :param config: dict, configuration parameters of scenario
    :param name: str, name of the location
    :return:
    '''
    emptyness_flag = "nothing"
    interface.show_interface(config, name)
    locations_dict = config["locations"]
    number_of_choices = len(locations_dict[name]["option"])
    if not number_of_choices:
        return
    while True:
        choice = int(input())
        if 1 <= choice <= number_of_choices:
            required = locations_dict[name]["requirement"][choice - 1]
            if required != emptyness_flag:
                if not check_state(config, status, required):
                    print("It is not possible to do it. (>﹏<) ")
                    continue

            change = locations_dict[name]["change"][choice - 1]
            if change != emptyness_flag:
                change_state(config, status, change)
            stop_flag = False  # True if we don`t need to go to location
            message = locations_dict[name]["message"][choice - 1]
            print('|' * 45, message, '|' * 45, sep='\n')
            for condition, location in config["basic_check"].items():
                if check_state(config, status, condition) and not stop_flag:
                    stop_flag = True
                    play_location(config, status, location)
            if stop_flag:
                return
            location = locations_dict[name]["next"][choice - 1]
            play_location(config, status, location)
            break
        print('(>_<) Paaardon?? There is no such an option. (>_<)')


def play_scenario(path):
    '''
    Start the scenario
    :param path: path to the scenario
    :return:
    '''
    config = dict()
    with open(path, "r", encoding="utf-8") as load_file:
        config = json.load(load_file)
    status = config["status"]
    play_location(config, status, "start")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('scenario_file')
    args = parser.parse_args()
    play_scenario(args.scenario_file)
