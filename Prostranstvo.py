def test_function():
    print('Я функция', inner_function())


def inner_function():
    print('Я в области видимости функции test_function')


test_function()
inner_function()