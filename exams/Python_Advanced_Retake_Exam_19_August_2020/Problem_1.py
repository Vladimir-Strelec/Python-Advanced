from collections import deque
line_customer = deque([int(el) for el in input().split(', ')])
line_taxi = [int(el) for el in input().split(', ')]


time = 0

while line_taxi and line_customer:
    current_taxi = line_taxi.pop()
    current_customer = line_customer.popleft()
    if current_taxi >= current_customer:
        time += current_customer
    elif current_taxi < current_customer:
        line_customer.appendleft(current_customer)

if not line_customer:
    print('All customers were driven to their destinations')
    print(f'Total time: {time} minutes')

else:
    print('Not all customers were driven to their destinations')
    print(f'Customers left: {", ".join([str(i) for i in line_customer])}')