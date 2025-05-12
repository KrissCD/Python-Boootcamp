def count_rec1(n):
    if n < 10:
        return 1
    return 1 + count_rec1 (n // 10)

print(count_rec1(3211511))


