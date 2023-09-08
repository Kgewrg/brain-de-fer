from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.model_selection import KFold
from sklearn.neural_network import MLPClassifier
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
import joblib
import pandas as pd
import numpy as np
import scipy


def main():
    #Train dataset
    train="C:/Users/Nikos/Desktop/brain-de-fair/mindwavealldata - copy.csv"
    test="C:/Users/Nikos/Desktop/brain-de-fair/TestData - copy.csv"
    #things
    trainSet = pd.read_csv(train)
    trainSet=trainSet.iloc[:,:].values
    #np.random.shuffle(trainSet)
    N=len(trainSet[0])-1 #the columns of the dataset exlcuding the category
    x_train=trainSet[:,0:N]#original
    y_train=trainSet[:,-1]

    #test dataset
    testSet = pd.read_csv(test)
    testSet=testSet.drop_duplicates()
    testSet=testSet.iloc[:,:].values
    # np.random.shuffle(testSet)
    x_test=testSet[:,0:N]
    y_test=testSet[:,-1]
    
    #crossVal(x_train,y_train)
    coef=linearcoef(x_train,y_train)    
    
    # x_train=newFeatures(coef,x_train)
    # x_test=newFeatures(coef,x_test)
    repeats=1
    ScoreKnn=0
    ScoreNaive=0
    ScoreForest=0
    ScoreMLP=0
    ScoreSVM=0
    for i in range(repeats):
        Knn,Naive,Rforest,Mlp,Svm =crossVal(x_train,y_train)
        ScoreKnn = ScoreKnn + Knn
        ScoreNaive = ScoreNaive + Naive
        ScoreForest = ScoreForest + Rforest
        ScoreMLP = ScoreMLP + Mlp
        ScoreSVM = ScoreSVM + Svm
    print("KNN: ",ScoreKnn * 100 /repeats)
    print("Naive: ",ScoreNaive * 100 /repeats)
    print("Forest: ",ScoreForest * 100 /repeats)
    print("MLP: ",ScoreMLP * 100 /repeats)
    print("SVM: ",ScoreSVM* 100 /repeats)

    # splitMethod(x_train,y_train,x_test,y_test)
    # splitMethod2(x_train,y_train,x_test,y_test)
    #logcoef(x_train,y_train)


def newFeatures(coef,x_train):
    x_train=x_train.astype(np.float32)
    for i in range(len(x_train)):
        for j in range(len(x_train[0])):
            x_train[i][j]=x_train[i][j]*coef[j]
    return x_train

def crossVal(X_dataset,Y_dataset):
    cross_validator=KFold(n_splits=10,shuffle=True)
    #models-----------------------------------
    Knn =  KNeighborsClassifier(n_neighbors=9)
    naiveBayes =  GaussianNB()
    rForest = RandomForestClassifier(n_estimators=100, max_depth=20)
    mlp = MLPClassifier(hidden_layer_sizes=(64), activation='relu', solver='adam',max_iter=600)
    Svm =svm.SVC(cache_size=1000)
    #-----------------------------------------
    scoresKNN = cross_val_score(Knn, X_dataset, Y_dataset, cv=cross_validator)
    scoresNaive = cross_val_score(naiveBayes, X_dataset, Y_dataset, cv=cross_validator)
    scoresForest = cross_val_score(rForest, X_dataset, Y_dataset, cv=cross_validator)
    # scoresMLP = cross_val_score(mlp , X_dataset, Y_dataset, cv=cross_validator)
    scoresSVM = cross_val_score(Svm, X_dataset, Y_dataset, cv=cross_validator)
    #Calculate and print the mean accuracy across all folds
    
    KnnAcc = scoresKNN.mean()
    # print(f"KNN: {KnnAcc*100}")
    NaiveAcc = scoresNaive.mean()
    # print(f"Naive: {NaiveAcc*100}")
    ForestAcc = scoresForest.mean()
    # print(f"Forest: {ForestAcc*100}")
    # MLPAcc = scoresMLP.mean()
    MLPAcc=1
    # print(f"MLP: {mean_accuracy*100}")
    SVMAcc = scoresSVM.mean()
    # print(f"SVM: {mean_accuracy*100}")

    return KnnAcc, NaiveAcc, ForestAcc, MLPAcc, SVMAcc

