import numpy as np

beta_coefficients = {
    "β01": 0.1,
    "β1": 0.5,
    "β2": 0.5,
    "β02": 1,
    "β03": 0
}

data = {
'X1': [2, 3, 5, 7, 1, 8, 4, 5, 6, 7],
'X2': [1, 5, 3, 8, 2, 7, 5, 9, 4, 2],
'Sero': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}


#function defining utilities

def V1(beta_coefficients, data_array):
    return beta_coefficients["β01"] + beta_coefficients["β1"] * data_array[0,:] + beta_coefficients["β2"] * data_array[1,:]

def V2(beta_coefficients, data_array):
    return beta_coefficients["β02"] + beta_coefficients["β1"] * data_array[0,:] + beta_coefficients["β2"] * data_array[1,:]

def V3(beta_coefficients, data_array):
    return beta_coefficients["β03"] + beta_coefficients["β1"] * data_array[2,:] + beta_coefficients["β2"] * data_array[2,:]

#Creating utilities function list to add new functions here, for expansion.
functions = [V1,V2,V3]   

#Utilities can accomidate more functions and data when added
utilities = [functions[i] for i in range(len(data.keys()))]


#function definition

def calculate_probabilities(parameters, data, utilities):
    #Error handling 1: To catch mismatched dimensions b/w parameters and data
    if len(parameters) != len(data) + 2:
        raise ValueError("Error: The number of beta coefficients must be one more than the number of lists in data.")
    
    # Get the lists from the dictionary and convert them to numpy arrays
    arrays = [np.array(v) for v in data.values()]

    # Error handling 2: Check if all arrays have the same length
    if all(len(arr) == len(arrays[0]) for arr in arrays):
        # Stack the arrays vertically to create a 2D array
        data_array = np.vstack(arrays)
    else:
        print("Error: All lists in the data dictionary must have the same length.")


    # same denominator for all, so define it
    denominator = np.exp(utilities[0](parameters, data_array))
    #loop to accomidate expansion in utility function
    for i in range(1,len(utilities)):
        denominator += np.exp(utilities[i](parameters, data_array))
    
    #Probality calculation and dictionary to add values
    P_dict = {}
    for i in range(len(utilities)):
        P_dict['P{}'.format(i+1)] = (np.exp(utilities[i](parameters, data_array)) / denominator)
    return P_dict
P_dict = calculate_probabilities(beta_coefficients, data, utilities)

#P_dict is saved as dictionary with arrays
with open('P_dict.txt', 'w') as file:
    file.write(str(P_dict))


# Below code saves P_dict as list, instead of np.arrays. numpy-arrays are fast.

# with open('P_dict.txt', 'w') as file:
#     for key in P_dict.keys():
#         line = str(key) + ': ' + ', '.join(map(str, P_dict[key])) + '\n'
#         file.write(line)
