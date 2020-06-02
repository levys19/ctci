import heapq
"""
flight time:
you are given a list of flight start and end times.
Determine the max amount of airplanes in the air at the same time
Examples:
Start:2, End:5
Start:3, End:7
Start:8, End:9
return 2
"""
#brute force
def brute_flight_time(flight_schedule: [])-> int:
    start_time = min([flight[0] for flight in flight_schedule])
    end_time = max(flight[1] for flight in flight_schedule)
    air_time = {key: 0 for key in range(start_time, end_time)}

    for flights in flight_schedule:
        for time in range(flights[0], flights[1]):
            air_time[time] += 1
    return max(air_time.values())

print(brute_flight_time([(2,5),(3,7),(8,9)]))


def flight_time(flight_schedule: []) -> int:
    flight_schedule = sorted(flight_schedule)
    max_flight = 0
    active = 0
    in_air = []
    for flight in flight_schedule:
        active += 1
        while in_air:
            if flight[0] > in_air[0]:
                heapq.heappop(in_air)
                active -= 1
            else:
                break
        heapq.heappush(in_air, flight[1])
        if active > max_flight:
            max_flight = active
    return max_flight

print(flight_time([(2,5),(3,7),(8,9)]))
