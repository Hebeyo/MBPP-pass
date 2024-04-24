'''Write a function that gives profit amount if the given amount has profit else return none.
'''
def profit_amount(actual_cost,sale_amount):
  if actual_cost > sale_amount:
    return actual_cost - sale_amount
  else:
    return None
'''
Standard answer: 
def profit_amount(actual_cost,sale_amount): 
 if(actual_cost > sale_amount):
    amount = actual_cost - sale_amount
    return amount
 else:
    return None
'''
assert profit_amount(1500,1200)==300
assert profit_amount(100,200)==None
assert profit_amount(2000,5000)==None
