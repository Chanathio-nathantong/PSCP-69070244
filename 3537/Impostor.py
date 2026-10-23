""" Impostor """
players = {}
while True:
    line = input().strip()
    if line == "Start":
        break

    clean_line = line.replace("{", "").replace("}", "").replace('"', '').strip()
    name, role = clean_line.split(":")
    players[name.strip()] = role.strip()

dead = {}

while True:
    line = input().strip()
    if line == "End":
        break

    if line in players:
        dead[line] = players.pop(line)
impostor_count = list(players.values()).count("Impostor")

print(f"{impostor_count} Impostor Remains")
print("***Alive***")
for name in sorted(players.keys()):
    print(f"{name} : {players[name]}")

print("***Dead***")
for name in sorted(dead.keys()):
    print(f"{name} : {dead[name]}")
