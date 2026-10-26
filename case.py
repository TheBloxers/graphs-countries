import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('countries of the world.csv')


print('Menampilkan 5 data pertama')
print(df.head())

print('Menampilkan 5 data terakhir')
print(df.tail())

print('Menampilkan semua informasi')
print(df.info())

print('Menjelaskan data numerik/angka secara detail')
print(df.describe())

df['Deathrate'].plot(kind='hist', bins=7, color='red', edgecolor='beige')

plt.title('Deathrate by GDP ($ per capita)')
plt.xlabel('Deathrate')
plt.ylabel('GDP ($ per capita)')
plt.grid(axis='y', linestyle='--', alpha=0.9)

plt.tight_layout()
plt.savefig('Deathrate_GDP.png')
plt.show()
plt.close()

# race_counts = df['Region'].value_counts().sort_index()
# fig, ax = plt.subplots(figsize=(8, 5))
# race_counts.plot(kind='pie', color='skyblue', ax=ax)
# ax.set_title('Number of Countries by Region Group', fontsize=14, fontweight='bold')
# ax.set_xlabel('Region Group', fontsize=12)
# ax.set_ylabel('Country Count', fontsize=12)
# ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
# ax.grid(axis='y', linestyle='--', alpha=0.7)
# plt.tight_layout()
# plt.savefig('country_counts_by_gender.png')
# plt.close()
# plt.figure(figsize=(8, 5))


# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv("countries of the world.csv")

# avg = df.groupby('Deathrate')['GDP ($ per capita)'].mean()

# plt.figure()

# plt.subplot(1, 3, 1)
# plt.scatter(df['Birthrate'], df['GDP ($ per capita)'])

# plt.subplot(1, 3, 2)
# plt.hist(df['GDP ($ per capita)'])

# plt.subplot(1, 3, 3)
# plt.plot(avg.index, avg.values)

# plt.tight_layout()
# plt.show()
