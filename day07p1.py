from src import Debug, Reader, Index

day = 7

debug = Debug()


# Day 7 Part 1

total = 0

with Reader(day, example=False) as reader:
    field = reader.get_field("")

    # Get the input source
    index: Index = Index(0, field[0].index("S"))
    index.set(field, ".")

    # Process the beam
    beams: set[Index] = {index}
    seen: set[Index] = set()
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
                    if beam.W not in seen:
                        tmp_beams.add(beam.W)
                        seen.add(beam.W)
                    if beam.E not in seen:
                        tmp_beams.add(beam.E)
                        seen.add(beam.E)
                    total += 1
        beams = tmp_beams

print("Day", day, "part 1:", total)
