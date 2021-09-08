import csv
import numpy as np
import plotly.express as px


def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x = "Days Present",y = "Marks In Percentage")
        fig.show()


def getDataSource(data_path):
# Defining two arrays
    marks_of_students = []
    days_present = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
# Storing the values into the arrays
            marks_of_students.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))

# Returning the values from the arrays
    return {"x" : marks_of_students, "y": days_present}

def findCorrelation(datasource):
# Using the corrcoef function which has two datasets from the numpy library to find the correlation
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Student's Marks and the no. of days present :-  \n--->",correlation[0,1])

# Giving the path of the file in which content should be taken
def setup():
    data_path  = "Student Marks vs Days Present.csv"

# Calling the functions
    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()









