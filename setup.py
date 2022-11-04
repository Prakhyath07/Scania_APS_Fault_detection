from setuptools import find_packages,setup
from typing import List


def get_requirements()-> List:
    """

    This function returns a list of requirements in list format
    """
    try:
        requirement_list:List[str] = []

        with open('requirements.txt', 'r') as f:
            lines = f.readlines()
        requirement_list = [line.replace('\n', '') for line in lines]
        if "-e ." in requirement_list:
            requirement_list.remove("-e .")

        return requirement_list
    except Exception as e:
        raise e

setup(
    name="sensor",
    version="0.0.0",
    author="Prakhyath07",
    author_email="prakhyathb07@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
    )