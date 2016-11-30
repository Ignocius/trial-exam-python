# Create a function that takes a list as a parameter,
# and returns a new list with all its element's values doubled.
# It should raise an error if the parameter is not a list.

def list_item_value_doubler(param_list):
    if isinstance(param_list, list):
        returned_list = []
        for i in range(len(param_list)):
            returned_list.append(param_list[i]*2)
        return returned_list
    else:
        raise ValueError("Please feed me with list")
test = [1,2,3,4]
testt = 1
print(list_item_value_doubler(testt))
