import pandas as pd
from CreateTraingData import CreateTraingData
windowsize=5

streamdata=pd.read_csv('FinalData.csv')         #streamdata is dataframe
CreateTraingData(streamdata,windowsize)
