import pandas as pd
import numpy as np
#ΤΑ PATHS ΓΑΜΩ ΤΑ PATHS
def main():
    focusarray,unfocusarray=merge_ALL()
    mergedfile=[[0,0,0,0,0,0,0,0,0,0,0,0]]

    for i in focusarray:
        i=i.iloc[:,:].values
        #i=np.delete(i,0,1)
        column_one=np.full((len(i), 1) ,1)
        i= np.column_stack((i, column_one))
        mergedfile=np.concatenate((mergedfile,i),axis=0)

    for i in unfocusarray:
        i=i.iloc[:,:].values
        #i=np.delete(i,0,1)
        column_zero=np.full((len(i), 1), 0)
        i= np.column_stack((i, column_zero))
        mergedfile=np.concatenate((mergedfile,i),axis=0)
    # focused=focused.iloc[:,:].values
    # unfocused=unfocused.iloc[:,:].values
    # focused=np.delete(focused,0,1)
    # unfocused=np.delete(unfocused,0,1)

    

    #create a sizeofarray column  filled with 1 for focused and 0 for unfocused
    # column_one=np.full((len(focused), 1) ,1)
    # column_zero=np.full((len(unfocused), 1), 0)
    

    #add column 1 to focused and column 2 to unfocused
    # focused= np.column_stack((focused, column_one))
    # unfocused= np.column_stack((unfocused, column_zero))

    # merged_file=np.concatenate((focused,unfocused),axis=0)
    mergedfile=pd.DataFrame(mergedfile)

    mergedfile.to_csv("C:/Users/Nikos/Desktop/KNN/mindwavealldata.csv", index=False)
    
    print(len(mergedfile))



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

    focused9=pd.read_csv(path+"subject9_focused.csv")
    unfocused9=pd.read_csv(path+"subject9_relaxed.csv")

    focused10=pd.read_csv(path+"subject10_focused.csv")
    unfocused10=pd.read_csv(path+"subject10_relaxed.csv")

    focusarray=[focused1,focused2,focused3,focused4,focused5,focused6,focused7,focused9,focused10]
    unfocusarray=[unfocused1,unfocused2,unfocused3,unfocused4,unfocused5,unfocused6,unfocused7,unfocused9,unfocused10]
    

    return focusarray,unfocusarray


if __name__ == "__main__":
    main()
