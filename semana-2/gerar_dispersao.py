import pandas as pd # data process
import numpy as np

#importando dataset 
data = pd.read_csv("./iris.csv",usecols=['SepalLengthCm','SepalWidthCm', 'PetalLengthCm','PetalWidthCm','Species']) 
data.head()

pd.options.plotting.backend = "plotly" 
np.random.seed(1) 
fig = data.plot.scatter([data['SepalLengthCm'], data['PetalLengthCm']],data['Species']) 
fig.show()