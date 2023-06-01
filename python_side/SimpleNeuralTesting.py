from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
import joblib
import pandas as pd
import numpy as np
import scipy


def main():
    N=11
    #datasets_names="C:/Users/Nikos/Desktop/KNN/mindwavealldata.csv"
    #Train dataset
    datasets_names="C:/Users/Dounas P/Desktop/brain-de-fair/mindwavealldata.csv"
    dataset = pd.read_csv (datasets_names)
    dataset=dataset.iloc[:,:].values
    #Test dataset
    path="C:/Users/Dounas P/Desktop/brain-de-fair/mindwaveTest.csv"
    Test = pd.read_csv(path)
    Test=Test.iloc[:,:].values
    TestX=Test[:,0:N]
    TestY=Test[:,-1]
    
    counter=0
    X=dataset[:,0:N]
    Y=dataset[:,-1]
    X_dataset=[]
    Y_dataset=[]
    X_dataset.append(dataset[0][0:N])
    Y_dataset.append(dataset[0][-1])
    for i in range(len(dataset[:])):
        counter+=1
        if( counter == 60 ):#mia timh kathe 1 deutero ara 60 times to deutero(peripou)
            counter=0
            X_dataset.append(dataset[i][0:N])
            Y_dataset.append(dataset[i][-1])
    
    
    splitMethod(X_dataset,Y_dataset,TestX,TestY)
    #crossVal(X_dataset,Y_dataset)
    
    # rForest = RandomForestClassifier(n_estimators=150, max_depth=10)
    # X_train, test, y_train, train = train_test_split(X_dataset, Y_dataset, test_size=0.000001, random_state=None,shuffle=True)  
    # rForest.fit(X_train,y_train)
    # joblib.dump(rForest,"RandomForestModel.pkl")
    

def crossVal(X_dataset,Y_dataset):
    cross_validator=KFold(n_splits=10,shuffle=True)
    #models-----------------------------------
    KNN =  KNeighborsClassifier(n_neighbors=11)
    naiveBayes =  GaussianNB()
    rForest = RandomForestClassifier(n_estimators=150, max_depth=10)
    #SVM =svm.SVC(cache_size=1000)
    #-----------------------------------------
    scoresKNN = cross_val_score(KNN, X_dataset, Y_dataset, cv=cross_validator)
    scoresNaive = cross_val_score(naiveBayes, X_dataset, Y_dataset, cv=cross_validator)
    scoresForest = cross_val_score(rForest, X_dataset, Y_dataset, cv=cross_validator)
    #scoresSVM = cross_val_score(SVM, X_dataset, Y_dataset, cv=cross_validator)
    # Calculate and print the mean accuracy across all folds
    
    mean_accuracy = scoresKNN.mean()
    #print(f"KNN: {mean_accuracy*100}")
    mean_accuracy = scoresNaive.mean()
    #print(f"Naive: {mean_accuracy*100}")
    mean_accuracy = scoresForest.mean()
    print(f"Forest: {mean_accuracy*100}")
    # mean_accuracy = scoresSVM.mean()
    # print(f"SVM: {mean_accuracy*100}")
    



def splitMethod(X_dataset,Y_dataset,TestX,TestY):
    
    X_train, test, y_train, train = train_test_split(X_dataset, Y_dataset, test_size=0.00001, random_state=None,shuffle=True)  
    X, test, Y,train=train_test_split(TestX, TestY, test_size=0.00001, random_state=None,shuffle=True)  
    array=[] 

    print("hey")

    #initialize the KNN classifier
    KNN =  KNeighborsClassifier(n_neighbors=11)
    KNN.fit(X_train,y_train)
    y_pred=KNN.predict(X)
    array.append(accuracy_score(Y,y_pred)*100)
    print("----KNN Complete----")

    #initialize the naiveBayes classifier
    naiveBayes =  GaussianNB()
    naiveBayes.fit(X_train,y_train)
    joblib.dump(naiveBayes,"naiveBayes.pkl")
    y_pred=naiveBayes.predict(X)
    array.append(accuracy_score(Y,y_pred)*100)
    print("----Gaussian Bayes Complete----")
    
    #initialize the RandomForest classifier
    rForest = RandomForestClassifier(n_estimators=100, max_depth=12)
    rForest.fit(X_train,y_train)
    joblib.dump(rForest,"RandomForestModel.pkl")
    y_pred=rForest.predict(X)
    array.append(accuracy_score(Y,y_pred)*100)
    print("----Randomforest Complete----")
    
    #initialize the SVM classifier
    SVM =svm.SVC(cache_size=1000)#SVC->classification SVR->Regression
    SVM.fit(X_train,y_train)
    joblib.dump(SVM,"SVMModel.pkl")
    y_pred=SVM.predict(X)
    array.append(accuracy_score(Y,y_pred)*100)
    print("----SVM Complete----")

    print(array)


if __name__ == "__main__":
    main()
