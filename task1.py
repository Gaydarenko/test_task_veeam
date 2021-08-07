"""This is the test task №1"""

import xml.dom.minidom as minidom
import shutil
import os


def task1(config: str):
    """
    Parse config file
    :param config: string with file path
    :return: None
    """
    doc = minidom.parse(config)
    files = doc.getElementsByTagName("file")

    for file in files:
        copy_file(dict(file.attributes.items()))


def copy_file(attr: dict):
    """
    Copy file
    :param attr: dictionary with file attributes (source, dest, name)
    :return: None
    """
    source = os.path.join(attr["source_path"], attr["file_name"])
    destination = attr["destination_path"]

    shutil.copy(source, destination)


if __name__ == '__main__':
    task1("config.xml")
