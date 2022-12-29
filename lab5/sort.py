def sort_without_lambda(data):
    return sorted(data, reverse=True, key=abs)


def sort_with_lambda(data):
    return sorted(data, reverse=True, key=lambda x: abs(x))
