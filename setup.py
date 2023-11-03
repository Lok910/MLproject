from setuptools import  find_packages, setup
hpen = '-e .'
def get_requirements(file_path:str):
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if hpen in  requirements:
            requirements.remove(hpen)
    return requirements
setup(
name = 'MlProject',
version = '0.0.1',
author = 'Lok',
author_email = 'manilok937@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')

)