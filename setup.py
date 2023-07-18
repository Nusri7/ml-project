from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = " -e ."
def get_requirements(file_path:str)-> List[str]:
    '''
    This function returns the list of requirements from the requirements.txt file
    '''
    requirements=[]
    with open(file_path,'r') as f:
        requirements=f.readlines()
        requirements=[req.replace("\n", " ") for req in requirements]
        
    
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    
setup(
    name='ml=project',
    version='0.1.0',
    author= "Nusri",
    author_email="321nusri@gmail.com",
    packages=  find_packages(),
    install_requires=get_requirements("requirements.txt")
)