def logcoef(x_train,y_train):
    reg=LogisticRegression().fit(x_train,y_train)
    coef=reg.coef_
    array=[]
    names=[["attention"], ["meditation"], ["low-alpha"] , ["high alpha"] , ["low-beta"], [" high-beta"] , ["low gamma"], ["mid-gamma"],["raw_value"],["delta"],["theta"]]
    for i in range(len(coef)):
        for j in range(len(coef[0])):
            array.append(coef[i][j])
    for i in range(len(array)):
        print(names[i]," : ",array[i])
    return array

def linearcoef(x_train,y_train):
    reg=LinearRegression().fit(x_train,y_train)
    coef=reg.coef_
    names=["attention","meditation","low-alpha","high alpha","low-beta"," high-beta","low gamma","mid-gamma","raw_value","delta","theta"]
    print(len(coef))
    for i in range(len(coef)):
        print(names[i]," : ",coef[i])
    return coef



def splitMethod2(X_dataset,Y_dataset,x_test,y_test):
    
    x_train, xTest, y_train, yTest = train_test_split(X_dataset, Y_dataset, test_size=20, random_state=None,shuffle=True)  
    array=[] 
    avg="binary"
    
    #initialize the KNN classifier
    KNN =  KNeighborsClassifier(n_neighbors=8)
    KNN.fit(x_train,y_train)
    y_pred=KNN.predict(xTest)
    array.append(accuracy_score(yTest,y_pred)*100)
    print("----KNN Complete----")

    #initialize the ΝaiveBayes classifier
    naiveBayes = GaussianNB()
    naiveBayes.fit(x_train,y_train)
    # joblib.dump(naiveBayes,"naiveBayes.pkl")
    y_pred=naiveBayes.predict(xTest)
    array.append(accuracy_score(yTest,y_pred)*100)
    print("----Gaussian Bayes Complete----")

    #initialize the RandomForest classifier
    rForest = RandomForestClassifier(n_estimators=300, max_depth=7)
    rForest.fit(x_train,y_train)
    # joblib.dump(rForest,"RandomForestModel.pkl")
    y_pred=rForest.predict(xTest)
    array.append(accuracy_score(yTest,y_pred)*100)
    print("----Randomforest Complete----")
    print(array)
    #----test dataset----#

    #---KNN---#
    y_pred=KNN.predict(x_test)
    print("KNN")
    print("Accuracy: ",accuracy_score(y_test,y_pred)*100)
    print("Recall: ",recall_score(y_test,y_pred,average=avg)*100)
    #---NaiveBayes---#
    y_pred=naiveBayes.predict(x_test)
    print("NaiveBayes")
    print("Accuracy: ",accuracy_score(y_test,y_pred)*100)
    print("Recall: ",recall_score(y_test,y_pred,average=avg)*100)
    #---RForest---#
    y_pred=rForest.predict(x_test)
    print("RForest")
    print("Accuracy: ",accuracy_score(y_test,y_pred)*100)
    print("Recall: ",recall_score(y_test,y_pred,average=avg)*100)
    

    #initialize the SVM classifier
    # SVM =svm.SVC(cache_size=1000)#SVC->classification SVR->Regression
    # SVM.fit(x_train,y_train)
    # # joblib.dump(SVM,"SVMModel.pkl")
    # y_pred=SVM.predict(x_test)
    # array.append(accuracy_score(y_test,y_pred)*100)
    # print("----SVM Complete----")

    #initialize the MultiLayerPerceptron classifier
    # mlp = MLPClassifier(hidden_layer_sizes=(64), activation='relu', solver='adam',max_iter=600)
    # mlp.fit(x_train, y_train)
    # y_pred = mlp.predict(x_test)
    # array.append(accuracy_score(y_test, y_pred)*100)
    # print("----Randomforest Complete----")
    # print(array)


if __name__ == "__main__":
    main()
