import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle


def data_split(data, ratio):
    np.random.seed(42)
    shuffled = np.random.permutation(len(data))
    test_set_size = int(len(data) * ratio)
    test_indices = shuffled[:test_set_size]
    train_indices = shuffled[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]


if __name__ == "__main__":
    #reading the data
    df = pd.read_csv('data1.csv')
    
    train, test = data_split(df,0.2)
    
    x_train = train[['fever', 'bodyPain', 'age', 'dryCough', 'runnyNose', 'diffBreath']].to_numpy()
    x_test = test[['fever', 'bodyPain', 'age', 'dryCough', 'runnyNose', 'diffBreath']].to_numpy()

    y_train = train[['infectionProb']].to_numpy().reshape(3200,)
    y_test = test[['infectionProb']].to_numpy().reshape(799,)

    clf = LogisticRegression()
    clf.fit(x_train, y_train)

    # open a file, where you ant to store the data
    file = open('model.pkl', 'wb')

    # dump information to that file
    pickle.dump(clf, file)

    

    file.close()

    

