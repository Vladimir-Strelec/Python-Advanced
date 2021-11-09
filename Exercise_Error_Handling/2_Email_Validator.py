from Python_Advanced.Exercise_Error_Handling.custom_exceptions import NameTooShort, MustContainAtSymbolError, InvalidDomainError
from Python_Advanced.Exercise_Error_Handling.helpers import VALID_DOMAINS


email = input()


def valid_email(mail):
    try:
        name, domain = mail.split('@')
    except ValueError:
        raise MustContainAtSymbolError('Email must contain @')

    try:
        name, extension = domain.split('.')
    except ValueError:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')
    if extension not in VALID_DOMAINS:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')

    if len(name) < 4:
        raise NameTooShort('Name must be more than 4 characters')

    return True


while not email == 'End':
    if valid_email(email):
        print('Email is valid')

    email = input()
