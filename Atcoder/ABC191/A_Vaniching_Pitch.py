V, T, S, D = map(int, input().split())


def is_hit_ok(v, t, s, d):
    hitting_time = d / v
    if (hitting_time >= t) & (hitting_time <= s):
        return 'No'
    else:
        return 'Yes'


print(is_hit_ok(V, T, S, D))
