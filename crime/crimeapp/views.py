from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html',{'st':'Assam', 'year':'2030'})

def predictCases(request):
    
    st = request.GET["user"]
    year = request.GET["pass"]
    
    year = int(year)
    
    import numpy as np # linear algebra
    import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
    import seaborn as sns
    import matplotlib.pyplot as plt
    vic_rape_df = pd.read_csv("C:/MNNIT_Python/crime_data/20_Victims_of_rape.csv")
    
    mah_vic = vic_rape_df.loc[vic_rape_df['Area_Name']==st]
    mah_vic = mah_vic [(mah_vic['Subgroup']=='Total Rape Victims')]
    
    Y = mah_vic.Victims_of_Rape_Total.values
    X = mah_vic.Year[:,np.newaxis]
    
    Xmin = X.min()
    Xmax = X.max()
    Xnorm = (X -Xmin)/(Xmax-Xmin)
    Ynorm = (Y - Y.min())/(Y.max()-Y.min())
    df2 = mah_vic
    df2.Year = Xnorm
    df2.Victims_of_Rape_Total = Ynorm
    
    import sklearn.linear_model as lm
    lr = lm.LinearRegression()

    lr.fit(X,Y)  #Training the model
    
    noc = lr.predict(year)
    noc = int(noc)
    response = "In Year ",year," there is probability of ",noc," Cases"
    return HttpResponse(response)