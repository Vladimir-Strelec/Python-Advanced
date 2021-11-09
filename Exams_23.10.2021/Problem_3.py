def shopping_list(budget, **kwargs):
    result_dict = {}
    if budget < 100:
        return f"You do not have enough budget."
    for k, v in kwargs.items():
        summa = v[0] * v[1]
        if summa <= budget:
            if len(result_dict) < 5:
                result_dict[k] = summa
                budget -= summa
    return "\n".join([f"You bought {k} for {v:.2f} leva." for k, v in result_dict.items()])


# print(shopping_list(100, microwave=(70, 2), skirts=(15, 4), coffee=(1.50, 10),))
# print(shopping_list(20, jeans=(19.99, 1),))
print(shopping_list(104, cola=(1.20, 2), candies=(0.25, 15), bread=(1.80, 1), pie=(10.50, 5), tomatoes=(4.20, 1), milk=(2.50, 2), juice=(2, 3), eggs=(3, 1),))


# You bought skirts for 60.00 leva.
# You bought coffee for 15.00 leva.

# You do not have enough budget.