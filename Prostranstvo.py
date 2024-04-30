def test_function():
    print('Я функция')

    def inner_function():
        print('Я в области видимости функции test_function')


test_function()
# inner_function() не вызывается и пишется что мы имели в виду test_function
