from collections import deque

matirials = deque(list(map(int, input().split())))
magick = deque(list(map(int, input().split())))

result_dict = {'Gemstone': 0, 'Porcelain Sculpture': 0, 'Gold': 0, "Diamond Jewellery": 0}
x = False
while matirials and magick:
    current_matirials, current_magick = matirials.pop(), magick.popleft()
    summa = current_matirials + current_magick
    if 100 <= summa <= 199:
        result_dict["Gemstone"] += 1
    elif 200 <= summa <= 299:
        result_dict['Porcelain Sculpture'] += 1
    elif 300 <= summa <= 399:
        result_dict['Gold'] += 1
    elif 400 <= summa <= 499:
        result_dict["Diamond Jewellery"] += 1
    elif summa < 100:
        if summa % 2 == 0:
            current_matirials *= 2
            current_magick *= 3
            if (current_magick + current_matirials) < 100:
                continue
            matirials.append(current_matirials)
            magick.appendleft(current_magick)

        elif summa % 2 != 0:
            if summa * 2 < 100:
                continue
            matirials.append(current_matirials * 2)
            magick.appendleft(current_magick * 2)
    if summa > 499:
        summa /= 2
        if 100 <= summa <= 199:
            result_dict["Gemstone"] += 1
        elif 200 <= summa <= 299:
            result_dict['Porcelain Sculpture'] += 1
        elif 300 <= summa <= 399:
            result_dict['Gold'] += 1
        elif 400 <= summa <= 499:
            result_dict["Diamond Jewellery"] += 1


if result_dict['Gemstone'] > 0 and result_dict['Porcelain Sculpture'] > 0 or result_dict['Gold'] > 0 and result_dict["Diamond Jewellery"] > 0:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")
if matirials:
    print(f"Materials left: {', '.join([str(i) for i in matirials])}")
if magick:
    print(f"Magic left: {', '.join([str(i) for i in magick])}")

filter_dict = sorted(result_dict.items(), key=lambda x: x[0])
for k, v in filter_dict:
    if v > 0:
        print(f"{k}: {v}")