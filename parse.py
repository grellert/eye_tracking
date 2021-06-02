import pandas as pd 
import numpy as np 

columns = "RespondentNr", "StimulusNr", "timestamp ms","Gaze x %","Gaze y"
data = pd.read_csv("teste.csv", comment = "#", sep = ";", skip_blank_lines=True)
print(data.describe())

screen_w, screen_h = 400, 400

gaze_times = []
for idx in range(data["timestamp ms"].shape[0]-1):
    gaze_time = data["timestamp ms"].values[idx+1] - data["timestamp ms"].values[idx]
    gaze_times.append(gaze_time)
gaze_times.append(0)

data["gaze time ms"] = gaze_times
data["time stamp s"] = np.floor(data["timestamp ms"]/1000.0).astype(int)
data.drop("timestamp ms", axis = 1, inplace = True)
data.to_csv("processado.csv", sep = ";")
grouped = data.groupby(["RespondentNr","StimulusNr","time stamp s","Gaze x %", "Gaze y %"]).sum()
print(grouped)