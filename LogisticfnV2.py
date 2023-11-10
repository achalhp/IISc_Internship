import numpy as np

class MultinomialLogitModel:
    def __init__(self, beta_coefficients, data):
        self.beta_coefficients = beta_coefficients
        self.data = data
        self.utilities = []
        self.P_dict = {}

    def utility(self, beta_coefficients, data_array, index):
        if index < 2:  # For X1 and X2
            return beta_coefficients[f"β0{index+1}"] + beta_coefficients["β1"] * data_array[0,:] + beta_coefficients["β2"] * data_array[1,:]
        else:  # For Sero
            return beta_coefficients["β03"] + beta_coefficients["β1"] * data_array[2,:] + beta_coefficients["β2"] * data_array[2,:]

    def calculate_probabilities(self):
        arrays = [np.array(v) for v in self.data.values()]
        data_array = np.vstack(arrays)
        
        denominator = np.exp(self.utility(self.beta_coefficients, data_array, 0))
        for i in range(1, len(self.data.keys())):
            denominator += np.exp(self.utility(self.beta_coefficients, data_array, i))
        
        for i in range(len(self.data.keys())):
            self.P_dict[f'P{i+1}'] = (np.exp(self.utility(self.beta_coefficients, data_array, i)) / denominator)
        return self.P_dict

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

model = MultinomialLogitModel(beta_coefficients, data)
P_dict = model.calculate_probabilities()

with open('P_dict1.txt', 'w') as file:
    file.write(str(P_dict))
