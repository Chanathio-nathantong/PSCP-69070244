""" Point Sorting """
def solve():
    """ solve """
    T = int(input())
    all_results = []

    for _ in range(T):
        N = int(input())
        points = []
        for i in range(N):
            i += 1
            x, y = map(int, input().split())
            points.append((x, y))
        points.sort(key=lambda p: (p[0] + p[1], -p[1]))

        for x, y in points:
            all_results.append(f"{x} {y}")

    print('\n'.join(all_results))

solve()
