# import requests
# import csv
#
# url = 'http://localhost:5000/vizier-db/api/v1/projects/bd52b624/datasets/acda8df615cc41e7866dbb29ae1fe36b/csv'
# resp = requests.get(url)
#
# with open('data1.csv','w') as f:
#     writer = csv.writer(f)
#     for line in resp.iter_lines():
#         writer.writerow(line.decode('utf-8').split(','))
#
# def plotData():
#     x = []
#     y = []
#     with open('data1.csv', 'r') as f:
#         reader = csv.reader(f)
#         next(reader, None)
#         for row in reader:
#             #print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~``")
#             #print(row)
#             if (len(row) > 6):
#                 x.append(float(row[4]))
#                 y.append(float(row[5]))
#     return {'x':x, 'y': y}
