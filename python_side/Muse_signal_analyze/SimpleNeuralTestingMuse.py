from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.neural_network import MLPClassifier
import joblib
import pandas as pd
import numpy as np
import scipy
from tqdm import tqdm


def main():
    # dataset
    datasets_names="C:/Users/Nikos/Desktop/brain-de-fair/mindwavealldata.csv"
    dataset = pd.read_csv(datasets_names)
    dataset=dataset.iloc[:,:].values
    DatasetX=dataset[:,:-1]
    DatasetY=dataset[:,-1]
    
    splitMethod(DatasetX,DatasetY)
    #crossVal(DatasetX,DatasetY)
    

def crossVal(X_dataset,Y_dataset):
    cross_validator=KFold(n_splits=10,shuffle=False)
    #models-----------------------------------
    KNN =  KNeighborsClassifier(n_neighbors=11)
    naiveBayes =  GaussianNB()
    rForest = RandomForestClassifier(n_estimators=100, max_depth=12)
    SVM =svm.SVC(cache_size=1000)
    MLP = MLPClassifier(hidden_layer_sizes=(64), activation='relu', solver='adam',max_iter=600)
    #-----------------------------------------
    scoresKNN = cross_val_score(KNN, X_dataset, Y_dataset, cv=cross_validator)
    scoresNaive = cross_val_score(naiveBayes, X_dataset, Y_dataset, cv=cross_validator)
    scoresForest = cross_val_score(rForest, X_dataset, Y_dataset, cv=cross_validator)
    scoresSVM = cross_val_score(SVM, X_dataset, Y_dataset, cv=cross_validator)
    scoresMLP = cross_val_score(MLP, X_dataset, Y_dataset, cv=cross_validator)
    # Calculate and print the mean accuracy across all folds
    
    mean_accuracy = scoresKNN.mean()
    print(f"KNN: {mean_accuracy*100}")
    mean_accuracy = scoresNaive.mean()
    print(f"Naive: {mean_accuracy*100}")
    mean_accuracy = scoresForest.mean()
    print(f"Forest: {mean_accuracy*100}")
    mean_accuracy = scoresSVM.mean()
    print(f"SVM: {mean_accuracy*100}")
    mean_accuracy = scoresMLP.mean()
    print(f"MLP: {mean_accuracy*100}")
    
def splitMethod(X_dataset,Y_dataset):
    
    x_train, x_test, y_train, y_test = train_test_split(X_dataset, Y_dataset, test_size=20, random_state=None,shuffle=True)  
    array=[] 

    #initialize the KNN classifier
    KNN =  KNeighborsClassifier(n_neighbors=11)
    KNN.fit(x_train,y_train)
    y_pred=KNN.predict(x_test)
    array.append(accuracy_score(y_test,y_pred)*100)
    print("----KNN Complete----")

    #initialize the ΝaiveBayes classifier
    naiveBayes =  GaussianNB()
    naiveBayes.fit(x_train,y_train)
    # joblib.dump(naiveBayes,"naiveBayes.pkl")
    y_pred=naiveBayes.predict(x_test)
    array.append(accuracy_score(y_test,y_pred)*100)
    print("----Gaussian Bayes Complete----")
    
    #initialize the RandomForest classifier
    rForest = RandomForestClassifier(n_estimators=100, max_depth=12)
    rForest.fit(x_train,y_train)
    # joblib.dump(rForest,"RandomForestModel.pkl")
    y_pred=rForest.predict(x_test)
    array.append(accuracy_score(y_test,y_pred)*100)
    print("----Randomforest Complete----")
    print(array)

    #initialize the SVM classifier
    SVM =svm.SVC(cache_size=1000)#SVC->classification SVR->Regression
    SVM.fit(x_train,y_train)
    # joblib.dump(SVM,"SVMModel.pkl")
    y_pred=SVM.predict(x_test)
    array.append(accuracy_score(y_test,y_pred)*100)
    print("----SVM Complete----")

    #initialize the MultiLayerPerceptron classifier
    mlp = MLPClassifier(hidden_layer_sizes=(64), activation='relu', solver='adam',max_iter=600)
    mlp.fit(x_train, y_train)
    y_pred = mlp.predict(x_test)
    array.append(accuracy_score(y_test, y_pred)*100)
    print("----Randomforest Complete----")
    print(array)


if __name__ == "__main__":
    main()
