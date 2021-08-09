"""This is the test task №3"""

from pathlib import Path
import random
import logging
import time
from datetime import datetime as dt
import psutil


class TestCase:
    """
    Base class for test cases
    """

    def __init__(self, tc_id, name):
        self.tc_id = tc_id
        self.name = name


class CaseType1(TestCase):
    """
    Test case №1
    """

    def __init__(self, tc_id, name):
        super().__init__(tc_id, name)

    def prep(self):
        """
        If the current system time, specified as an integer number of seconds
         from the beginning of the Unix epoch, is not a multiple of two,
         then the test case interrupted.
        :return: None
        """
        if int(time.time()) % 2 != 0:
            raise SystemExit

    def run(self):
        """
        Return list files from the current user's home directory.
        :return: list of files in home directory
        """
        paths = Path.home().glob("*.*")
        files = list(map(lambda x: x.name, paths))
        return files

    def clean_up(self):
        """
        No action required.
        :return: None
        """
        pass


class CaseType2(TestCase):
    """
    Test case №2
    """

    def __init__(self, tc_id, name):
        super().__init__(tc_id, name)

    def prep(self):
        """
        If the amount of RAM of the machine on which the test is executed is less than one gigabyte,
            then the test case interrupted.
        :return: None
        """
        if psutil.virtual_memory()[0] < 1073741824:
            raise SystemExit

    def run(self):
        """
        Create a 1024 KB file test with random content.
        :return: None
        """
        filename = "test.txt"
        path = Path(filename)

        with open(filename, 'w') as file:
            while path.stat().st_size < 1024:
                file.write(chr(random.randint(33, 126)))
            file.truncate(1024)

    def clean_up(self):
        """
        Delete file test.
        :return: None
        """
        test_file = Path("test.txt")
        test_file.unlink()


class Execute:
    """
    General order of test cases execution
    """

    def execute(self, test_cases):
        """
        The method sets the general order of the test case execution.
          All stages of the test case execution,
          as well as exceptional situations are documented in the log file.
        :param test_cases: object
        :return: None
        """
        logging.basicConfig(filename="some.log", filemode="w", level=logging.DEBUG)
        for test_case in test_cases:
            log = logging.getLogger(f"{test_case.__class__}")
            try:
                log.debug(f"Start method prep() for test_case {test_case.tc_id} {test_case.name}")
                test_case.prep()
            except SystemExit:
                log.exception(dt.now())
                continue

            try:
                log.debug(f"Start method run for test_case - {test_case.tc_id} {test_case.name}")
                test_case.run()
            except Exception:
                log.exception(dt.now())

            try:
                log.debug(f"Start method clean_up for test_case {test_case.tc_id} {test_case.name}")
                test_case.clean_up()
            except Exception:
                log.exception(dt.now())


if __name__ == '__main__':
    test1 = CaseType1(1, "testcase1")
    test2 = CaseType2(2, "testcase2")
    execute = Execute()
    execute.execute([test1, test2])
