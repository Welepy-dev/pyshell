import os

def cdBuiltin(line: str) -> int:
    if line.startswith("~"):
        line = line.replace("~", str(os.getenv("HOME")))
    elif not line.startswith("/"):
        line = os.getcwd() + "/" + line
    if os.path.exists(line):
        os.chdir(line)
    else:
        print("cd: " + line + ": No such file or directory")
    return (0)
