import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
import csv

df = pd.read_csv("PDS2.csv")
rows = []
with open ('PDS2.csv', 'r') as f:
  file = csv.reader(f)
  for row in file:
    rows.append(row)
headers = rows[0]
stardata = rows[1:]

headers[0] = 'row number'

starmass = []
starradius = []
starname = []

for i in stardata:
  starmass.append(i[4])
  starradius.append(i[5])
  starname.append(i[2])
stargravity = []

for index,name in enumerate(starname):
  g = float(starmass[index])
  g2 =  g*5.972e+24
  g3 = g2/(float(starradius[index]))
  g4 = g3*(float(starradius[index]))
  g5 = g4*(6371000*637100)
  g6 = g5*6.674e-11
  stargravity.append(g6)
'''
index = df[1].tolist()
names = df[2].tolist()
distance = df[3].tolist()
mass = df[4].tolist()
radius = df[5].tolist()
'''
X = []
for index, starmass in enumerate(starmass):
  temp_list = [
                  starradius[index],
                  starmass
              ]
  X.append(temp_list)

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state = 42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(10,5))
sns.lineplot(range(1, 11), wcss, marker='o', color='red')
plt.title('Elbow Graph')
plt.xlabel('Clusters')
plt.ylabel('WCSS')
plt.show()
