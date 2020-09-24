import pickle

data_filename='E:\deep-speaker\deep-speaker-data\cache\\full_inputs.pkl'


data = pickle.load(open(data_filename, 'rb'))
print(data)
kx_train, ky_train, kx_test, ky_test, categorical_speakers = data_to_keras(data)