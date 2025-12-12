from copy import deepcopy

from src import Debug, Reader


day = 11
example = False

debug = Debug()

# Day 11 Part 2
debug.disable()

total = 0

with Reader(day, example) as reader:
    graph: dict[str, list[str]] = dict()
    device: str
    attached_line: str
    for device, attached_line in reader.iter_split(": "):
        graph[device] = attached_line.split(" ")

    # [(current, fft seen, dac seen)]
    limit = 12
    paths: list[tuple[str, bool, bool]] = [("svr", False, False)]
    while paths and limit > 0:
        paths_next: list[tuple[str, bool, bool]] = list()
        for current, fft, dac in paths:
            devices = graph[current]
            debug(current, devices)
            for device in devices:
                if device == "out":
                    if fft and dac:
                        total += 1
                else:
                    if not fft and device == "fft":
                        fft = True
                    if not dac and device == "dac":
                        dac = True
                    paths_next.append((device, fft, dac))
        paths = paths_next
        limit -= 1

print("Day", day, "part 2:", total)


import sys

sys.exit(1)
