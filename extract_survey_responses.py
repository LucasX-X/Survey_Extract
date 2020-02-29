import json

with open('/Users/theo/PycharmProjects/surveyDataCollection/MyQualtricsDownload/[Bart]FY19 - WO - Grounds - Feb 28.json', 'r') as f:
    data = json.load(f)

print("Satisfaction Rating Criteria: "
      "\nQ1: Work quality and timeliness of completion "
      "\nQ2: Consistency and quality of communication "
      "\nQ3: Level of technical expertise provided")
print("\nSatisfaction Rating Scores: "
      "\n1: Below Expectations "
      "\n2: Low Meets Expectations "
      "\n3: Meets Expectations "
      "\n4: High Meets Expectations "
      "\n5: Exceeds Expectations\n")

result = [(item.get('RecipientFirstName', 'NA'), item.get('RecipientLastName', 'NA'), item.get('RecipientEmail', 'NA'),
           item.get('EmbeddedDataB', 'NA'), item.get('EmbeddedDataA', 'NA'),
           item.get('Q2_1', 'NA'), item.get('Q2_2', 'NA'), item.get('Q2_6', 'NA'),
           item.get('Q3', 'NA'),
           item.get('Q5', 'NA'))
          for item in data['responses']]
sum1 = 0
sum2 = 0
sum3 = 0

for i in result:
    recipientName = i[0] + " " + i[1]
    print("%s.\tRecipient: %-20s %s" % (result.index(i) + 1, recipientName, i[2]))
    print("\tWork Order: %s\t %s" % (i[3], i[4]))
    print("\tQ1: %s Q2: %s Q3: %s" % (i[5], i[6], i[7]))
    sum1 += int(i[5])
    sum2 += int(i[6])
    sum3 += int(i[7])
    print("\tComment: %s" % (i[8]))
    if i[9] == "1":
        print("\tContact? Yes")
    else:
        print("\tContact? No")
    print("\n")

print("Average score for \"work quality and timeliness of completion\": %f" % (sum1 / len(result)))
print("Average score for \"consistency and quality of our communication\": %f" % (sum2 / len(result)))
print("Average score for \"level of technical expertise provided\": %f" % (sum3 / len(result)))
