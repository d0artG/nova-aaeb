import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, MinMaxScaler


def load_process_breast_cancer_dataset():
    dataset_link = "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data"

    df = pd.read_csv(dataset_link, header=None)

    attributes_names = ['Sample ID', 'Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape',
                        'Marginal Adhesion', 'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin',
                        'Normal Nucleoli', 'Mitoses', 'Diagnosis']

    df.columns = attributes_names

    df.drop_duplicates(inplace=True)

    value_counts = df['Sample ID'].value_counts()
    sample_ids = value_counts[value_counts != 1].index

    sample_index = df[df['Sample ID'].isin(sample_ids)].index

    df.drop(sample_index, inplace=True)

    df.set_index('Sample ID', inplace=True)

    id_miss_values = df['Bare Nuclei'][df['Bare Nuclei'] == "?"].index

    df.drop(id_miss_values, inplace=True)

    X = df[df.columns[:-1]]
    y = df['Diagnosis']

    X_train_bc, X_test_bc, y_train_bc, y_test_bc = train_test_split(X, y, test_size=0.3)

    encoder_bc = LabelEncoder()
    y_train_bc = encoder_bc.fit_transform(y_train_bc)
    y_test_bc = encoder_bc.transform(y_test_bc)

    scaler_bc = MinMaxScaler()
    X_train_bc = scaler_bc.fit_transform(X_train_bc)
    X_test_bc = scaler_bc.transform(X_test_bc)

    return X_train_bc, X_test_bc, y_train_bc, y_test_bc, X.columns
