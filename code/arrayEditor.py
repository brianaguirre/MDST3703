__author__ = 'BrianAguirre'

data = [
        ['AL', 'Alabama', '46', '46', 'Abortion'], ['AK', 'Alaska', '56', '52', 'Second Amendment (gun control)'], ['AZ', 'Arizona', '45', '66', 'Environment'], ['AR', 'Arkansas', '55', '44', 'Immigration Reform'], ['CA', 'California', '74', '66', 'Economy (tax reform)'], ['CO', 'Colorado', '67', '72', 'Surveillance'], ['CT', 'Connecticut', '66', '68', 'Foreign Policy'], ['DE', 'Delaware', '55', '59', 'Abortion'], ['DC', 'District of Columbia', '64', '87', 'Second Amendment (gun control)'], ['FL', 'Florida', '40', '4', 'Environment'], ['GA', 'Georgia', '43', '26', 'Immigration Reform'], ['HI', 'Hawaii', '54', '41', 'Abortion'], ['ID', 'Idaho', '58', '48', 'Second Amendment (gun control)'], ['IL', 'Illinois', '51', '37', 'Environment'], ['IN', 'Indiana', '54', '36', 'Immigration Reform'], ['IA', 'Iowa', '53', '41', 'Economy (tax reform)'], ['KS', 'Kansas', '46', '32', 'Surveillance'], ['KY', 'Kentucky', '44', '26', 'Foreign Policy'], ['LA', 'Louisiana', '47', '21', 'Abortion'], ['ME', 'Maine', '75', '12', 'Second Amendment (gun control)'], ['MD', 'Maryland', '75', '10', 'Environment'], ['MA', 'Massachusetts', '68', '20', 'Immigration Reform'], ['MI', 'Michigan', '50', '10', 'Economy (tax reform)'], ['MN', 'Minnesota', '46', '40', 'Surveillance'], ['MS', 'Mississippi', '38', '23', 'Foreign Policy'], ['MO', 'Missouri', '40', '35', 'Abortion'], ['MT', 'Montana', '48', '17', 'Second Amendment (gun control)'], ['NE', 'Nebraska', '39', '28', 'Environment'], ['NV', 'Nevada', '56', '15', 'Immigration Reform'], ['NH', 'New Hampshire', '65', '7', 'Economy (tax reform)'], ['NJ', 'New Jersey', '44', '6', 'Surveillance'], ['NM', 'New Mexico', '50', '7', 'Foreign Policy'], ['NY', 'New York', '77', '45', 'Abortion'], ['NC', 'North Carolina', '43', '10', 'Second Amendment (gun control)'], ['ND', 'North Dakota', '44', '14', 'Environment'], ['OH', 'Ohio', '53', '28', 'Immigration', 'Reform'], ['OK', 'Oklahoma', '43', '47', 'Economy (tax reform)'], ['OR', 'Oregon', '68', '14', 'Surveillance'], ['PA', 'Pennsylvania', '65', '46', 'Foreign', 'Policy'], ['RI', 'Rhode Island', '65', '28', 'Abortion'], ['SC', 'South Carolina', '39', '30', 'Second Amendment (gun control)'], ['SD', 'South Dakota', '43', '1', 'Environment'], ['TN', 'Tennessee', '44', '30', 'Immigration Reform'], ['TX', 'Texas', '41', '37', 'Economy (tax reform)'], ['UT', 'Utah', '47', '23', 'Surveillance'], ['VT', 'Vermont', '65', '21', 'Foreign Policy'], ['VA', 'Virginia', '54', '36', 'Abortion'], ['WA', 'Washington', '80', '25', 'Second Amendment (gun control)'], ['WV', 'West Virginia', '41', '16', 'Environment'], ['WI', 'Wisconsin', '48', '27', 'Immigration Reform'], ['WY', 'Wyoming', '47', '14', 'Economy (tax reform)']
    ]

for i in range(0, 50):
    if (i%6 == 0):
        data[i][2] = str(100-int(data[i][2]))
    else:
        data[i][2] = str(100-int(data[i][2]) - 8)



"""
for i in range(0, 50):
    print(str(data[i][1]) + ": ")
    for j in range(2,3):
        x = input("NEW: ")
        data[i][j] = x
        """


print (data)

data1 = [
	['AL', 'Alabama', '54', '46', 'Abortion'],
	['AK', 'Alaska', '48', '52', 'Second Amendment (gun control)'],
	['AZ', 'Arizona', '34', '66', 'Environment'],
	['AR', 'Arkansas', '56', '44', 'Immigration Reform'],
	['CA', 'California', '34', '66', 'Economy (tax reform)'],
	['CO', 'Colorado', '28', '72', 'Surveillance'],
	['CT', 'Connecticut', '32', '68', 'Foreign Policy'],
	['DE', 'Delaware', '41', '59', 'Abortion'],
	['DC', 'District of Columbia', '13', '87', 'Second Amendment (gun control)']
 ]