resolution = [500, 500]
framerate = 30


def load(fname):
    settings = {}
    file = open(fname, "r")
    text = file.read()
    lines = text.splitlines()
    for l in lines:
        comp = l.split("=")
        comp = [c.replace(" ", "") for c in comp]
        key = comp[0]
        value = comp[1]
        if key == "resolution":
            try:
                settings[key] = [int(i) for i in value.split("x")]
            except ValueError:
                print(f"Invalid resolution: {value}")
                settings[key] = resolution
        elif key == "fps":
            try:
                settings[key] = int(value)
            except ValueError:
                print(f"Invalid framerate: {value}")
                settings[key] = framerate

    return settings


print(load("settings.cfg"))