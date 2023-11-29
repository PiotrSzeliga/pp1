movie = {
    "title":"Big Lebowski",
    "year":"1998",
    "actor":{"leading":"Jeff Bridges","supporting":"John Goodman"},
    "oscar":False,
    "genre":"comedy",
    "runtime":"1 godz. 57 min",
    "rating":"10/10"
}
import json
with open("favourite.json ","w") as file:
    json.dump(movie, file, indent=5)