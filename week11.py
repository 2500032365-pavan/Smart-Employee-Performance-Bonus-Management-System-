import pandas as pd


data = {

    "Name":["A","B","C"],

    "Salary":[30000,40000,50000],

    "Rating":[4.5,3.2,4.8]

}


df = pd.DataFrame(data)


print(df.describe())
