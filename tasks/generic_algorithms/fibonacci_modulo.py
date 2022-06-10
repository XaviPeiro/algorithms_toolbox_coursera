def get_fibonacci_periodic_serie(n_pos, modulo):
    check = []
    modulus_histo = [0, 1]
    res = {0: 0, 1: 1}
    for i in range(2, n_pos+1):

        if i <= 1:
            res[i] = i
        else:
            res[i] = res[i-1] + res[i-2]

        modulus_histo.append(res[i] % modulo)

        if modulus_histo[-2:] == [0, 1]:
            check = modulus_histo[:-2]
        elif len(check) > 0:
            if modulus_histo[0:len(check)] == check:
                break
    else:
        return modulus_histo

    return check


def get_fibonacci_modulo(n_pos, modulo):
    periodic_serie = get_fibonacci_periodic_serie(n_pos=n_pos, modulo=modulo)
    remaining = n_pos % len(periodic_serie)
    return periodic_serie[remaining]

a, b = map(lambda x: int(x), input().split())
res = get_fibonacci_modulo(a, b)
print(res)
