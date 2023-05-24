import matplotlib.pyplot as plt
import numpy as np


FOCUSED_FN = "C:\\Users\\tsarosDesktop\\Documents\\repositories\\brain-de-fair\\python_side\\Muse_signal_analyze\\muse_dataset\\subject5_focused.csv"
UNFOCUSED_FN = "C:\\Users\\tsarosDesktop\\Documents\\repositories\\brain-de-fair\\python_side\\Muse_signal_analyze\\muse_dataset\\subject10_relaxed.csv"



focused = np.loadtxt(FOCUSED_FN, delimiter=",", dtype=str)
unfocused = np.loadtxt(UNFOCUSED_FN, delimiter=",", dtype=str)
focused = focused[2:].astype(float)
unfocused = unfocused[2:].astype(float)


fig = plt.figure()

focused = np.array(focused)
plt.scatter(focused[:,1], focused[:,4], marker="o", color="r")

unfocused = np.array(unfocused)
plt.scatter(unfocused[:,1], unfocused[:,4], marker="^", color="b")

plt.show()