from typing import List, Dict
from dataclasses import dataclass

@dataclass
class Developer:
    def __init__(self, experience: float, github_link: str) -> None:
        self._experience = experience
        self._github_link = github_link

    @property
    def experience(self) -> float:
        return self._experience

    @property
    def github_link(self) -> str:
        return self._github_link

@dataclass
class Manager:
    def __init__(self, experience: float, github_link: str) -> None:
        self._experience = experience
        self._github_link = github_link

    @property
    def experience(self) -> float:
        return self._experience

    @property
    def github_link(self) -> str:
        return self._github_link


def get_list_of_developers(developers: List[Developer]) -> List[Dict]:
    developers_list = []
    for developer in developers:
        developers_list.append({
        'experience' : developer.experience,
        'github_link' : developer.github_link
            })
    return developers_list

def get_list_of_managers(managers: List[Manager]) -> List[Dict]:
    managers_list = []
    for manager in managers:
        managers_list.append({
        'experience' : manager.experience,
        'github_link' : manager.github_link
            })
    return managers_list

## create list of developer objects
company_developers = [
    Developer(experience=2.5, github_link='https://github.com/1'),
    Developer(experience=1.5, github_link='https://github.com/2')
]
company_developers_list = get_list_of_developers(developers=company_developers)

## create list of manager objects
company_managers = [
    Manager(experience=4.5, github_link='https://github.com/3'),
    Manager(experience=5.7, github_link='https://github.com/4')
]
company_managers_list = get_list_of_managers(managers=company_managers)
