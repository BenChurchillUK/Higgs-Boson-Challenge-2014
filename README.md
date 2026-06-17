# Higgs Boson Machine Learning Challenge

## Project Overview

The challenge was to identify positive signals for the Higgs Boson from the provided ATLAS data. This repository serves to explore key techniques, such as using Machine Learning for data analysis.

## Dataset

The official data was used, as stored by CERN. The relevant csv file is called in src/data_processing.py or found at https://opendata.cern.ch/record/328.

The dataset holds records for 818,238 events, with 29 features. The target (Higgs Boson candidates) are separated in "Label" by signals ("s") and background/noise ("b").

## Repository Structure

/notebooks -- Runs the data investigations, machine learning models, evaluation and validation processes.  
// 01_dataset_overview.ipynb -- Explores the structure of the dataset.  
// 02_feature_investigation.ipynb -- Explores the statistical relevance of each feature in the dataset.  
// 03_baseline_logistic_regression_model.ipynb -- Builds and evaluates a logistic regression model based on the features from notebook 02.  
// 04_baseline_random_forest_model.ipynb -- Builds and evaluates a random forest classifier based on the features from notebook 02.  
// 05_baseline_validation.ipynb -- Runs a cross validation of both the logistic regression model and random forest classifier from notebooks 03 and 04.  

/src -- Organises functions to ensure the results are reproducible.  
//data_processing.py -- Has functions for pulling the dataset and preprossessing the data.  
//feature_investigation.py -- Functions for testing the features.  
//training_functions.py -- Functions for splitting and scaling the data.  
//evaluation_metrics.py -- For functions testing a single run of a model.  
//validation_metrics.py -- For cross validation functions and attaining performance scores.  

requirements.txt -- Lists python libraries used.

## Methodology

Firstly, the data was explored in notebook 01. The structure was assessed through functions such as describe() and info(). Understanding the features, the data type, and how many null values was important for avoiding errors.

Further looking into the features, notebook 02 compares the distribution of signal and background events for each distribution. The aim was to discover which features had a distinguishable difference between candidates and non-candidates. The four features selected, PRI_met, DER_pt_tot, DER_mass_jet_jet, and DER_pt_h, had little to no overlap between signals and noise, and were selected for this reason.

The first two models were Logistic Regression and Random Forest Classifier. These models were defined as baseline, to test whether the features had an impact on separating Higgs Boson candidates. Logistic Regression was selected for testing whether there was a linear relation between the features and identifying candidates; and Random Forest Classifier was selected to test if there was a non-linear relation. Then, notebook_05 ran stratified K-Folds to test the consistency of the model by breaking the dataset down, producing multiple training and test data.

## Results

The initial baseline models focused on statistically relevant features, through a Logistic Regression and Random Forest Classifier models. Upon validation, both models attained a mean accuracy of 68%, however the Random Forest scored marginally better when considering the Receiver-Operating Characteristic and Area Under Curve (ROC-AUC) and Logistic Regression performed considerably better when considering the logarithmic loss. This could suggest that both models are making different probability estimates despite achieving similar accuracy scores.

|   | Accuracy Score | ROC-AUC | Log Loss (Negative) |
|---|---|---|---|
|Logistic Regression|0.681078 ± 0.001023|0.678342 ± 0.002043|-0.603889 ± 0.000745|
|Random Forest Classifier|0.680245 ± 0.000577|0.692452 ± 0.001662|-0.886763 ± 0.007772|

## The Models

Due to the nature of the provided dataset; supervised, classification models were selected.

Logistic Regression: A regression model that estimates the probability of an event based off of previous data.

Random Forest Classifier: A model that combines multiple decision trees to predict the probability of an event.

## Future Work

Future models to explore: Neural Networks, Extreme Gradient Boosting, K-Nearest-Neighbour, Support Vector Machine Algorithm

## References

Atlas doc.
