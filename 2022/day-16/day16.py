import copy
import numpy as np

def prepare_input(file):
    _dict = {}
    for line in file:
        valve_string, tunnels_string = line.split("; ")
        valve_name = valve_string[6:8]
        valve_flow_rate = int(valve_string.split("=")[1])
        connected_tunnels = tunnels_string.split()[4:]
        connected_tunnels = [t.split(",")[0] for t in connected_tunnels]
        _dict[valve_name] = (valve_flow_rate, connected_tunnels)

    return _dict

def find_all_paths_part_one(caves_dict, current_cave, end_cave, path):
    path = path + [current_cave]

    if current_cave == end_cave:
        return [path]
    if current_cave not in caves_dict:
        return []

    paths = []
    for next_cave in caves_dict[current_cave][1]:
        if next_cave not in path:
            new_paths = find_all_paths_part_one(caves_dict, next_cave, end_cave, path)
            for new_path in new_paths:
                paths.append(new_path)

    return paths

def part_one(_input):
    minutes = 30
    valves_with_flow_rate = []
    for valve, flow_rate_tunnels in _input.items():
        flow_rate, connected_tunnels = flow_rate_tunnels
        if flow_rate != 0:
            valves_with_flow_rate.append(valve)

    curr_valve = "AA"
    optimal_flow_rate = 0
    optimal_steps = 0
    optimal_path = []
    optimal_next_tunnel = ""
    max_flow_rate = 0
    valves_with_flow_rate_copy = copy.deepcopy(valves_with_flow_rate)
    idx = 0
    # while idx != len(valves_with_flow_rate_copy)-1:
    while len(valves_with_flow_rate) != 0:
        # valves_with_flow_rate.pop()
        for v in valves_with_flow_rate:
            paths = find_all_paths_part_one(_input, curr_valve, v, [])
            shortest_path = min(paths, key=len)
            steps = len(shortest_path) - 1
            if minutes - steps - 1 > 0:
                curr_flow_rate = (minutes - steps - 1) * _input[v][0]
                if curr_flow_rate > optimal_flow_rate:
                    optimal_steps = steps + 1
                    optimal_path = shortest_path
                    optimal_next_tunnel = v
                    optimal_flow_rate = curr_flow_rate
        minutes -= optimal_steps
        valves_with_flow_rate.remove(optimal_next_tunnel)
        curr_valve = optimal_next_tunnel
        max_flow_rate += optimal_flow_rate
        optimal_flow_rate = 0
    # while len(valves_with_flow_rate) != 0:
    #     for v in valves_with_flow_rate:
    #         paths = find_all_paths_part_one(_input, curr_valve, v, [])
    #         steps = len(min(paths, key=len))-1
    #         curr_flow_rate = (minutes-steps-1)*_input[v][0]
    #         if curr_flow_rate > optimal_flow_rate:
    #             optimal_steps = steps + 1
    #             optimal_next_tunnel = v
    #             optimal_flow_rate = curr_flow_rate
    #     minutes -= optimal_steps
    #     valves_with_flow_rate.remove(optimal_next_tunnel)
    #     curr_valve = optimal_next_tunnel
    #     max_flow_rate += optimal_flow_rate
    #     optimal_flow_rate = 0

    return max_flow_rate

def part_two(_input):
    return 0

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        _input = prepare_input(f)

    _input_copy = copy.deepcopy(_input)
    answer1 = part_one(_input_copy)
    print("Part one:")
    print("Answer: {}".format(answer1))
    print()
    answer2 = part_two(_input)
    print("Part two:")
    print("Answer: {}".format(answer2))
