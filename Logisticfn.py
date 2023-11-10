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

x1 = np.array(data["X1"])
x2 = np.array(data["X2"])
sero = np.array(data["Sero"])


def V1(beta_coefficients, data):
    x1 = np.array(data["X1"])
    x2 = np.array(data["X2"])
    sero = np.array(data["Sero"])
    return beta_coefficients["β01"] + beta_coefficients["β1"] * x1 + beta_coefficients["β2"] * x2

def V2(beta_coefficients, data):
    x1 = np.array(data["X1"])
    x2 = np.array(data["X2"])
    sero = np.array(data["Sero"])
    return beta_coefficients["β02"] + beta_coefficients["β1"] * x1 + beta_coefficients["β2"] * x2

def V3(beta_coefficients, data):
    x1 = np.array(data["X1"])
    x2 = np.array(data["X2"])
    sero = np.array(data["Sero"])
    return beta_coefficients["β03"] + beta_coefficients["β1"] * sero + beta_coefficients["β2"] * sero

#Creating utilities function list.

functions = [V1(beta_coefficients, data),V2(beta_coefficients, data),V3(beta_coefficients, data)]

utilities = [functions[i] for i in range(len(data.keys()))]

def calculate_probabilities(parameters, data, utilities):
    denominator = np.exp(utilities[0])
    for i in range(1,len(utilities)):
        denominator += np.exp(utilities[i])
    P_dict = {}
    for i in range(len(utilities)):
        P_dict['P{}'.format(i+1)] = (np.exp(utilities[i]) / denominator)
    return P_dict
P_dict = calculate_probabilities(beta_coefficients, data, utilities)

with open('P_dict.txt', 'w') as file:
    file.write(str(P_dict))


# I'm avoiding for-loops to make it fast. Hence P_dict is outputted as is.

# with open('P_dict.txt', 'w') as file:
#     for key in P_dict.keys():
#         line = str(key) + ': ' + ', '.join(map(str, P_dict[key])) + '\n'
#         file.write(line)
