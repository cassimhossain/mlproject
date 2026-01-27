from setuptools import find_packages, setup

from typing import List

Hyphe_E_Dot = "-e ."

def get_requirements(file_path:str)->List[str]:
    '''
    this will return the require libraries or packages
    '''
    requirements=[]
    
    with open(file_path) as file_obj:##temp obj
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if Hyphe_E_Dot in requirements:
            requirements.remove(Hyphe_E_Dot)
    
    return requirements


setup(
name='mlproject',
version='0.0.1',
author='Qasim Mushtaq',
author_email='cassimhossain@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')



)