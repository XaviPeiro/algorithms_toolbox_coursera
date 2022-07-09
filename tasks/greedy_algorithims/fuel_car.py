from typing import List


def less_travels_fuel_car(destination: int, max_travel_distance: int, stops: List[int]) -> int:
    number_of_travels: int = 0
    next_position: int = 0
    current_position: int = 0

    stops.append(destination)
    for stop in stops:
        if stop - (current_position + max_travel_distance) <= 0:
            next_position = stop
        elif next_position != current_position:
            number_of_travels += 1
            current_position = next_position
        else:
            return -1

    return number_of_travels


if __name__ == "__main__":
    destination = int(input())
    max_travel_distance = int(input())
    n_of_stops = int(input())
    stops = list(map(int, input().split()))
    res = less_travels_fuel_car(destination=destination, max_travel_distance=max_travel_distance, stops=stops)
    print(res)
