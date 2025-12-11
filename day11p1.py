from src import Debug, Reader


day = 11
example = False

debug = Debug()

# Day 11 Part 1
debug.disable()

total = 0

with Reader(day, example) as reader:
    graph: dict[str, list[str]] = dict()
    device: str
    attached_line: str
    for device, attached_line in reader.iter_split(": "):
        graph[device] = attached_line.split(" ")

    currents: list[str] = ["you"]
    while currents:
        currents_next: list[str] = list()
        for current in currents:
            devices = graph[current]
            debug(current, devices)
            for device in devices:
                if device == "out":
                    total += 1
                else:
                    currents_next.append(device)
        currents = currents_next

print("Day", day, "part 1:", total)
