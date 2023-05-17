import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os



# focused
def main():
    
    pathfoc="C:/Users/Nikos/Desktop/brain-de-fair/python_side/mindwave_dataset/subject10_focused.csv"
    pathnotfoc="C:/Users/Nikos/Desktop/brain-de-fair/python_side/mindwave_dataset/subject10_relaxed.csv"
    foc=getData(pathfoc,0)
    notfoc=getData(pathnotfoc,0)

    #plotData(pathfoc,pathnotfoc,60)

    focused_avg_atte = np.mean(foc)
    
    unfocused_avg_atte = np.mean(notfoc)

    print("focused avg: focus %f "%(focused_avg_atte))
    print("unfocused avg: focus %f "%(unfocused_avg_atte))

#returns the selected column from the dataset as a 1-dimensional array and removes doubles
def getData(path,column):
    dataset = pd.read_csv(path)
    dataset=dataset.values

    rowspersecond=int(len(dataset[:])/60)

    focused_attention=[]
    focused_attention.append(dataset[0][0])
    for i in range(len(dataset[:])):
        if( i % rowspersecond == 0):
            focused_attention.append(dataset[i][column])
    return focused_attention

def plotData(focused,notfocused,duration):#duration-->record time (sec)
    att1=getData(focused,0)
    timeVector = np.linspace(0,duration-1,len(att1))# 1 minute
    att2=getData(notfocused,0)
   
    plt.subplot(211)
    plt.title("Focused")
    plt.plot(timeVector, att1, "b", label="attention")
    plt.legend()
    plt.grid(True)
    timeVector = np.linspace(0,duration-1,len(att2))# 1 minute
    plt.subplot(212)
    plt.title("NotFocused")
    plt.plot(timeVector, att2, "b", label="attention")
    plt.legend()
    plt.grid(True)
    plt.show()





if __name__ == "__main__":
    main()