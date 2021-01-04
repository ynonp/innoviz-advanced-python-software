import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('covid19_tweets.csv')

data = df.groupby('user_name').count()['text'].sort_values(ascending=False).head()

data.plot(kind="pie")

plt.show()
