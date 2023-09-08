import pandas as pd
import numpy as np
#ΤΑ PATHS ΓΑΜΩ ΤΑ PATHS
def main():
    mindwaveMerge()
    #museMerge()
    

def mindwaveMerge():#sunarthsh pou enonei ola ta datasets tou mindwave kai diagrafei diplotipes times
    focusarray,unfocusarray=merge_ALL()
    mergedfile=[[0,0,0,0,0,0,0,0,0,0,0,0]]
    
    for i in focusarray:
        i=i.iloc[:,:].values
        column_one=np.full((len(i), 1) ,1)#dimiourgw ena pinaka me 1 oso to length tou prwtou dataset
        i= np.column_stack((i, column_one))#to kollaw ston kurio pinaka
        mergedfile=np.concatenate((mergedfile,i),axis=0)#prosthetw to epejergasmeno dataset sto kurio arxeio

    for i in unfocusarray:
        i=i.iloc[:,:].values
        column_zero=np.full((len(i), 1), 0)
        i= np.column_stack((i, column_zero))
        mergedfile=np.concatenate((mergedfile,i),axis=0)
    
    mergedfile=pd.DataFrame(mergedfile)
    mergedfile=mergedfile.drop_duplicates()
    mergedfile.to_csv("C:/Users/Nikos/Desktop/brain-de-fair/mindwavealldata.csv", index=False)
    print(len(mergedfile))

def removeDoubles(dataset):#diagrafei tis sunexomenes diples times mindwave
    startlength=len(dataset)
    arraytemp=[]
    temp=10000

    for i in range(len(dataset)-1,-1,-1):
        if dataset[i][8] == temp :
            arraytemp.append(1)
            dataset=np.delete(dataset,i, axis=0)
            continue
        temp=dataset[i][8]

    endlength=len(dataset)
    print(endlength)
    print("ελεγχος μεγεθους πινακα ",startlength-len(arraytemp))
    return dataset

def museMerge():
    focusarray,unfocusarray=merge_ALL()
    mergedfile=[[0,0,0,0,0]]
    
    for i in focusarray:
        i=i.iloc[:,:].values
        i=np.delete(i,0,1)#diagrafw thn sthlh tou xronou
        column_one=np.full((len(i), 1) ,1)#dimiourgw ena pinaka me 1 oso to length tou prwtou dataset
        i= np.column_stack((i, column_one))#to kollaw ston kurio pinaka
        mergedfile=np.concatenate((mergedfile,i),axis=0)#prosthetw to epejergasmeno dataset sto kurio arxeio

    for i in unfocusarray:
        i=i.iloc[:,:].values
        i=np.delete(i,0,1)#diagrafw thn sthlh tou xronou
        column_zero=np.full((len(i), 1), 0)
        i= np.column_stack((i, column_zero))
        mergedfile=np.concatenate((mergedfile,i),axis=0)
    

    mergedfile=removeNoise(mergedfile)#PROSOXH 
    mergedfile=pd.DataFrame(mergedfile)
    mergedfile.to_csv("C:/Users/Dounas P/Desktop/brain-de-fair/MuseALL.csv", index=False)
    print(len(mergedfile))

def removeNoise(dataset):#diagrafw opoia seira exei estw kai mia timh megaluterh tou 100 h tou -100
    startlength=len(dataset)
    arraytemp=[]
    for i in range(len(dataset)-1,-1,-1):
        for j in dataset[i]:
            if j>100 or j<-100 :
                arraytemp.append(1)
                dataset=np.delete(dataset,i, axis=0)
                break
    endlength=len(dataset)
    print(endlength)
    print("ελεγχος μεγεθους πινακα ",startlength-len(arraytemp))
    return dataset

def merge_ALL():
    path="C:/Users/Nikos/Desktop/brain-de-fair/python_side/mindwave_dataset/"
    focused1=pd.read_csv(path+"subject1_focused.csv")
    unfocused1=pd.read_csv(path+"subject1_relaxed.csv")
    
    focused2=pd.read_csv(path+"subject2_focused.csv")
    unfocused2=pd.read_csv(path+"subject2_relaxed.csv")

    focused3=pd.read_csv(path+"subject3_focused.csv")
    unfocused3=pd.read_csv(path+"subject3_relaxed.csv")

    focused4=pd.read_csv(path+"subject4_focused.csv")
    unfocused4=pd.read_csv(path+"subject4_relaxed.csv")

    focused5=pd.read_csv(path+"subject5_focused.csv")
    unfocused5=pd.read_csv(path+"subject5_relaxed.csv")

    focused6=pd.read_csv(path+"subject6_focused.csv")
    unfocused6=pd.read_csv(path+"subject6_relaxed.csv")

    focused7=pd.read_csv(path+"subject7_focused.csv")
    unfocused7=pd.read_csv(path+"subject7_relaxed.csv")

    focused8=pd.read_csv(path+"subject8_focused.csv")
    unfocused8=pd.read_csv(path+"subject8_relaxed.csv")

    focused9=pd.read_csv(path+"subject9_focused.csv")
    unfocused9=pd.read_csv(path+"subject9_relaxed.csv")

    focused10=pd.read_csv(path+"subject10_focused.csv")
    unfocused10=pd.read_csv(path+"subject10_relaxed.csv")

    unfocused11=pd.read_csv(path+"noise.csv")

    focusarray=[focused1,focused2,focused3,focused4,focused5,focused6,focused7,focused8,focused9,focused10]
    unfocusarray=[unfocused1,unfocused2,unfocused3,unfocused4,unfocused5,unfocused6,unfocused8,unfocused7,unfocused9,unfocused10,unfocused11]
    

    return focusarray,unfocusarray


if __name__ == "__main__":
    main()
