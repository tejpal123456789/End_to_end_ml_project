from typing import List
def get_requirements(filepath:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    with open(filepath) as file:
        requirements=file.readlines()
        #print(requirements)
        requirements=[req.replace('/n','') for req in requirements]
        return requirements
       
get_requirements('requirements.txt')