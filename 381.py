'''Write a function to sort a list of lists by a given index of the inner list.
'''
def index_on_inner_list(list_data, index_no):
    result = sorted(list_data, key=lambda x: x[index_no])
    return result
'''
Standard answer: 
from operator import itemgetter
def index_on_inner_list(list_data, index_no):
    result = sorted(list_data, key=itemgetter(index_no))
    return result
'''
assert index_on_inner_list([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] ,0)==[('Beau Turnbull', 94, 98), ('Brady Kent', 97, 96), ('Greyson Fulton', 98, 99), ('Wyatt Knott', 91, 94)]
assert index_on_inner_list([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] ,1)==[('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98), ('Brady Kent', 97, 96), ('Greyson Fulton', 98, 99)]
assert index_on_inner_list([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] ,2)==[('Wyatt Knott', 91, 94), ('Brady Kent', 97, 96), ('Beau Turnbull', 94, 98), ('Greyson Fulton', 98, 99)]
