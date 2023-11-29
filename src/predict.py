import os
import pandas as pd
import joblib
os.chdir('C:/Users/user/TrabajoAIO/AIO/')

def predict(src_filename):

    rfmodel = joblib.load(os.path.join('models/ml-model2.model'))
    """
    :param src_filename: Data of a new patient in csv format
    :return: Returns the probability of Exitus - Death for this new patient in the next 30 days given the data provided
    """
    new_patient_data = pd.read_csv(os.path.join('data',src_filename))

    # Put your code here so the probability is returned as prediction
    prediction = rfmodel.predict_proba(new_patient_data.values)
    prediction = prediction[:,1]
    return prediction

if __name__ == '__main__':

    print(f"Probability of death in the next 30 days for patient A is: {predict(os.path.join('..', 'data', 'test-data-a.csv'))}")
    print(f"Probability of death in the next 30 days for patient B is: {predict(os.path.join('..', 'data', 'test-data-b.csv'))}")
