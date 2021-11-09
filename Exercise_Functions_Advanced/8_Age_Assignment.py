def age_assignment(*args, **kwargs):
    dict_res = {i: kwargs.get(i[0]) for i in args}
    return dict_res


print(age_assignment('Peter', 'George', G=26, P=19))







