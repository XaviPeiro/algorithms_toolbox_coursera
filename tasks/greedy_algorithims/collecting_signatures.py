from typing import Tuple, List


def collecting_signatures(segments: List[Tuple[int, int]]):
    sorted_segments = sorted(segments)
    res = []
    ending_point_curr_segment = sorted_segments.pop(0)[1]
    for segment in sorted_segments:
        if segment[0] <= ending_point_curr_segment:
            ending_point_curr_segment = min(ending_point_curr_segment, segment[1])
        else:
            res.append(ending_point_curr_segment)
            ending_point_curr_segment = segment[1]
    else:
        res.append(ending_point_curr_segment)

    return res


if __name__ == "__main__":
    n_of_segments = int(input())
    segments = []
    try:
        for line in iter(input, ""):
            init_point, end_point = map(int, line.split())
            segments.append((init_point, end_point))
    except EOFError:
        ...

    res = collecting_signatures(segments=segments)
    print(len(res))
    print(res)
