def s(n):
    seen = set()
    steps = 0
    while True:
        s_str = f"{n:04d}"
        if len(set(s_str)) == 1:
            return "NE"
        largest = int("".join(sorted(s_str, reverse=True)))
        smallest = int("".join(sorted(s_str)))
        result = largest - smallest
        steps += 1
        if result == 6174:
            return steps
        if result < 1000:
            return "NE"
        if result in seen:
            return "NE"
        seen.add(result)
        n = result

n = int(input())
brojevi = [int(input()) for _ in range(n)]

rezultati = [str(s(broj)) for broj in brojevi]

print("\n".join(rezultati))
