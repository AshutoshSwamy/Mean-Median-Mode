import csv 
with open("HeightWeight.csv", newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
#print(file_data)
new_data = []
for i in range(len(file_data)):
    num = file_data[i][1]
    new_data.append(float(num))
print(new_data)

n = len(new_data)
new_data.sort()
if(n%2 == 0):
    median_1 = float(new_data[n//2])
    median_2 = float(new_data[n//2-1])
    median = (median_1 + median_2)/2