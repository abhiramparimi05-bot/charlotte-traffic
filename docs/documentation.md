# Charlotte Traffic Prediction — Code Documentation

## 1. Data Collection (`collect_traffic.py`)

**`traffic_level(ratio)`**

Classifies traffic using the ratio of current speed to free-flow speed. Returns low, medium, or high congestion.

**`get_weather()`**

Requests current Charlotte weather data from Open-Meteo, including temperature, precipitation, weather code, and wind speed. If the request fails, it returns blank weather fields.

**`collect()`**

Requests traffic flow information for 25 Charlotte locations using the TomTom API. It combines traffic measurements, weather conditions, and time information, calculates congestion labels, and appends the observations to `charlotte_traffic.csv`.

## 2. Data Preparation (`data_preparation.ipynb`)

The notebook performs the following operations using pandas:

- Loads `charlotte_traffic.csv`.
- Inspects column names, data types, and missing values.
- Removes duplicate rows.
- Standardizes column names and text values.
- Converts timestamps and creates time-related features.
- Checks numeric values and congestion class distribution.
- Creates traffic-level and average-speed visualizations using matplotlib.
- Saves the prepared dataset to `cleaned_charlotte_traffic.csv`.

## 3. Machine Learning (`Charlotte_Traffic_Prediction.ipynb`)

**Feature selection:** Uses time, road, location, and weather information as model inputs.

**Target creation:** Converts congestion labels into two classes: no/low traffic (0) and medium/high traffic (1).

**Preprocessing:** Uses `ColumnTransformer`, `OneHotEncoder`, and `StandardScaler` to prepare categorical and numeric features.

**Training:** Sorts records by timestamp, uses the earliest 80% for training and the latest 20% for testing, and trains a Random Forest classifier with 300 trees.

**Evaluation:** Calculates accuracy, balanced accuracy, classification report, and confusion matrix.

**Predictions:** Estimates traffic probabilities for test observations and the latest available record from each location.

## 4. Example Script (`bin/run_demo.py`)

The example script loads the cleaned traffic CSV using pandas, displays sample records, and prints the congestion-level distribution.

Run it from the project directory:

```bash
python bin/run_demo.py
```
