## Outlier detection
Outlier detection is the process of identifying observations or data points that significantly deviate from the majority of the data.
These observations are often referred to as **outliers** because they "lie outside" the typical pattern or distribution of the data¹. Here are some key points:

1. **What is an Outlier?**
   - An outlier is essentially a statistical anomaly—a data point that significantly deviates from other observations in a dataset.
   - Outliers can arise due to measurement errors, natural variation, or rare events.
   - They can have a disproportionate impact on statistical analyses and machine learning models if not appropriately handled.

2. **Why is Outlier Detection Important?**
   - **Accuracy Improvement**: Removing or accurately handling outliers enhances the performance and predictability of data models.
   - **Fraud Detection**: Outliers can indicate fraudulent activity, especially in financial or transaction data.
   - **Data Quality**: Regular outlier detection maintains data integrity and quality, affecting decision-making processes.
   - **Model Performance**: Outliers impact statistical models and machine learning algorithms. Handling them improves model accuracy.
   - **Insight Generation**: Outliers may represent unique or interesting phenomena in the data.

3. **Techniques for Outlier Detection**:
   - **Standard Deviation Method**: Identifies data points beyond a certain number of standard deviations from the mean.
   - **IQR (Interquartile Range) Method**: Uses quartiles to detect outliers based on the spread of data.
   - **Z-Score Method**: Measures how many standard deviations a data point is from the mean.
   - **Clustering Methods**: Detect outliers by analyzing data clusters.
   - **Isolation Forest**: Builds an ensemble of decision trees to isolate outliers.

1. **Sum (Total)**:
   - The `sum()` function calculates the sum of values in a pandas Series or DataFrame along a specified axis (usually rows or columns). For example:
     ```python
     import pandas as pd

     data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
     df = pd.DataFrame(data)

     total_sum = df['A'].sum()  # Sum of column 'A'
     print("Total sum of column 'A':", total_sum)
     ```

2. **Mean (Average)**:
   - The `mean()` function computes the average of numeric values in a Series or DataFrame. It provides the central tendency of the data. Example:
     ```python
     average = df['B'].mean()  # Mean of column 'B'
     print("Average of column 'B':", average)
     ```

3. **Median**:
   - The `median()` function returns the middle value of a sorted dataset. It's useful for understanding the central value when dealing with skewed data. Example:
     ```python
     median_value = df['A'].median()  # Median of column 'A'
     print("Median of column 'A':", median_value)
     ```

4. **Mode**:
   - The `mode()` function identifies the most frequently occurring value(s) in a dataset. Example:
     ```python
     mode_values = df['B'].mode()  # Mode(s) of column 'B'
     print("Mode(s) of column 'B':", mode_values)
     ```

5. **Min (Minimum)** and **Max (Maximum)**:
   - These functions return the smallest and largest values in a Series or DataFrame, respectively. Example:
     ```python
     min_value = df['A'].min()  # Minimum value in column 'A'
     max_value = df['B'].max()  # Maximum value in column 'B'
     print("Minimum value in column 'A':", min_value)
     print("Maximum value in column 'B':", max_value)
     ```

6. **Count** and **Count Unique**:
   - The `count()` function gives the number of non-null values in a Series or DataFrame. Example:
     ```python
     non_null_count = df['A'].count()  # Count of non-null values in column 'A'
     print("Non-null count in column 'A':", non_null_count)

   - The `nunique()` function returns the count of unique/distinct values in a Series. Example:
     ```python
     unique_count = df['B'].nunique()  # Count of unique values in column 'B'
     print("Unique count in column 'B':", unique_count)
     ```

7. **Standard Deviation** and **Variance**:
   - The `std()` function computes the standard deviation, which measures the dispersion or spread of data around the mean. Example:
     ```python
     std_dev = df['A'].std()  # Standard deviation of column 'A'
     print("Standard deviation of column 'A':", std_dev)

   - The `var()` function calculates the variance, which quantifies the variability of data. Example:
     ```python
     variance = df['B'].var()  # Variance of column 'B'
     print("Variance of column 'B':", variance)
     ```
