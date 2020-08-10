import csv
import json

csvFile = 'SampleAIAALexiconReport.csv'
jsonFile = 'SampleAIAALexiconReport.json'

csvData = csv.reader(open(csvFile))

jsonData = open(jsonFile, 'w', encoding= "UTF-8")
jsonData.write('\n[')

rowNum = 0
for row in csvData:

    if rowNum == 0:
        tags = row

        for i in range(len(tags)):
            tags[i] = tags[i].replace(' ', '_')
    else:
        jsonData.write('\n{')

        for i in range(len(tags)):
            if '||' in '{}'.format(row[i]):
                row[i] = row[i].split('||')
            elif '|' in '{}'.format(row[i]):
                row[i] = row[i].split('|')
                row[i] = list(map(int, row[i]))
            elif row[i].isdigit():
                row[i] = int(row[i])
            elif row[i] == 'TRUE':
                row[i] = bool(row[i])
            elif row[i] == 'FALSE':
                row[i] = bool(row[i])
            elif row[i] == '':
                row[i] = None
            # print(row[i], "is of type", type(row[i]))
            row[i] = json.dumps(row[i], ensure_ascii=False)

            jsonData.write('\t"{0}":{1},\n'.format(tags[i], row[i]))
        jsonData.write('\n},')

    rowNum += 1

jsonData.write('\n]')

jsonData.close()
