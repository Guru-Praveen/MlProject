from setuptools import setup, find_packages
from typing import List

hypen = '-e .'
def create_requirements(filepath:str)->List[str]:
    requirements = []
    
    with open(filepath,'r') as file:
        requirements = file.readlines()
        requirements = [req.replace('\n', "") for req in requirements]
        for hypen in requirements:
            if hypen in requirements:
                requirements.remove(hypen)
                
        return requirements
        
        
    
setup(
    
    name='mlproject',
    version='0.0.1',
    author='praveen',
    author_email='v.gurupraveen123@gmail.com',
    packages=find_packages(),
    install_packages = create_requirements('requirements.txt')
) 