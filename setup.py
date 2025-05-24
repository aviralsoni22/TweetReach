from setuptools import setup, find_packages
from typing import List


def get_requirements()->List[str]:
    #This function will return the list of requirements
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                requirement=line.strip()
                #ignoring empty lines and -e .
                if requirement and requirement != "-e .":
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt not found")
    return requirement_lst
    
setup(
    name="TweetReach",
    version="0.0.1",
    author="Aviral Soni",
    author_email="aviralsoni22@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)
