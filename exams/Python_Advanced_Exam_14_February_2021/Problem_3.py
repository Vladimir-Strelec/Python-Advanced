def stock_availability(inventory, command, *args):
        if command == 'delivery':
            return inventory + list(args)
        if not args:
            return inventory[1:]
        if isinstance(args[0], int):
            count = int(args[0])
            return inventory[count:]
        sold_items = set(args)
        return [i for i in inventory if i not in sold_items]


