from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def Get_Requirements(File_Path:str)->List[str]:
    '''
    This Function Will Return Requirements
    '''
    requirements=[]
    with open(File_Path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(

    name='mlproject',
    version='0.0.1',
    author='Arham',
    author_email='ak06598909@gmail.com',
    packages=find_packages(),
    install_requires=Get_Requirements('requirements.txt')
)