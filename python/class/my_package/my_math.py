def factorial(x):
    """Bu fonksiyon içerisine yazilan sayinin faktöriyel değerini bulur"""

    assert x >= 0, "Negatif sayilarin faktöriyeli aranmaz"

    carpim_degeri = 1
    for i in range(x, 0, -1):

        carpim_degeri *= i

    return carpim_degeri


def my_pow(x, y):

    return x ** y


def mean(x, y):
    """Bu fonksiyon iki sayının ortalamasını verir."""

    return (x + y) / 2


def mean_(* x):
    """Girdiğiniz sayıların ortalamasını döndürür."""

    return sum([i for i in x]) / len(x)


my_pi = 3.14
