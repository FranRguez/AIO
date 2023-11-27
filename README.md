# Coding exercise for AIO DataScience profile candidates

**This exercise is expected to be finished in less than 4 hours. We don't expect the highest accuracy but just to see how do you approach the ML problem and if you are able to produce ready-to-use code and work in a remote team. So focus on covering all the tasks instead on getting a 0.99 accuracy on just one model. We may review with you the exercise later on, so you can explain your approach and discuss the results.**

Please clone the repo and push into another GitHub repo that you will share with us.

You are provided with a dataset containing some clinical information about patients that you can find at:

`./data/dataset.csv`

The columns represent lab and other clinical values obtained during a routine patient visit. Each row is a different patient.

The column `time` represent the time (in days) from the time when the routine patient visit occurs and the next contact or information about that patient. The column `DEATH_EVENT` represents if the patient died on that time (1) or if the patient was alive on that time (0).

For example for a patient with `time=20` and `DEATH_EVENT=1` it means the patient died 20 days after the routine visit. For a patient with `time=90` and `DEATH_EVENT=0` it means the patient was alive 90 days after the routine visit.

## Task 1 (expected max time 1 hour):

Create a brief descriptive notebook of the dataset that you could share with a physician (non-IT audience), do not spend more than 1 hour for this task. Save it as `./notebooks/descriptive.ipynb`

## Task 2 (expected max time 1,5 hours):

Train a predictive model, based on some "classical" Machine Learning approach, able to predict if a patient will die in the next 30 days after routine visit using the variables collected during that routine visit. Use a notebook saved as `./notebooks/ml-training.ipynb` that could be replicated to retrain the model.

Persist the model in a file named `ml-model.model` inside the `models` folder.

Include in the `./notebooks/ml-training.ipynb` notebook a section with the validation metrics you would use to validate the model.

## Task 3 (expected max time 1 hour): 

Train a predictive model based on some Deep Learning approach (using Keras/Tensorflow/Pytorch) able to predict if a patient will die in the next 90 days after routine visit using CPU. Create a notebook saved as `./notebooks/dl-training.ipynb` that could be replicated to retrain the model.

Persist the model in a file named `dl-model.model` inside the `models` folder.

Include in the `./notebooks/dl-training.ipynb` notebook a section with the validation metrics you would use to validate the model.

## Task 4 (expected max time 0.5 hours):

Edit the file `./scr/predict.py` with the required code so when run from the terminal as `python predict.py` the script will load the `ml-model.model` and print the prediction in a terminal.

Note: If your ml-model.model works well the `./tests/test.py` should pass both assertions but this is not mandatory.




