""" หั่นขนมปัง """
W, H, M, N = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))

widths = [X[0]]
for i in range(1, M):
    widths.append(X[i] - X[i - 1])
widths.append(W - X[-1])

heights = [Y[0]]
for i in range(1, N):
    heights.append(Y[i] - Y[i - 1])
heights.append(H - Y[-1])

widths.sort(reverse=True)
heights.sort(reverse=True)

max1 = widths[0] * heights[0]
max2 = max(widths[0] * heights[1], widths[1] * heights[0])

print(f"{max1} {max2}")
