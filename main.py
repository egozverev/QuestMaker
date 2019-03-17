# -*- coding: UTF-8 -*-
import interface
import sys
import json
import argparse


def check_state(config, state):
    '''

    :param config: dict, scenario file
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
        if key not in config["status"]:
            return False
        if operator == 'is' and not config["status"][key] == value:
            return False
        if operator == 'less' and not config["status"][key] < value:
            return False
        if operator == 'more' and not config["status"][key] > value:
            return False
    return True


def change_state(config, change):
    '''
    Change the status according to 'change'
    :param config: dict, scenario file
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
        if key not in config["status"] or operator == 'make':
            config["status"][key] = value
        if operator == '+':
            config["status"][key] += value
        if operator == '-':
            config["status"][key] -= value


def play_location(config, name):
    '''
    Does everyhing is necessary to interact with the new location.
    :param config: dict, configuration parameters of scenario
    :param name: str, name of the location
    :return:
    '''
    interface.show_interface(config, name)
    number_of_choices = len(config["loc_options"][name])
    if not number_of_choices:
        return
    while True:
        choice = int(input())
        if 1 <= choice <= number_of_choices:
            required = config["loc_required"][name][choice - 1]
            if required != 'nothing':
                if not check_state(config, required):
                    print("It is not possible to do it. (>﹏<) ")
                    continue

            change = config["loc_changes"][name][choice - 1]
            if (change != 'nothing'):
                change_state(config, change)
            stop_flag = False  # True if we don`t need to go to location
            message = config["loc_messages"][name][choice - 1]
            print('|' * 45, message, '|' * 45, sep='\n')
            for condition, location in config["basic_check"].items():
                if check_state(config, condition) and not stop_flag:
                    stop_flag = True
                    play_location(config, location)
            if stop_flag:
                return
            location = config["loc_next"][name][choice - 1]
            play_location(config, location)
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
    play_location(config, "start")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('scenario_dir')
    args = parser.parse_args()
    play_scenario(args.scenario_dir)
