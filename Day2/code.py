data = 1

if data == 0:
    f = open("test.py")
else:
    f = open("input.py")

games = {}
output = 0
power_output = 0

for line in f:
    line = line.strip()
    game = {"id":0, "r":0, "g":0, "b":0}
    
    line = line.split(":")
    game["id"] = line[0][5:]
    line = line[1].split(";")
    for a in line:
        a = a.split(',')
        for b in a:
            b = b.split(" ")
            if b[2] == "red":
                if int(b[1]) > game["r"]:
                    game["r"] = int(b[1])
            if b[2] == "blue":
                if int(b[1]) > game["g"]:
                    game["g"] = int(b[1])
            if b[2] == "green":
                if int(b[1]) > game["b"]:
                    game["b"] = int(b[1])
    # print(game)
    if game["r"] < 13:
        if game["b"] < 14:
            if game["g"] < 15:
                output += int(game["id"])
    power = game["r"] * game["g"] * game["b"]
    power_output += power

print("First answer:", output)
print("second answer:", power_output)
