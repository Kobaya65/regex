import re


class Bcolors:
    # ANSI escape codes
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def phone_number_check():
    """ Vérifier la validité d'un numéro de téléphone français
        qui commence par 0, avec ou sans séparation tous les deux chiffres
        via . ou -
    """
    tel_pattern = r"^0[1-9][\s\.-]?(\d{2}[ \.-]?){4}"
    numeros_de_telephone = [
        '06-27-81-64-73',
        '0627816473',
        'aa02-12-34-56-78B',
        '02 12 33 75 12',
        '00.23.14.52.44',
        '04.23.14.52.44',
        '514-235-0293',
        '03-52-31-56-34',
        '53-52-31-56-34',
    ]
    max_long = compute_max_len(numeros_de_telephone)

    for numero in numeros_de_telephone:
        test_re = re.match(tel_pattern, numero)
        if test_re:
            print(
                f"{Bcolors.OKGREEN}Le numéro {numero:<{max_long}} est valide{Bcolors.ENDC}")
        else:
            print(
                f"{Bcolors.FAIL}Le numéro {numero:<{max_long}} est invalide{Bcolors.ENDC}")


def email_check():
    """ Vérifier la validité d'une adresse mail
    """
    email_pattern = r"^[a-zA-Z0-9\.\-_]+@[a-zA-Z0-9]+\.[a-zA-Z]+"
    emails = [
        'philamice@gmail.com',
        'toto@dget.Fr',
        'marcel.amice',
        'phil@foc',
        'f51@laposte.net',
        'roro.gmail.com',
        'rui#gmail.fr',
        'roger.fri@ghu-com',
        'toto@phil@gmail.com',
        'jean-philippe.fournier@socgen.com',
        '1ter@gmail.com',
        'info@01net.com'
    ]
    max_long = compute_max_len(emails)

    for email in emails:
        test_re = re.match(email_pattern, email)
        if test_re:
            print(
                f"{Bcolors.OKGREEN}L'adresse {email:<{max_long}} est valide{Bcolors.ENDC}")
        else:
            print(
                f"{Bcolors.FAIL}L'adresse {email:<{max_long}} est invalide{Bcolors.ENDC}")


def compute_max_len(items: list[any]) -> int:
    """ Compute length of the biggest item in a list.
    - items    : list of items\n
    Return length of the biggest item
    """
    max_long = 0
    for elem in items:
        long = len(elem)
        if long > max_long:
            max_long = long
    return max_long


def test():
    pat_neg = '^((?!result).)+$'
    pat_pos = '^((?=result).)+$'
    contents = [
        'ACM_Compliance_2024 Q1_result.xlsx',
        'ACM_Compliance_2024 Q1.xlsx',
    ]
    print('\nnegative match')
    for content in contents:
        result = re.match(pat_neg, content, re.IGNORECASE)
        print(f'{content:<50} {result}')
    print('negative search')
    for content in contents:
        result = re.search(pat_neg, content, re.IGNORECASE)
        print(f'{content:<50} {result}')
    print('-' * 120)
    print('positive match')
    for content in contents:
        result = re.match(pat_pos, content, re.IGNORECASE)
        print(f'{content:<50} {result}')
    print('positive search')
    for content in contents:
        result = re.search(pat_pos, content, re.IGNORECASE)
        print(f'{content:<50} {result}')


test()