def maximizeTheCuts(self, n, x, y, z):
    seg = [-1] * (n + 1)
    seg[0] = 0

    for i in range(1, n + 1):
        if i >= x and seg[i - x] != -1:
            seg[i] = max(seg[i], seg[i - x] + 1)
        if i >= y and seg[i - y] != -1:
            seg[i] = max(seg[i], seg[i - y] + 1)
        if i >= z and seg[i - z] != -1:
            seg[i] = max(seg[i], seg[i - z] + 1)

    if seg[n] != -1:
        return seg[n]
    else:
        return 0
