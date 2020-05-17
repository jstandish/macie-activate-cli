from PyInquirer import prompt, print_json, Separator, style_from_dict, Token
import sys
# try:
from colorama import Fore, Back, Style
# except ImportError:
#     colorama = None


prog_description = 'CLI interface to Isengard'

# Account/role selection menu style:
pyinq_style = style_from_dict({
    Token.Separator: '#6C6C6C',
    Token.QuestionMark: '#FF9D00 bold',
    Token.Selected: '#5F819D',
    Token.Pointer: '#FF9D00 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#5F819D bold',
    Token.Question: '',
})

def print_info(message):
    print( Fore.YELLOW + message + Fore.RESET)

def print_headline(message):
    print( Fore.GREEN + message)
    print_padding(len(message), '-')
    print(Fore.RESET)

def print_padding(length, char):
    print('{s:{c}^{n}}'.format(s='', n=length, c=char))


def print_warning(message):
    print( Fore.MAGENTA + message + Fore.RESET)

def confirmation(message):
    """Returns True if user confirms operation"""
    question = [
        {
            'type': 'confirm',
            'name': 'confirm',
            'message': message,
            'default': False,
        }
    ]
    answer = prompt(question)
    if 'confirm' not in answer:
        sys.exit(1)
    if not answer['confirm']:
        return False
    return True


def ask(question, default=None, validator=lambda x: len(x) > 0):
    """Returns string with answer"""
    question = [
        {
            'type': 'input',
            'name': 'value',
            'message': question,
            'default': '' if not default else default,
            'validate': validator
        }
    ]
    answer = prompt(question)
    if 'value' not in answer:
        sys.exit(1)
    return answer['value']

def select(message, choices, display=lambda x: ''):
    """Returns string with answer"""


    displayChoices = []

    for c in choices:
        displayChoices.append(
            {
                'name' : display(c),
                'value' : c
            }
        )


    question = [
        {
            'type': 'list',
            'name': 'selection',
            'message': message,
            'choices': displayChoices,
        }
    ]

    answers = prompt(question, style=pyinq_style)

    if 'selection' not in answers:
        # User cancelled, exit script:
        sys.exit(1)

    return answers['selection']