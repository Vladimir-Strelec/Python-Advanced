def flights (*args):
    line_dict = {}
    for i in range(0, len(args)+1, 2):
        if not args[i] == 'Finish' and args[i] not in line_dict:
            line_dict[args[i]] = 0
        if not args[i] == 'Finish' and args[i] in line_dict:
            line_dict[args[i]] += args[i+1]
        else:
            break
    return line_dict


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))