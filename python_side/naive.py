from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
import scipy


def main():
    datasets_names="C:/Users/Nikos/Desktop/KNN/mindwavealldata.csv"
    dataset = pd.read_csv (datasets_names)
    dataset=dataset.iloc[:,:].values
    X=dataset[:,0:4]
    

    y=dataset[:,-1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=None,shuffle=True)  
    array=[] 
    #initialize the naiveBayes classifier
    naiveBayes =  KNeighborsClassifier(n_neighbors=11)
    naiveBayes.fit(X_train,y_train)
    y_pred=naiveBayes.predict(X_test)
    array.append(accuracy_score(y_test,y_pred)*100)
    print("----KNN Complete----")

    naiveBayes =  GaussianNB()
    naiveBayes.fit(X_train,y_train)
    y_pred=naiveBayes.predict(X_test)
    array.append(accuracy_score(y_test,y_pred)*100)
    print("----Gaussian Bayes Complete----")
    

    naiveBayes = RandomForestClassifier(n_estimators=100, random_state=None)
    naiveBayes.fit(X_train,y_train)
    y_pred=naiveBayes.predict(X_test)
    array.append(accuracy_score(y_test,y_pred)*100)
    print("----RandomforestComplete----")
    
    print(array)

def bandPassFilter(signal, lowcut, highpass):
    sfreq = 256.0 #Sampling freq

    nyq = 0.5 * sfreq
    low = lowcut / nyq
    high = highpass / nyq

    order = 4

    b, a = scipy.signal.butter(order, [low, high], 'bandpass', analog=False)
    y = scipy.signal.filtfilt(b, a, signal, axis=0)

    return y


if __name__ == "__main__":
    main()
