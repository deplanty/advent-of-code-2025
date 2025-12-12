from src import Debug, Reader, Index
from src import draw_table


day = 7

debug = Debug()


# Day 7 Part 2

with Reader(day, example=True) as reader:
    field = reader.get_field("")

    # Get the input source
    index: Index = Index(0, field[0].index("S"))
    index.set(field, ".")

    # Process the beam
    beams: set[Index] = {index}
    seen: set[Index] = set()
    splitters: list[Index] = list()
    loop = True
    while len(beams) > 0:
        tmp_beams: set[Index] = set()

        for beam in beams:
            match beam.get(field):
                case ".":
                    if not beam.S.is_in(field):
                        continue
                    if beam.S not in seen:
                        tmp_beams.add(beam.S)
                        seen.add(beam.S)
                case "^":
                    splitters.append(beam)
                    if beam.W not in seen:
                        tmp_beams.add(beam.W)
                        seen.add(beam.W)
                    if beam.E not in seen:
                        tmp_beams.add(beam.E)
                        seen.add(beam.E)
        beams = tmp_beams

total = len(splitters)
print(splitters)
draw_table(field, {"^": "#80aae1"})

print("Day", day, "part 2:", total * 2)

import sys

sys.exit(1)
