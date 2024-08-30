calls = 0
string = "How much"


def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    count_calls()
    return string.upper() in [s.upper() for s in list_to_search]


print(string_info("AbraKadabRa"))
print(string_info("URBAN"))
print(is_contains("URbAN", ["ur", "RBAN", "ban"]))
print(is_contains("chemodAN", ["chem", "oda", "chemodan"]))
print(calls)


