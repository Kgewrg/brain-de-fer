import tkinter as tk
from tkinter import Scrollbar
import os
import sys
import subprocess
import time
import serial.tools.list_ports

sys.path.append(os.path.abspath("C:\\Users\\tsarosDesktop\Documents\\repositories\\brain-de-fair\pre-production\PythonScripts"))
import subPrograms


gamePath = os.path.join(os.path.dirname(__file__), "brain_de_fair_unity.exe")
bridgePath = os.path.join(os.path.dirname(__file__), "PythonScripts")
dataFilePath = os.path.join(os.path.dirname(__file__), "brain_de_fair_unity_Data", "data.csv")


runningBridgePath = ""
selectedBridge = ""
bridgeProcess = 0

PVE = "PVE.py"
PVP = "PVP.py"
PVP_demo = "PVP_demo.py"

PORT1 = PORT2 = ""

bridgeArray = [PVE, PVP, PVP_demo]


def writeToTextBox(text: str):
    timestamp = "["+ time.strftime("%H:%M:%S") + "]: "
    text = timestamp + text + "\n"

    logBox.config(state="normal") # enables the widget to write
    logBox.insert(tk.END, text)
    logBox.config(state="disabled") # disbles is afterwards
    logBox.see(tk.END)
    root.update()


def checkIfConnectorISRunning():
    """Διαβάζει μια φορά, περιμένει λίγο, διαβάζει δεύτερη, 
        αν είναι διαφοερτικά αυτά που διάβασε τότε επιστρέφει true"""
    running = False
    old_leftAttention = old_rightAttention = leftAttention = rightAttention = 0
    with open(dataFilePath, "r") as csv:
        values = csv.readline().split(',')

        # Μπορει να μην έχει γραφτεί τίποτα μέσα στο αρχείο
        if (values[0] == ""):
            return running  
        
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
        writeToTextBox("Starting Connector: " + runningBridgePath)
        if bridgeProcess != 0:
            bridgeProcess.kill() 

        print ("Running with ports:", PORT1, PORT2)
        bridgeProcess = subprocess.Popen(["python", runningBridgePath, PORT1, PORT2], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        


        time.sleep(2)

        writeToTextBox("Starting Game")

        os.startfile(gamePath)

    except Exception as e:
        writeToTextBox(f"Error: {str(e)}")
        return 


def startConnectorButton():
    global bridgeProcess
    writeToTextBox("Laucning connector: " + runningBridgePath)
    # Kill the previus Bridge if it is already running
    if bridgeProcess != 0:
        bridgeProcess.kill() 
    
    print ("Running with ports:", PORT1, PORT2)
    bridgeProcess = subprocess.Popen(["python", runningBridgePath, PORT1, PORT2], stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def checkConnectorButton():
    if (not checkIfConnectorISRunning()):
        writeToTextBox("Connector is NOT running")
    else:
        writeToTextBox("Connector is running")


def on_dropdown_change(*args):
    
    global runningBridgePath, selectedBridge

    selected_option = dropdown_var.get()
    option_index = options.index(selected_option)
    
    selectedBridge = bridgeArray[option_index]
    runningBridgePath = os.path.join(bridgePath, bridgeArray[option_index])
    
def setSelectedPort(*args):
    global selectedPort
    selectedPort = portDropdownVar.get()

def setPORT_1(*args):
    global PORT1
    PORT1 = port1Var.get()

def setPORT_2(*args):
    global PORT2
    PORT2 = port2Var.get()

    
def testSinglePort():
    global selectedPort

    writeToTextBox("Checking port: "+ selectedPort + ", this process may take some time")
    
    subPrograms.checkPort(selectedPort, writeToTextBox)
    # TODO: κάπως πρέπει να στηθεί το output, μάλλον πάσσαρε και το logbox
    # η να περαστεί η ίδια writeToTextBox

def testAllPorts(ports: []):

    writeToTextBox("Availale ports: [" + " ".join(ports) + "]")
    writeToTextBox("This process takes some time, please wait until you see a result on this text box\nthe launcer may appear crashed, it's fine.")

    for port in ports:
        writeToTextBox("Checking port: " + port)
        result = subPrograms.checkPort(port, writeToTextBox)
       
        if result == 0:
            writeToTextBox("Port found! " + port)
            return port
    
    writeToTextBox("None of the available ports are correct, try to restart the luncher \nif the problem continiues restart the headsets and bluetooth")




# Create the main window
root = tk.Tk()
root.title("Brain de fer Launcer")


# Register the function to be called when the window is closed
root.protocol("WM_DELETE_WINDOW", on_closing)


# Create a dropdown menu
options = ["Player VS Bot", "Player VS Player", "Demo mode"]
dropdown_var = tk.StringVar(root)
dropdown_var.set(options[0])  # Set the default option

runningBridgePath = os.path.join(bridgePath, bridgeArray[0]) # set the default game mode too
selectedBridge = bridgeArray[0]


dropdown = tk.OptionMenu(root, dropdown_var, *options)
dropdown.grid(row=0, column=0, pady=10)
dropdown_var.trace_add("write", on_dropdown_change)


# Create three larger buttons
button1 = tk.Button(root, text="Start Game", command=startGameButton, width=15, height=2)
button1.grid(row=1, column=0, pady=10)

button2 = tk.Button(root, text="Launch Connector", command=startConnectorButton, width=15, height=2)
button2.grid(row=2, column=0, pady=10)

button3 = tk.Button(root, text="Check Connector", command=checkConnectorButton, width=15, height=2)
button3.grid(row=3, column=0, pady=10)


# Test single port button
testSingleButton = tk.Button(root, text="Test port", command=testSinglePort, width=15, height=2)
testSingleButton.grid(row=1, column=1, pady=10)

# Test all ports button
testAllButton = tk.Button(root, text="Test all ports", command=lambda: testAllPorts(portsOptions), width=15, height=2)
testAllButton.grid(row=2, column=1, pady=10)

# Create a Text widget for the log
logBox = tk.Text(root, width=50, height=10, wrap=tk.WORD)
logBox.grid(row=6, column=0, columnspan=2, pady=10)
logBox.config()



# Search για τις comports
portsOptions = [port.name for port in serial.tools.list_ports.comports()]
portDropdownVar = tk.StringVar(root)
if  (len(portsOptions) == 0):
    portsOptions = ["None", "None"]
    writeToTextBox("There are no available devices to connect to")
    # Θα μπορούσε εδώ να κάνει disable το PVE και PVP 
    
portDropdownVar.set(portsOptions[0])
selectedPort  = portsOptions[0]

# port drowpDown
dropdown = tk.OptionMenu(root, portDropdownVar, *portsOptions, command=setSelectedPort)
dropdown.grid(row=0, column=1, pady=10)
# dropdown_var.trace_add("write", onPortDropdownChange)


# device1 dropdown label
device1_lable = tk.Label(root, text="Left EEG port")
device1_lable.grid(row=4, column=0)

# device1 dropdown
port1Var = tk.StringVar(root)
port1Var.set(portsOptions[0])
PORT1 = portsOptions[0]
device1_dd  = tk.OptionMenu(root, port1Var, *portsOptions, command=setPORT_1)
device1_dd.grid(row=5, column=0, pady=10)

# device2 dropdown label
device2_lable = tk.Label(root, text="Right EEG port")
device2_lable.grid(row=4, column=1)

# device2 dropdown
port2Var = tk.StringVar(root)
port2Var.set(portsOptions[1])
PORT2 = portsOptions[1]
device2_dd  = tk.OptionMenu(root, port2Var, *portsOptions, command=setPORT_2)
device2_dd.grid(row=5, column=1, pady=10)

# Start the Tkinter event loop
root.mainloop()
