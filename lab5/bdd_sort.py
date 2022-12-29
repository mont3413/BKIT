from sort import sort_without_lambda, sort_with_lambda
from pytest_bdd import scenario, given, when, then


@scenario('sort.feature', 'sorting without lambda')
def test_sort_without_lambda():
    pass


@scenario('sort.feature', 'sorting with lambda')
def test_sort_with_lambda():
    pass


@given('data: [4, -30, 100, -100, 123, 1, 0, -1, -4]', target_fixture='data')
def data():
    return [4, -30, 100, -100, 123, 1, 0, -1, -4]


@when('running sort_without_lambda function', target_fixture='result')
def sort_wo_l(data):
    return sort_without_lambda(data)


@when('running sort_with_lambda function', target_fixture='result')
def sort_w_l(data):
    return sort_with_lambda(data)


@then('the result is sorted data: [123, 100, -100, -30, 4, -4, 1, -1, 0]')
def result(result):
    assert result == [123, 100, -100, -30, 4, -4, 1, -1, 0]
