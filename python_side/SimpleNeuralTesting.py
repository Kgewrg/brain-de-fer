from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.model_selection import KFold
from sklearn.neural_network import MLPClassifier
from sklearn import preprocessing

import joblib
import pandas as pd
import numpy as np
import scipy


def main():
    N=11#the columns of the dataset exlcuding the category
    #datasets_names="C:/Users/Nikos/Desktop/KNN/mindwavealldata.csv"

    #Train dataset
    datasets_names="C:/Users/Nikos/Desktop/brain-de-fair/MindwaveDataset.csv"
    dataset = pd.read_csv (datasets_names)
    dataset=dataset.iloc[:,:].values
    np.random.shuffle(dataset)
    #attributes and category of train dataset 
    x_train_or=dataset[:,0:N]#original
    y_train_or=dataset[:,-1]

    #Test dataset
    path="C:/Users/Nikos/Desktop/brain-de-fair/python_side/mindwaveTest.csv"
    Test = pd.read_csv(path)
    Test=Test.iloc[:,:].values
    np.random.shuffle(Test)
    #attributes and category of test dataset 
    TestX=Test[:,0:N]
    TestY=Test[:,-1]
    
    counter=0
    new_dataset=[]
    new_dataset.append(dataset[0][:])

    x_train=[]
    y_train=[]
    #creating a new dataset with 1 value per 60 of the original trying to remove doubles
    for i in range(0,len(dataset),60):
            new_dataset.append(dataset[i][:])
    new_dataset=np.array(new_dataset)
    x_train = new_dataset[:,:-1]
    y_train = new_dataset[:,-1]
    
    crossVal(x_train,y_train)
    splitMethod(x_train_or,y_train_or,TestX,TestY)
    

def crossVal(X_dataset,Y_dataset):
    cross_validator=KFold(n_splits=10,shuffle=False)

    #models-----------------------------------
    KNN =  KNeighborsClassifier(n_neighbors=11)
    naiveBayes =  GaussianNB()
    rForest = RandomForestClassifier(n_estimators=150, max_depth=10)
    mlp = MLPClassifier(hidden_layer_sizes=(64), activation='relu', solver='adam',max_iter=600)
    SVM =svm.SVC(cache_size=1000)
    #-----------------------------------------
    scoresKNN = cross_val_score(KNN, X_dataset, Y_dataset, cv=cross_validator)
    scoresNaive = cross_val_score(naiveBayes, X_dataset, Y_dataset, cv=cross_validator)
    scoresForest = cross_val_score(rForest, X_dataset, Y_dataset, cv=cross_validator)
    scoresMLP = cross_val_score(mlp , X_dataset, Y_dataset, cv=cross_validator)
    scoresSVM = cross_val_score(SVM, X_dataset, Y_dataset, cv=cross_validator)
    #Calculate and print the mean accuracy across all folds
    
    mean_accuracy = scoresKNN.mean()
    print(f"KNN: {mean_accuracy*100}")
    mean_accuracy = scoresNaive.mean()
    print(f"Naive: {mean_accuracy*100}")
    mean_accuracy = scoresForest.mean()
    print(f"Forest: {mean_accuracy*100}")
    mean_accuracy = scoresMLP.mean()
    print(f"MLP: {mean_accuracy*100}")
    mean_accuracy = scoresSVM.mean()
    print(f"SVM: {mean_accuracy*100}")
    



def splitMethod(x_train,y_train,x_test,y_test):
    #initialize the KNN classifier
    KNN =  KNeighborsClassifier(n_neighbors=11)
    KNN.fit(x_train,y_train)
    y_pred=KNN.predict(x_test)
    print("----KNN Complete----")
    print(accuracy_score(y_test,y_pred)*100)

    #initialize the naiveBayes classifier
    naiveBayes =  GaussianNB()
    naiveBayes.fit(x_train,y_train)
    # joblib.dump(naiveBayes,"naiveBayes.pkl")
    y_pred=naiveBayes.predict(x_test)
    print("\n----Gaussian Bayes Complete----")
    print(accuracy_score(y_test,y_pred)*100)
    
    #initialize the RandomForest classifier
    rForest = RandomForestClassifier(n_estimators=100, max_depth=12)
    rForest.fit(x_train,y_train)
    # joblib.dump(rForest,"RandomForestModel.pkl")
    y_pred=rForest.predict(x_test)
    print("\n----Randomforest Complete----")
    print(accuracy_score(y_test,y_pred)*100)
    
    # #initialize the SVM classifier
    # SVM =svm.SVC(cache_size=1000)#SVC->classification SVR->Regression
    # SVM.fit(x_train,y_train)
    # # joblib.dump(SVM,"SVMModel.pkl")
    # y_pred=SVM.predict(X)
    # array.append(accuracy_score(Y,y_pred)*100)
    # print("\n----SVM Complete----")
    
    mlp = MLPClassifier(hidden_layer_sizes=(64), activation='relu', solver='adam',max_iter=1200)
    mlp.fit(x_train, y_train)
    y_pred = mlp.predict(x_test)
    print("\n----MLP Complete----")
    print(accuracy_score(y_test,y_pred)*100)
    



if __name__ == "__main__":
    main()
