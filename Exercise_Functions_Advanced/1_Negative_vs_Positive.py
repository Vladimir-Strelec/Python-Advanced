def check(num_numbers):
    negatives = [i for i in num_bers if i < 0]
    positives = [i for i in num_bers if i >= 0]
    return negatives, positives


num_bers = list(map(int, input().split()))
n, p = check(num_bers)

print(sum(n))
print(sum(p))
if abs(sum(n)) > sum(p):
    print('The negatives are stronger than the positives')
else:
    print('The positives are stronger than the negatives')