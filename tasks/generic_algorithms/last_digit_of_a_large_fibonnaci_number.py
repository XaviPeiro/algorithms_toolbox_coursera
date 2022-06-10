def get_fibonacci_periodic_serie(n_pos, modulo) -> list:
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


def calc_last_digit_of_n(n, sequence):
    res = (n+1)//len(sequence) * sum(sequence)

    mod = (n+1) % len(sequence)
    if mod > 0:
        res += sum(sequence[:mod])
    return res


def last_digit_of_a_large_fibonnaci_number(x: int) -> int:
    sequence = get_fibonacci_periodic_serie(x, 10)
    res = calc_last_digit_of_n(x, sequence)
    return res % 10
