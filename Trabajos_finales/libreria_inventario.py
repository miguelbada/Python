from colorama import Fore, Style, init


def warning_message(text):
    print(Fore.RED + text + Style.RESET_ALL)

def success_message(text):
    """
    Imprime un mensaje de éxito en la consola.

    :param text: El texto del mensaje de éxito a imprimir.
    """
    print(Fore.GREEN + text + Style.RESET_ALL)

def info_message(text):
    """
    Imprime un mensaje informativo en la consola.

    :param text: El texto del mensaje informativo a imprimir.
    """
    print(Fore.BLUE + text + Style.RESET_ALL)

def is_null(value):
    """
    Chequa si el valor no es None o una cadena vacía.

    :param value: El valor a verificar, puede ser de cualquier tipo.
    :return: True si el valor no es None y no es una cadena vacía, False en caso contrario.
    
    """
    return value is None or value == ""

def error_null(value, name=""):
    """
    Imprime un mensaje de error si el valor es None o una cadena vacía.

    :param value: El valor a verificar.
    :param name: El nombre del mensaje de error a imprimir si el valor es None o una cadena vacía.
    """
    var = False
    if is_null(value):
        warning_message(f"El valor '{name}' no puede ser nulo o vacío. Por favor, ingrese un valor válido.")
        var = True

    return var
