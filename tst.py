import matplotlib.pyplot as plt
import numpy as np


# focused
data = np.loadtxt("focused.csv", delimiter=",", dtype=str)
titles = data[0]
data = data[1:-1]
data = data.astype(float)

poor = data[1:-1, 0]
raw = data[1:-1, 1]
focused_attention = data[1:-1, 2]
focused_meditation = data[1:-1, 3] 

timeVector = [i for i in range(len(raw))]




plt.subplot(211)
plt.title("focused")

plt.plot(timeVector, poor, "b", label="poor")
plt.plot(timeVector, raw, "r", label="raw")
plt.plot(timeVector, focused_attention, "g", label="attention")
plt.plot(timeVector, focused_meditation, "m", label="meditation")
plt.legend()

data = np.loadtxt("unfocused.csv", delimiter=",", dtype=str)
titles = data[0]
data = data[1:-1]
data = data.astype(float)

poor = data[1:-1, 0]
raw = data[1:-1, 1]
unfocused_attention = data[1:-1, 2]
unfocused_meditation = data[1:-1, 3] 

focused_avg_atte = np.mean(focused_attention)
focused_avg_med = np.mean(focused_meditation)

unfocused_avg_atte = np.mean(unfocused_attention)
unfocused_avg_med = np.mean(unfocused_meditation)

print("focused avg: att %f, med %f"%(focused_avg_atte, focused_avg_med))
print("unfocused avg: att %f, med %f"%(unfocused_avg_atte, unfocused_avg_med))




timeVector = [i for i in range(len(raw))]
plt.subplot(212)
plt.title("unfocused")
plt.plot(timeVector, poor, "b", label="poor")
plt.plot(timeVector, raw, "r", label="raw")
plt.plot(timeVector, unfocused_attention, "g", label="attention")
plt.plot(timeVector, unfocused_meditation, "m", label="meditation")
plt.legend()
plt.show()


