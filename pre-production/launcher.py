import tkinter as tk
import os
import subprocess
import time

gamePath = os.path.join(os.path.dirname(__file__), "brain_de_fair_unity.exe")
bridgePath = os.path.join(os.path.dirname(__file__), "PythonScripts")
dataFilePath = os.path.join(os.path.dirname(__file__), "brain_de_fair_unity_Data", "data.csv")

runningBridgePath = ""
selectedBridge = ""
bridgeProcess = 0

PVE = "PVE.py"
PVP = "PVP.py"
PVP_demo = "PVP_demo.py"

bridgeArray = [PVE, PVP, PVP_demo]


def writeToTextbox(text: str):
    """ Clear the texbox and writes to it the new text """

    textbox.delete("0", tk.END)
    textbox.insert(tk.END, text)




def checkIfConnectorISRunning():
    running = False
    old_leftAttention = old_rightAttention = leftAttention = rightAttention = 0
    with open(dataFilePath, "r") as csv:
        values = csv.readline().split(',')
        old_leftAttention = values[0]
        old_rightAttention = values[1]

    time.sleep(1.2)

    with open(dataFilePath, "r") as csv:
        values = csv.readline().split(',')
        leftAttention = values[0]
        rightAttention = values[1]

    if (old_leftAttention != leftAttention) or (old_rightAttention != rightAttention):
        running = True



    return running    



    
def on_closing():
    
    if bridgeProcess != 0:
        bridgeProcess.kill() # Kill the subprocess

    root.destroy()  # Destroy the Tkinter window



def startGameButton():
    global bridgeProcess, selectedBridge
    
    try:
        print("Starting Connector: " + selectedBridge)
        writeToTextbox("Starting Connector: " + selectedBridge)
        if bridgeProcess != 0:
            bridgeProcess.kill() 
                
        bridgeProcess = subprocess.Popen(["python", runningBridgePath], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        time.sleep(2)

        writeToTextbox("Starting Game")

        os.startfile(gamePath)
        
        label.config(text="Button 1 Clicked - Application Launched")

    except Exception as e:
        label.config(text=f"Error: {str(e)}")

def startConnectorButton():
    global bridgeProcess

    # Kill the previus Bridge if it is already running
    if bridgeProcess != 0:
        bridgeProcess.kill() 
    
    label.config(text="Launch Connector")
    bridgeProcess = subprocess.Popen(["python", runningBridgePath], stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def button3_click():
    if (not checkIfConnectorISRunning()):
        writeToTextbox("Connector is NOT running")
    else:
        writeToTextbox("Connector is running")




def on_dropdown_change(*args):
    global runningBridgePath, selectedBridge

    selected_option = dropdown_var.get()
    option_index = options.index(selected_option)
    
    label.config(text=f"Selected Option: {selected_option}")
    selectedBridge = bridgeArray[option_index]
    runningBridgePath = os.path.join(bridgePath, bridgeArray[option_index])
    


# Create the main window
root = tk.Tk()
root.title("Brain de fer Launcer")

# Create a label
label = tk.Label(root, text="Press a button.")
label.pack(pady=10)

# Register the function to be called when the window is closed
root.protocol("WM_DELETE_WINDOW", on_closing)


# Create a dropdown menu
options = ["Pkayer VS Bot", "Player VS Player", "Demo mode"]
dropdown_var = tk.StringVar(root)
dropdown_var.set(options[0])  # Set the default option

runningBridgePath = os.path.join(bridgePath, bridgeArray[0]) # set the default game mode too
selectedBridge = bridgeArray[0]


dropdown = tk.OptionMenu(root, dropdown_var, *options)
dropdown.pack(pady=10)
dropdown_var.trace_add("write", on_dropdown_change)


# Create three larger buttons
button1 = tk.Button(root, text="Start Game", command=startGameButton, width=15, height=2)
button1.pack(pady=5)

button2 = tk.Button(root, text="Launch Connector", command=startConnectorButton, width=15, height=2)
button2.pack(pady=5)

button3 = tk.Button(root, text="Check Connector", command=button3_click, width=15, height=2)
button3.pack(pady=5)

# Create a textbox
textbox = tk.Entry(root, width=100)
textbox.pack(pady=10)


# Start the Tkinter event loop
root.mainloop()
