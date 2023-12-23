import pandas as pd
import matplotlib.pyplot as plt

# Replace 'your_file.csv' with the path to your CSV file
df = pd.read_csv('sentimentdataset.csv')

# Display the first few rows of the dataframe
print(df.head())

# Assuming 'class_column' is the column containing class labels
target_distribution = df['Target'].value_counts()

# Display the distribution
print(target_distribution)



# Plot a bar chart for class distribution
target_distribution.plot(kind='bar', rot=45, color='skyblue')
plt.title('sentiment dataset Distribution')
plt.xlabel('Target')
plt.ylabel('Frequency')
plt.show()
