import pandas as pd

def CreateTraingData(streamdata,windowsize):
    length=len(streamdata)-windowsize+1
    windowdata=pd.DataFrame(columns=[])
    for i in range(length):
