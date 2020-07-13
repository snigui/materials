import requests
import csv
#
# data = {'columns': [{'id': 0, 'name': 'CASE_NAME', 'type': 'string'}, {'id': 1, 'name': 'INTEGRATION_D', 'type': 'string'}, {'id': 2, 'name': 'INTEGRATION_R', 'type': 'string'}, {'id': 3, 'name': 'INTEGRATION_G', 'type': 'string'}, {'id': 4, 'name': 'JSC', 'type': 'string'}, {'id': 5, 'name': 'JSC/INT_D', 'type': 'string'}, {'id': 6, 'name': 'INT_R/INT_D', 'type': 'string'}, {'id': 7, 'name': 'INT_D/INT_G', 'type': 'string'}, {'id': 8, 'name': 'PASS TEST?', 'type': 'string'}], 'id': '6070d166f8f846c2a609cdb0ea65ad12', 'links': [{'href': 'http://localhost:5000/vizier-db/api/v1/projects/12020d28/datasets/6070d166f8f846c2a609cdb0ea65ad12', 'rel': 'self'}, {'href': 'http://localhost:5000/vizier-db/api/v1/projects/12020d28/datasets/6070d166f8f846c2a609cdb0ea65ad12?limit=-1', 'rel': 'dataset.fetch'}, {'href': 'http://localhost:5000/vizier-db/api/v1/projects/12020d28/datasets/6070d166f8f846c2a609cdb0ea65ad12/csv', 'rel': 'dataset.download'}, {'href': 'http://localhost:5000/vizier-db/api/v1/projects/12020d28/datasets/6070d166f8f846c2a609cdb0ea65ad12/annotations', 'rel': 'annotations.get'}, {'href': 'http://localhost:5000/vizier-db/api/v1/projects/12020d28/datasets/6070d166f8f846c2a609cdb0ea65ad12/annotations', 'rel': 'annotations.update'}, {'href': 'http://localhost:5000/vizier-db/api/v1/projects/12020d28/datasets/6070d166f8f846c2a609cdb0ea65ad12?offset=0', 'rel': 'page.first'}], 'offset': 0, 'rowCount': 9, 'rows': [{'id': '-882375290', 'rowAnnotationFlags': [True, True, True, True, True, True, True, True, True], 'values': ['t1/20x20/test', '3.68E+27', '3.37E+26', '5.89E+27', '7.45074', '0.9395447253', '0.0915464505', '0.6240682448', 'y']}, {'id': '1711256519', 'rowAnnotationFlags': [True, True, True, True, True, True, True, True, True], 'values': ['t1/20x20/test00000', '7.70E+26', '1.75E+24', '6.06E+27', '1.70469', '1.027447789', '0.002273079588', '0.1269288146', 'y']}, {'id': '-1503566732', 'rowAnnotationFlags': [True, True, True, True, True, True, True, True, True], 'values': ['t1/20x20/test00010', '8.00E+26', '1.74E+24', '6.05E+27', '1.75905', '1.020372056', '0.00217347572', '0.1321302655', 'y']}, {'id': '-1286017054', 'rowAnnotationFlags': [True, True, True, True, True, True, True, True, True], 'values': ['t1/20x20/test00020', '8.99E+26', '6.23E+24', '5.99E+27', '1.98183', '1.022500025', '0.006925271637', '0.1500983505', 'y']}, {'id': '307001290', 'rowAnnotationFlags': [True, True, True, True, True, True, True, True, True], 'values': ['t1/20x20/test00030', '9.06E+26', '3.74E+24', '6.10E+27', '1.93674', '0.99168958', '0.004126612286', '0.1485701897', 'y']}, {'id': '-672325411', 'rowAnnotationFlags': [True, True, True, True, True, True, True, True, True], 'values': ['t1/20x20/test00040', '8.34E+26', '3.64E+24', '6.04E+27', '1.8343', '1.020387728', '0.00436455372', '0.1379539245', 'y']}, {'id': '952121547', 'rowAnnotationFlags': [True, True, True, True, True, True, True, True, True], 'values': ['t1/20x20/test00050', '8.34E+26', '3.64E+24', '6.04E+27', '1.8343', '1.020387728', '0.00436455372', '0.1379539245', 'y']}, {'id': '1545774357', 'rowAnnotationFlags': [True, True, True, True, True, True, True, True, True], 'values': ['t1/20x20/test00060', '8.34E+26', '3.64E+24', '6.04E+27', '1.8343', '1.020387728', '0.00436455372', '0.1379539245', 'y']}, {'id': '2054255425', 'rowAnnotationFlags': [True, True, True, True, True, True, True, True, True], 'values': ['t1/20x20/test00070', '1.05E+27', '1.43E+24', '6.07E+27', '2.30433', '1.017126235', '0.001363870705', '0.173031039', 'y']}]}

# url = 'http://localhost:5000/vizier-db/api/v1/projects/12020d28/datasets/6070d166f8f846c2a609cdb0ea65ad12/csv'
# resp = requests.get(url)
# with open('data1.csv','w') as f:
#     writer = csv.writer(f)
#     for line in resp.iter_lines():
#         writer.writerow(line.decode('utf-8').split(','))
#         print(line)



def tableData():
    x = []
    y = []
    with open('dash_table/data1.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~``")
            print(row)
            x.append(float(row[4]))
            y.append(float(row[5]))
    return {'x':x, 'y': y}
