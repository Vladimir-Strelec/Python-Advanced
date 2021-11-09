from datetime import datetime, timedelta
from collections import deque

data = input().split(';')
time = datetime.strptime(input(), '%H:%M:%S')

robots = []
available_robots = deque([])
queue_products = deque([])

for element in data:
    robot_data = element.split('-')
    robot = {}
    robot['name'] = robot_data[0]
    robot['processing_time'] = int(robot_data[1])
    robot['available_at'] = time
    robots.append(robot)
    available_robots.append(robot)

product = input()
while not product =='End':
    queue_products.append(product)
    product = input()


while len(queue_products) > 0:
    time = time + timedelta(seconds=1)
    if available_robots:
        current_robot = available_robots.popleft()
        print(f"{current_robot['name']} - {queue_products.popleft()} [{time.strftime('%H:%M:%S')}]")
        current_robot['available_at'] = time + timedelta(seconds=current_robot['processing_time'])
    else:
        for r in robots:
            if time >= r['available_at']:
                available_robots.append(r)
        if not available_robots:
            queue_products.rotate(-1)
        else:
            current_robot = available_robots.popleft()
            print(f"{current_robot['name']} - {queue_products.popleft()} [{time.strftime('%H:%M:%S')}]")
            current_robot['available_at'] = time + timedelta(seconds=current_robot['processing_time'])
