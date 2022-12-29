from field import field
from pytest_bdd import scenario, given, when, then


@scenario('field.feature', 'one argument')
def test_field_one_argument():
    pass


@scenario('field.feature', 'many arguments')
def test_field_many_arguments():
    pass


@given('data: "goods" and argument: "title"', target_fixture='data1')
def data():
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]
    args = ['title']
    return [goods, args]


@given('data: "goods" and argument: "title", "price"', target_fixture='data2')
def data():
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]
    args = ['title', 'price']
    return [goods, args]


@when('running field function with one argument', target_fixture='result1')
def field_one_arg(data1):
    return field(data1[0], *data1[1])


@when('running field function with many arguments', target_fixture='result2')
def field_many_args(data2):
    return field(data2[0], *data2[1])


@then('the result is: "Ковер", "Диван для отдыха"')
def result(result1):
    assert result1 == ["Ковер", "Диван для отдыха"]


@then('the result is: {"title": "Ковер", "price": 2000}, {"title": "Диван для отдыха", "price": 5300}')
def result(result2):
    assert result2 == [{"title": "Ковер", "price": 2000}, {"title": "Диван для отдыха", "price": 5300}]
