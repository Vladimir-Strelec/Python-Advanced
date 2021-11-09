from collections import deque

number_of_pizzas = [int(el) for el in input().split(', ') if 0 < int(el) <= 10]
pizza_making = [int(el) for el in input().split(', ')]
pizza_making = deque(pizza_making)
number_of_pizzas = deque(number_of_pizzas)
result_pizza = 0
while pizza_making and number_of_pizzas:
    current_make = pizza_making.pop()
    current_pizza = number_of_pizzas.popleft()
    if current_make < current_pizza:
        current_pizza -= current_make
        result_pizza += current_make
        number_of_pizzas.appendleft(current_pizza)
    else:
        result_pizza += current_pizza

if not number_of_pizzas:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {result_pizza}')
    if pizza_making:
        y = [str(i) for i in pizza_making]
        print(f"Employees: {', '.join(y)}")
else:
    print('Not all orders are completed.')
    x = [str(i) for i in number_of_pizzas]
    print(f"Orders left: {', '.join(x)}")


