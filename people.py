from flask import make_response, abort

# JSON Data to serve with our API
PEOPLE = {
    "ricky": {
        "fname": "ricky",
        "lname": "ponting",
        "age": "11",
        "favorite_color": "pink",
    },
    "chris": {
        "fname": "chris",
        "lname": "gayle",
        "age": "29",
        "favorite_color": "green",
    },
    "shane": {
        "fname": "shane",
        "lname": "warne",
        "age": "33",
        "favorite_color": "white",
    },
}


def get_all():
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]


def get_one(fname):
    if fname in PEOPLE:
        person = PEOPLE.get(fname)
    else:
        abort(
            404, "Person with first name {fname} not found".format(fname=fname)
        )
    return person



def add(person):
    fname = person.get("fname", None)
    lname = person.get("lname", None)
    age = person.get("age", None)
    favorite_color = person.get("favorite_color", None)

    if fname not in PEOPLE and fname is not None:
        PEOPLE[fname] = {
            "fname": fname,
            "lname": lname,
            "age": age,
            "favorite_color": favorite_color
        }
        return make_response(
            "Record {fname} successfully created".format(fname=fname), 201
        )
    else:
        abort(
            406,
            "Peron with first name {fname} already exists".format(fname=fname),
        )



def update(fname, person):
    if fname in PEOPLE:
        PEOPLE[fname]["fname"] = person.get("fname")
        PEOPLE[fname]["lname"] = person.get("lname")
        PEOPLE[fname]["age"] = person.get("age")
        PEOPLE[fname]["favorite_color"] = person.get("favorite_color")
        return PEOPLE[fname]
    else:
        abort(
            404, "Person with first name {fname} not found".format(fname=fname)
        )


def delete(fname):
    if fname in PEOPLE:
        del PEOPLE[fname]
        return make_response(
            "{fname} successfully deleted".format(fname=fname), 200
        )
    else:
        abort(
            404, "Person with first name {fname} not found".format(fname=fname)
        )
