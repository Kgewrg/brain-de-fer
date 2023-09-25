import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os



# focused
def main():
    path="C:/Users/Dounas P/Desktop/brain-de-fair/python_side/mindwave_dataset/"
    subject="egw"
    pathfoc=path + subject +"_focused.csv"
    pathnotfoc=path + subject +"_relaxed.csv"
    
    foc=getDataForML(pathfoc,0)
    notfoc=getDataForML(pathnotfoc,0)

    focused_avg_atte = np.mean(foc)
    unfocused_avg_atte = np.mean(notfoc)

    print("focused avg: focus %f "%(focused_avg_atte))
    print("unfocused avg: focus %f "%(unfocused_avg_atte))
    plotDataForML(pathfoc,pathnotfoc,120)
    #plotData(pathfoc,pathnotfoc,60,subject)


#returns the selected column from the dataset as a 1-dimensional array and removes doubles
def getData(path,column):
    dataset = pd.read_csv(path)
    dataset=dataset.drop_duplicates()
    dataset=dataset.values
    focus=dataset[:,column]
    return focus

#We use this function when we record with the ML model
def getDataForML(path,column):
    dataset = pd.read_csv(path)
    #dataset=dataset.drop_duplicates()
    dataset=dataset.values
    focus=dataset[:,column]
    return focus

def plotDataForML(focused,notfocused,duration):#duration-->record time (sec)
    ML1=getDataForML(focused,0)
    att1=getDataForML(focused,1)
    timeVector1 = np.linspace(0,duration-1,len(att1))# 1 minute
    ML2=getDataForML(notfocused,0)
    att2=getDataForML(notfocused,1)
    timeVector2 = np.linspace(0,duration-1,len(att2))

    # #Plot the data on the single set of axes
    plt.subplot(211)
    plt.title("Focused")
    plt.plot(timeVector1, ML1, "r", label="ML")
    plt.plot(timeVector1,att1,"m",label="Headset")
    plt.legend()
    plt.grid(True)
    plt.subplot(212)
    plt.title("Relaxed")
    plt.plot(timeVector2, ML2, "r", label="ML")
    plt.plot(timeVector2, att2, "m", label="Headset")
    plt.legend()
    plt.grid(True)
    plt.show()

def plotData(focused,notfocused,duration,name):#duration-->record time (sec)
    att1=getData(focused,0)
    timeVector1 = np.linspace(0,duration-1,len(att1))# 1 minute
    att2=getData(notfocused,0)
    timeVector2 = np.linspace(0,duration-1,len(att2))


    # Plot the data on the single set of axes
    plt.plot(timeVector1,att1, label="Focused")
    plt.plot(timeVector2,att2, label="Relaxed")

    plt.title(name , fontweight="bold")
    plt.grid()
    plt.legend(loc="upper right")
    plt.xlabel("Time (Seconds)", fontweight="bold")
    plt.ylabel("Concentration percentage", fontweight="bold")

    plt.show()

    # plt.subplot(211)
    # plt.title("Focused")
    # plt.plot(timeVector, att1, "b", label="attention")
    # plt.legend()
    # plt.grid(True)
    # timeVector = np.linspace(0,duration-1,len(att2))# 1 minute
    # plt.subplot(212)
    # plt.title("NotFocused")
    # plt.plot(timeVector, att2, "b", label="attention")
    # plt.legend()
    # plt.grid(True)
    # plt.show()





if __name__ == "__main__":
    main()