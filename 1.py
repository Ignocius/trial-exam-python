# Create a function that takes a list as a parameter,
# and returns a new list with all its element's values doubled.
# It should raise an error if the parameter is not a list.

def list_data_doubler(data_list):
    if isinstance(data_list,list):
        reference_list = []
        for i in data_list:
            reference_list.append(i*2)
        return reference_list
    else:
        raise TypeError("Please give me a list for parameter!")

lista = [1,2,3,4]
print(list_data_doubler(lista))
