from typing import List


def is_reachable(origin, destination, distance) -> bool:
    return destination <= (origin + distance)


def less_travels_fuel_car(destination: int, max_travel_distance: int, n_stops: int, stops: List[int]) -> int:
    number_of_travels: int = 0
    next_position: int = 0
    current_position: int = 0
    safe_place = 0
    stops.append(destination)
    for stop in stops:
        if is_reachable(origin=current_position, destination=stop, distance=max_travel_distance):
            safe_place = stop
        elif stop != 0:
            current_position = safe_place
            number_of_travels += 1
            if not is_reachable(origin=current_position, destination=stop, distance=max_travel_distance):
                return -1
            else:
                safe_place = stop

        # if stop < (current_position + max_travel_distance):
        #     next_position = stop
        # elif stop == (current_position + max_travel_distance):
        #     next_position = current_position = stop
        #     number_of_travels += 1
        # elif next_position != current_position:
        #     number_of_travels += 1
        #     current_position = next_position
        # else:
        #     return -1

    return number_of_travels


if __name__ == "__main__":
    destination = int(input())
    max_travel_distance = int(input())
    n_of_stops = int(input())
    stops = list(map(int, input().split()))
    res = less_travels_fuel_car(
        destination=destination,
        max_travel_distance=max_travel_distance,
        n_stops=n_of_stops,
        stops=stops
    )
    print(res)
