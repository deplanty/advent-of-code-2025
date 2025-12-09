import os
import argparse

import jinja2


def create(day: int):
    # Generate the python files (part 1 and part 2) for the day
    environment = jinja2.Environment(loader=jinja2.FileSystemLoader("templates"))
    template = environment.get_template("day.py")
    create_file(f"day{day:02d}p1.py", text=template.render(day=day, part=1))
    create_file(f"day{day:02d}p2.py", text=template.render(day=day, part=2))

    # Create the input files (full input and example input)
    create_file(f"inputs/day{day:02d}.txt")
    create_file(f"inputs/day{day:02d}ex.txt")


def create_folders():
    if not os.path.exists("inputs/"):
        os.mkdir("inputs/")


def create_file(file, text: str = ""):
    if not os.path.exists(file):
        with open(file, "w", encoding="utf-8") as fid:
            fid.write(text)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("day", nargs="+", type=int, help="The days to create.")

    args = parser.parse_args()

    create_folders()
    for day in args.day:
        create(day)
