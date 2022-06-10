def get_fibonacci_periodic_serie(n_pos, modulo):
    check = []
    modulus_histo = [0, 1] if n_pos > 0 else [0, 0]
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


def get_last_n_position(n, sequence):
    mod = (n+1) % len(sequence)
    return mod-1


def last_digit_of_fibonaci_squares(n: int):
    sequence = get_fibonacci_periodic_serie(n, 10)
    s_1 = get_last_n_position(n, sequence)
    return (sequence[s_1]*(sequence[s_1]+sequence[s_1-1])) % 10
