import glob
import os
import subprocess
import time


def show_time(seconds: float) -> str:
    # Show as ms
    if seconds < 1:
        return f"{int(seconds * 1000)} ms"
    elif seconds <= 60:
        seconds, mseconds = divmod(seconds, 1)
        return f"{int(seconds)} s {int(mseconds * 1000)} ms"
    elif seconds <= 3600:
        minutes, seconds = divmod(seconds, 60)
        return f"{int(minutes)} min {int(seconds)} s"
    else:
        return str(seconds)


if os.path.exists("venv/Scripts/python.exe"):
    cmd_python = "venv/Scripts/python.exe"
else:
    cmd_python = "python"


search = "day*p*.py"
for script in glob.iglob(search):
    start = time.time()
    print(script, "-> ...", end="\r", flush=True)
    p = subprocess.run([cmd_python, script], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    sec = time.time() - start
    if p.returncode == 0:
        print(script, "->", show_time(sec))
    elif p.returncode == 1:
        print(script, "->", "Fail")
