import pandas as pd
import numpy as np

def load_HAR_features_data():
    
    feature_names = np.loadtxt('Data/UCI HAR Dataset/features.txt', dtype=str)[:, 1].flatten()

    X_train_values = np.loadtxt('Data/UCI HAR Dataset/train/X_train.txt')
    X_train = pd.DataFrame(X_train_values, columns=feature_names)
    X_train = X_train[[x for x in feature_names if 'Mag' in x]]
    
    X_test_values = np.loadtxt('Data/UCI HAR Dataset/test/X_test.txt')
    X_test = pd.DataFrame(X_test_values, columns=feature_names)
    X_test = X_test[[x for x in feature_names if 'Mag' in x]]
    
    y_train = np.loadtxt('Data/UCI HAR Dataset/train/y_train.txt')
    y_test = np.loadtxt('Data/UCI HAR Dataset/test/y_test.txt')
    
    subjects_train = np.loadtxt('Data/UCI HAR Dataset/train/subject_train.txt')
    subjects_test = np.loadtxt('Data/UCI HAR Dataset/test/subject_test.txt')
    
    return X_train, y_train, X_test, y_test, subjects_train, subjects_test