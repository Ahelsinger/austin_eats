import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

df = pd.read_csv('https://query.data.world/s/dm1x91ikhmk54am692862a7s3')
dfwhole = pd.read_csv('https://query.data.world/s/cosiwudjmqffla7w7wogwci62')
dfscorecount = pd.read_csv('https://query.data.world/s/6pukopv3emnqo4f22wehoyl9j')

# print df.head()
# print dfscorecount.head()

matplotlib.rcParams.update({'font.size': 10})

dfscorecount['zipnumber'] = range(1, len(dfscorecount) + 1)

x = df['Zip Code']
y = df['Score']
plt.hist(y,bins=20)
plt.xlabel('Scores')
plt.ylabel('Count')
plt.title("Austin Restaurant Inspections")
plt.show()


x2 = dfscorecount['Zip Code']
x3 = x2.astype('str')
y2 = dfscorecount['Score']
plt.scatter(x2,y2)
plt.xlabel('Zip Codes')
plt.xticks(x2,rotation=90)
plt.ylabel('Score', rotation=90)
plt.grid(True)
plt.show()

