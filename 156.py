'''Write a function to convert a tuple of string values to a tuple of integer values.
'''
def tuple_int_str(tuple_str):
    result = tuple((int(x[0]), int(x[1])) for x in tuple_str)
    return result
'''
Standard answer: 
def tuple_int_str(tuple_str):
    result = tuple((int(x[0]), int(x[1])) for x in tuple_str)
    return result
'''
assert tuple_int_str((('333', '33'), ('1416', '55')))==((333, 33), (1416, 55))
assert tuple_int_str((('999', '99'), ('1000', '500')))==((999, 99), (1000, 500))
assert tuple_int_str((('666', '66'), ('1500', '555')))==((666, 66), (1500, 555))
