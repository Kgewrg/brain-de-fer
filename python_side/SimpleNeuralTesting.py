from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
import scipy


def main():
    #datasets_names="C:/Users/Nikos/Desktop/KNN/mindwavealldata.csv"
    datasets_names="C:/Users/Dounas P/Desktop/brain-de-fair/mindwavealldata.csv"
    dataset = pd.read_csv (datasets_names)
    dataset=dataset.iloc[:,:].values
    X=dataset[:,0:4]
    

    y=dataset[:,-1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=None,shuffle=True)  
    array=[] 

    #initialize the KNN classifier
    naiveBayes =  KNeighborsClassifier(n_neighbors=11)
    naiveBayes.fit(X_train,y_train)
    y_pred=naiveBayes.predict(X_test)
    array.append(accuracy_score(y_test,y_pred)*100)
    print("----KNN Complete----")
    #initialize the naiveBayes classifier
    naiveBayes =  GaussianNB()
    naiveBayes.fit(X_train,y_train)
    y_pred=naiveBayes.predict(X_test)
    array.append(accuracy_score(y_test,y_pred)*100)
    print("----Gaussian Bayes Complete----")
    
    #initialize the RandomForest classifier
    naiveBayes = RandomForestClassifier(n_estimators=100, random_state=None)
    naiveBayes.fit(X_train,y_train)
    y_pred=naiveBayes.predict(X_test)
    array.append(accuracy_score(y_test,y_pred)*100)
    print("----Randomforest Complete----")
    
    # #initialize the SVM classifier
    # naiveBayes =svm.SVC(kernel='linear')#SVC->classification SVR->Regression
    # naiveBayes.fit(X_train,y_train)
    # y_pred=naiveBayes.predict(X_test)
    # array.append(accuracy_score(y_test,y_pred)*100)
    # print("----SVM Complete----")

    print(array)


if __name__ == "__main__":
    main()
