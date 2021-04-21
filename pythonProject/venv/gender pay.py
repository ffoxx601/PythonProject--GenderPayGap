# plot graphs of pay rates in relation to education and gender
import pandas
import seaborn
import matplotlib.pyplot
gender_data = pandas.read_csv('Glassdoor Gender Pay Gap.csv')

seaborn.catplot(x="Education", y="BasePay", kind="bar", hue="Gender", data=gender_data)
seaborn.catplot(x="Education", y="Bonus", kind="bar", hue="Gender", data=gender_data)

matplotlib.pyplot.show()

# comparing the average salary of men and women based on educational level
import csv

def mean(data):
    total = sum(data)
    length = len(data)

    return total / length

with open('Glassdoor Gender Pay Gap.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)

    femalephdsalary = []
    femalemasterssalary = []
    femalecollegesalary = []
    femalehighschoolsalary = []
    malephdsalary = []
    malemasterssalary = []
    malecollegesalary = []
    malehighschoolsalary = []

    for row in spreadsheet:
        if row['Gender'] == 'Female':
            if row['Education'] == 'PhD':
                femalephdsalary.append(int(row['BasePay']) + int(row['Bonus']))
            if row['Education'] == 'Masters':
                femalemasterssalary.append(int(row['BasePay']) + int(row['Bonus']))
            if row['Education'] == 'College':
                femalecollegesalary.append(int(row['BasePay']) + int(row['Bonus']))
            if row['Education'] == 'High School':
                femalehighschoolsalary.append(int(row['BasePay']) + int(row['Bonus']))
        if row['Gender'] == 'Male':
            if row['Education'] == 'PhD':
                malephdsalary.append(int(row['BasePay']) + int(row['Bonus']))
            if row['Education'] == 'Masters':
                malemasterssalary.append(int(row['BasePay']) + int(row['Bonus']))
            if row['Education'] == 'College':
                malecollegesalary.append(int(row['BasePay']) + int(row['Bonus']))
            if row['Education'] == 'High School':
                malehighschoolsalary.append(int(row['BasePay']) + int(row['Bonus']))


    print("The average pay for a female with a PhD is ${}".format(round(mean(femalephdsalary), 2)))
    print("The average pay for a female with a Masters is ${}".format(round(mean(femalemasterssalary), 2)))
    print("The average pay for a female with a College degree is ${}".format(round(mean(femalecollegesalary), 2)))
    print("The average pay for a female with a high school certificate is ${}".format(round(mean(femalehighschoolsalary), 2)))

    print("The average pay for a male with a PhD is ${}".format(round(mean(malephdsalary), 2)))
    print("The average pay for a male with a Masters is ${}".format(round(mean(malemasterssalary), 2)))
    print("The average pay for a male with a College degree is ${}".format(round(mean(malecollegesalary), 2)))
    print("The average pay for a male with a high school certificate is ${}".format(round(mean(malehighschoolsalary), 2)))

# total number of men and women at each educational level
with open('Glassdoor Gender Pay Gap.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)

    phdwomencounter = 0
    masterswomencounter = 0
    collegewomencounter = 0
    highschoolwomencounter = 0

    phdmencounter = 0
    mastersmencounter = 0
    collegemencounter = 0
    highschoolmencounter = 0

    for row in spreadsheet:
        if row['Gender'] == 'Female':
            if row['Education'] == 'PhD':
                phdwomencounter += 1
            if row['Education'] == 'Masters':
                masterswomencounter += 1
            if row['Education'] == 'College':
                collegewomencounter += 1
            if row['Education'] == 'High School':
                highschoolwomencounter += 1
        if row['Gender'] == 'Male':
            if row['Education'] == 'PhD':
                phdmencounter += 1
            if row['Education'] == 'Masters':
                mastersmencounter += 1
            if row['Education'] == 'College':
                collegemencounter += 1
            if row['Education'] == 'High School':
                highschoolmencounter += 1
    print("Women with a PhD: {}".format(phdwomencounter))
    print("Women with a Masters: {}".format(masterswomencounter))
    print("Women with a college degree: {}".format(collegewomencounter))
    print("Women with high school certificate: {}".format(highschoolwomencounter))

    print("Men with a PhD: {}".format(phdmencounter))
    print("Men with a Masters: {}".format(mastersmencounter))
    print("Men with a college degree: {}".format(collegemencounter))
    print("Men with high school certificate: {}".format(highschoolmencounter))

