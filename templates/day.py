from src import Debug, Reader


day = {{ day }}
example = True

debug = Debug()

# Day {{ day }} Part {{ part }}
# debug.disable()

total = 0

with Reader(day, example) as reader:
    pass

print("Day", day, "part {{ part }}:", total)
