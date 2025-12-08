from dataclasses import dataclass
from itertools import combinations
import math

from src import Debug, Reader


@dataclass
class Vector3:
    x: int = 0
    y: int = 0
    z: int = 0

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z))

    def distance_to(self, point: "Vector3") -> float:
        return math.sqrt(
            (self.x - point.x) ** 2 + (self.y - point.y) ** 2 + (self.z - point.z) ** 2
        )


day = 8
example = False

debug = Debug()

# Day 8 Part 1
debug.disable()

# Get all the points
with Reader(day, example) as reader:
    boxes: list[Vector3] = [Vector3(x, y, z) for x, y, z in reader.iter_split(",", int)]

# Calculate the distance between all the points
distances: dict[Vector3, dict[Vector3, float]] = dict()
for box_start in boxes:
    for box_end in boxes:
        if box_start == box_end:
            continue

        if box_start not in distances:
            distances[box_start] = dict()
        distances[box_start][box_end] = box_start.distance_to(box_end)

# Sort the connexions by distance
connexions = sorted(combinations(boxes, 2), key=lambda t: distances[t[0]][t[1]])

# Create all the circuits from the connexions
last_connexion: tuple[Vector3, Vector3] = (boxes[0], boxes[1])
circuits: list[set[Vector3]] = list()
for i in range(len(connexions)):
    box1, box2 = connexions[i]

    debug(box1, box2)

    # Find if the boxes can connect to an existing circuit
    circuit_index_box1: int = -1
    circuit_index_box2: int = -1
    for index, circuit in enumerate(circuits):
        if box1 in circuit:
            circuit_index_box1 = index
        if box2 in circuit:
            circuit_index_box2 = index

    # If box1 and box2 are not in a circuit
    # Then they create their own circuit
    if circuit_index_box1 == -1 and circuit_index_box2 == -1:
        debug("New circuit")
        circuits.append({box1, box2})
    # If box1 and box2 are in the same circuit
    # Then do nothing
    elif circuit_index_box1 == circuit_index_box2:
        debug("Same circuit")
        pass
    # If box1 is in a different circuit than box2
    # Then merge the two circuits
    elif circuit_index_box1 >= 0 and circuit_index_box2 >= 0:
        debug("Merge circuits")
        circuit_union: set = set()
        circuit_union.update(circuits.pop(max(circuit_index_box1, circuit_index_box2)))
        circuit_union.update(circuits.pop(min(circuit_index_box1, circuit_index_box2)))
        circuits.append(circuit_union)
        last_connexion = (box1, box2)
    # If only box1 is in a circuit
    # Then add box2 to that circuit
    elif circuit_index_box1 >= 0:
        debug("Add box2")
        circuits[circuit_index_box1].add(box2)
        last_connexion = (box1, box2)
    # If only box2 is in a circuit
    # Then add box1 to that circuit
    elif circuit_index_box2 >= 0:
        debug("Add box1")
        circuits[circuit_index_box2].add(box1)
        last_connexion = (box1, box2)

    debug("Circuits:", *circuits, sep="\n  - ")
    debug()

debug("Last connexion:", last_connexion)
total = last_connexion[0].x * last_connexion[1].x

print("Day", day, "part 2:", total)
