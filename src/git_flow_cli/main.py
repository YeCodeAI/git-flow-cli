from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from .tools import push, commit_lists, create_repo

def main() -> None:
    commands = {
        'Push to the repository': push,
        'Show all commits in the repository': commit_lists,
        'Create a new GitHub repository': create_repo
    }

    choices = [Choice(value=func, name=label) for label, func in commands.items()]

    choices.append(Choice(value=None, name='Exit'))

    choice = inquirer.select(
        message='Enter actions',
        choices=choices,
        pointer='>'
    ).execute()

    if choice:
        choice()

if __name__ == '__main__':
    main()