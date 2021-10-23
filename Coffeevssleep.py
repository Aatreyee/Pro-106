import plotly.express as px
import csv
with open ("D:\Coding folders\Python\Classes projects  97-107\Class 106\Cupsofcoffeevshoursofsleep.csv") as csv_file:
    df=csv.DictReader(csv_file)
    fig=px.scatter(df,x="Coffee in ml",y="sleep in hours",color="week")
    fig.show()