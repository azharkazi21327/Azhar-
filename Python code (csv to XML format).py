import csv
import html
csvFile = 'FinalAIAATestFile.csv'
xmlFile = 'FinalAIAATestFile.xml'

csvData = csv.reader(open(csvFile))
xmlData = open(xmlFile, 'w', encoding = "UTF-8")
xmlData.write('<?xml version = "1.0" encoding="UTF-8"?>' + "\n")
# Only one top level term
xmlData.write('<Lexicon>' + "\n")

rowNum = 0
for row in csvData:
    if rowNum == 0:
        tags = row

        for i in range(len(tags)):
            tags[i] = tags[i].replace(' ', '_')
    else:
        xmlData.write('<Lexicon_Term>' + "\n")
        for i in range(len(tags)):
            #replacing ampersand with character entity
            #row[i] = row[i].replace('&','&amp;')
            row[i] = '{}'. format(row[i])
            row[i] = html.escape(row[i])
            xmlData.write('    ' + '<' + tags[i] + '>' \
                          + row[i] + '</' + tags[i] + '>' + "\n")
        xmlData.write('</Lexicon_Term>' + "\n")

    rowNum += 1

xmlData.write('</Lexicon>' + "\n")
xmlData.close()