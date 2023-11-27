import os
import pandas as pd


def predict(src_filename):
    """

    :param src_filename: Data of a new patient in csv format
    :return: Returns the probability of Exitus - Death for this new patient in the next 30 days given the data provided
    """
    new_patient_data = pd.read_csv(src_filename)

    # Put your code here so the probability is returned as prediction
    prediction = None

    return prediction


if __name__ == '__main__':

    print(f"Probability of death in the next 30 days for patient A is: {predict(os.path.join('..', 'data', 'test-data-a.csv'))}")
    print(f"Probability of death in the next 30 days for patient A is: {predict(os.path.join('..', 'data', 'test-data-b.csv'))}")
