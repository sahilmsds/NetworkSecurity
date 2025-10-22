from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return the list of requirements.
    """
    requirement_lst:List[str] = []
    try:
        with open("requirements.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("No such file found.")
        
setup(
    name="NetworkSecurity",
    version = "0.0.1",
    author = "SahilSawant",
    author_email="smsawant17@gmail.com",
    packages=find_packages(),
    install_requirements = get_requirements()
)