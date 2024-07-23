calls = 0
def count_calls():
    global calls
    calls += 1
    return calls
def string_info(string):
    count_calls()
    numbers = str(len(string))
    top_string = string.upper()
    bottom_string = string.lower()
    tuple_string = (numbers, top_string, bottom_string)
    return tuple_string
def is_contains(string, list_to_search):
    count_calls()
    string = string.upper()
    contains_string = ''.join(list_to_search)
    contains_string = contains_string.upper()

    if string in contains_string:
        return True
    else:
        return False

print(string_info('Kapibara'))
print(string_info("Armageddon"))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)




