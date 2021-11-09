words = input()
print('\n'.join(sorted(set([f"{i}: {words.count(i)} time/s" for i in words]))))