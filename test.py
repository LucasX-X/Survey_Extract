import json

with open('/Users/theo/PycharmProjects/surveyDataCollection/MyQualtricsDownload/[Bart]FY19 - Construction 2 (Construction Services).json', 'r') as f:
    data = json.load(f)

print(len(data))