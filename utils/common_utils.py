import inspect
from decimal import Decimal, ROUND_HALF_UP


def get_current_calling_method():
    """
    returns the current calling method
    """
    return inspect.stack()[1][3]

def get_module_docstring(filepath):
    """

    :param filepath:
    :return:
    """

def round_exact(value, precision=2):
    decimal_num = Decimal(str(value))
    pre = 1*10 ** -precision
    return float(decimal_num.quantize(Decimal(str(pre)), rounding=ROUND_HALF_UP))


def main():
    print(get_current_calling_method())


main()
print(round_exact(10.4572, 2))