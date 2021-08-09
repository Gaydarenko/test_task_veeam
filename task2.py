"""This is the test task №2"""

import hashlib
import os


def task2(file: str):
    """
    Check files integrity.
    :param file: sting with filename
    :return: None
    """
    list_of_dict = read_file(file)
    for item in list_of_dict.items():
        list_of_dict[item[0]] = check_hash(item)
    print(list_of_dict)
    output_message(list_of_dict)


def read_file(filename: str) -> dict:
    """
    Retrieving data from file.
    :param filename: full path to the file as string
    :return: dictionary with files information
    """
    file_info = dict()
    with open(filename, 'r') as file:
        for line in file:
            line = line[:-1].split(" ")
            file_info[line[0]] = line[1:]
    return file_info


def check_hash(item: tuple):
    """
    Check file integrity.
    :param item: tuple with full path to the file as string, hash algorithm and hash
    :return: string with result hash check
    """
    if not os.path.isfile(item[0]):
        return "NOT FOUND"

    hash_obj = hashlib.new(item[1][0])
    hash_obj.update(open(item[0], "rb").read())

    return "OK" if hash_obj.hexdigest() == item[1][1] else "FAIL"


def output_message(results: dict):
    """
    Output message for user.
    :param results: dictionary with results
    :return: None
    """
    for key in results:
        print(f"{key} {results[key]}")


if __name__ == '__main__':
    task2("file.txt")
