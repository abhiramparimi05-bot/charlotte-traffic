# Charlotte Traffic Congestion Prediction

**Group:** Group 16

**Team Members:**
- Omar Osman — Data Preparation
- Justin Yip — Machine Learning
- Abhi (Abhiram) Parimi — Data Collection

**Repository:** https://github.com/abhiramparimi05-bot/charlotte-traffic

## 1. Project Overview

Charlotte Traffic Congestion Prediction is a data science project that collects, prepares, and analyzes traffic data from 25 locations across Charlotte, North Carolina.

The project combines real-time traffic information from the TomTom Traffic Flow API with weather information from the Open-Meteo API.

The project consists of three components:

1. **Data Collection:** Retrieves traffic speeds, travel times, road conditions, and weather information.
2. **Data Preparation:** Cleans and transforms traffic observations into a dataset suitable for machine learning.
3. **Machine Learning:** Trains and evaluates a Random Forest classifier to predict traffic congestion.

The original traffic observations are labeled as low, medium, or high congestion.

The current machine-learning model uses two prediction classes:

- **0 — No/low traffic:** Original low-congestion category.
- **1 — Traffic:** Original medium- and high-congestion categories combined.

## 2. How the Project Works

1. `collect_traffic.py` requests traffic data from TomTom for 25 selected Charlotte locations.
2. The script retrieves Charlotte weather information from Open-Meteo.
3. Each observation receives a congestion label based on current speed compared with free-flow speed.
4. The collected observations are saved to `charlotte_traffic.csv`.
5. `data_preparation.ipynb` cleans and prepares the dataset.
6. The cleaned dataset is saved as `cleaned_Charlotte_traffic.csv`.
7. `Charlotte_Traffic_Prediction.ipynb` trains and evaluates the Random Forest classification model.
8. `bin/run_demo.py` provides a simple example of loading and inspecting the cleaned dataset.

## 3. Required Libraries and Installation

**Requirements:** Python 3, pip, and Git.

The project uses:

- `requests` — API requests
- `python-dotenv` — Environment-variable configuration
- `pandas` — Data preparation and analysis
- `scikit-learn` — Machine learning and evaluation
- `matplotlib` — Data visualization
- `notebook` — Jupyter Notebook support

### Installation

**Step 1 — Clone the repository**

```bash id="76fhcf"
git clone https://github.com/abhiramparimi05-bot/charlotte-traffic.git
```

**Step 2 — Open the project directory**

```bash id="k90d9a"
cd charlotte-traffic
```

**Step 3 — Create a virtual environment**

```bash id="p9at6h"
python3 -m venv venv
```

**Step 4 — Activate the environment**

Mac/Linux:

```bash id="7h3ljg"
source venv/bin/activate
```

Windows:

```bash id="n7uwb5"
venv\Scripts\activate
```

**Step 5 — Install dependencies**

```bash id="m4v7qb"
pip install -r requirements.txt
```

If the notebook libraries are not already included in `requirements.txt`, install them separately:

```bash id="m2s1vy"
pip install pandas scikit-learn matplotlib notebook
```

## 4. API Configuration

To collect new traffic observations, obtain a TomTom API key from:

https://developer.tomtom.com/

Create a `.env` file in the project directory:

```env id="r7n1ze"
TOMTOM_API_KEY=your_key_here
```

Replace `your_key_here` with your own API key.

The Open-Meteo API does not require an API key.

**Security:** Do not upload your `.env` file or private API key to GitHub.

The existing cleaned sample dataset can be used for the machine-learning demonstration without a TomTom API key.

## 5. Data Collection — Abhi Parimi

**File:** `collect_traffic.py`

The script collects traffic information from 25 locations, including roads such as I-77, I-85, I-485, I-277, Independence Boulevard, South Boulevard, and Providence Road.

The collected information includes traffic speed, free-flow speed, travel time, road classification, weather conditions, and congestion levels.

### Running Data Collection

Collect one traffic snapshot:

```bash id="f0h9kn"
python collect_traffic.py
```

Collect repeatedly at 15-minute intervals:

```bash id="x3kb2s"
python collect_traffic.py 15
```

**Output:** `charlotte_traffic.csv`

### Major Functions

- **`traffic_level(ratio)`** — Assigns a low, medium, or high congestion label.
- **`get_weather()`** — Retrieves weather information from Open-Meteo.
- **`collect()`** — Combines traffic, weather, location, and time information and saves observations to the CSV file.

## 6. Traffic Congestion Classification

Congestion is calculated using:

**Speed Ratio = Current Speed / Free-Flow Speed**

| Congestion Level | Speed Ratio |
|---|---|
| Low | Greater than 0.8 |
| Medium | Greater than 0.5 and less than or equal to 0.8 |
| High | Less than or equal to 0.5 |

The original dataset retains all three congestion categories.

The machine-learning component combines medium and high congestion into one traffic class.

## 7. Data Preparation — Omar Osman

**Notebook:** `data_preparation.ipynb`

**Input:** `charlotte_traffic.csv`

**Output:** `cleaned_Charlotte_traffic.csv`

The data-preparation component uses pandas and matplotlib to clean, validate, transform, and analyze traffic observations.

### Main Steps

1. Load the original traffic dataset.
2. Inspect column types, missing values, and duplicates.
3. Remove duplicate observations and standardize column names and text fields.
4. Convert timestamps and prepare time-related features.
5. Explore and visualize traffic patterns.
6. Export the cleaned dataset for machine learning.

The prepared dataset provides structured observations for the Random Forest model.

## 8. Machine Learning — Justin Yip

**Notebook:** `Charlotte_Traffic_Prediction.ipynb`

The project uses a Random Forest classifier to predict traffic conditions using road, location, time, and weather features.

### Prediction Categories

- `0` = No/low traffic
- `1` = Traffic (medium/high combined)

### Input Features

The model uses features such as:

- Hour and minute
- Weekend and rush-hour indicators
- Road and road type
- Road classification
- Temperature and precipitation
- Rain indicator
- Weather code
- Wind speed
- Road closure status
- Location

### Preprocessing and Training

The model uses:

- `ColumnTransformer`
- `OneHotEncoder`
- `StandardScaler`
- `Pipeline`
- `RandomForestClassifier`

The dataset is divided chronologically into **80% training data and 20% testing data**.

The Random Forest classifier uses **300 decision trees** with balanced class weighting.

### Evaluation

Model performance is evaluated using:

- Accuracy
- Balanced accuracy
- Classification report
- Confusion matrix

## 9. Quick Training Demo on a Small Dataset

The repository includes `cleaned_Charlotte_traffic.csv`, a sample dataset containing 100 observations.

You can train the machine-learning model using this dataset without collecting new API data.

### Option 1 — Run the Machine-Learning Notebook

Start Jupyter Notebook:

```bash id="ud4uwf"
jupyter notebook
```

Open:

`Charlotte_Traffic_Prediction.ipynb`

Make sure `cleaned_Charlotte_traffic.csv` is available in the project directory.

Run the notebook cells in order to preprocess the data, train the Random Forest classifier, and view the evaluation results.

### Option 2 — Run the Example Script

Run:

```bash id="m4d4xw"
python3 bin/run_demo.py
```

The script loads the cleaned CSV file and displays sample records and congestion counts.

**Important:** `bin/run_demo.py` does not train the Random Forest model. Model training is performed in `Charlotte_Traffic_Prediction.ipynb`.

### Example Model Training Code

```python id="wm14f2"
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    balanced_accuracy_score,
    classification_report
)

df = pd.read_csv("cleaned_Charlotte_traffic.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])

feature_cols = [
    "hour", "minute", "is_weekend", "is_rush_hour",
    "road", "road_type", "road_class_frc",
    "temperature_f", "precipitation_in",
    "is_raining", "weather_code", "wind_speed_mph",
    "road_closure", "location"
]

categorical_cols = [
    "road", "road_type", "road_class_frc", "location"
]

boolean_cols = [
    "is_weekend", "is_rush_hour",
    "is_raining", "road_closure"
]

numeric_cols = [
    col for col in feature_cols
    if col not in categorical_cols
]

X = df[feature_cols].copy()

for col in boolean_cols:
    X[col] = X[col].astype(int)

y = (df["traffic_level"] != "low").astype(int)

df_sorted = df.sort_values("timestamp")
split_index = int(len(df_sorted) * 0.80)

train_indices = df_sorted.index[:split_index]
test_indices = df_sorted.index[split_index:]

X_train = X.loc[train_indices]
X_test = X.loc[test_indices]

y_train = y.loc[train_indices]
y_test = y.loc[test_indices]

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_cols
        ),
        (
            "numeric",
            StandardScaler(),
            numeric_cols
        )
    ]
)

model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        (
            "random_forest",
            RandomForestClassifier(
                n_estimators=300,
                max_depth=8,
                min_samples_leaf=2,
                class_weight="balanced",
                random_state=42,
                n_jobs=-1
            )
        )
    ]
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(
    "Balanced Accuracy:",
    balanced_accuracy_score(y_test, y_pred)
)
print(
    classification_report(
        y_test,
        y_pred,
        labels=[0, 1],
        target_names=["No/low traffic", "Traffic"],
        zero_division=0
    )
)
```

## 10. Project Files

| File or Folder | Description |
|---|---|
| `README.md` | Project overview and instructions |
| `collect_traffic.py` | Traffic and weather data collection |
| `charlotte_traffic.csv` | Original traffic dataset |
| `data_preparation.ipynb` | Data cleaning and preparation |
| `cleaned_Charlotte_traffic.csv` | Cleaned dataset |
| `Charlotte_Traffic_Prediction.ipynb` | Random Forest model training and evaluation |
| `requirements.txt` | Python dependency information |
| `.gitignore` | Files excluded from Git tracking |
| `bin/run_demo.py` | Example dataset demonstration |
| `docs/documentation.md` | Detailed documentation |
| `LICENSE` | MIT License |
| `archive/` | Earlier project files |

## 11. Dataset Description

The dataset includes:

- Observation timestamp
- Road and location
- Latitude and longitude
- Current and free-flow traffic speeds
- Speed ratio
- Travel times and delays
- Temperature and precipitation
- Rain and wind conditions
- Traffic congestion level

### Sample Dataset Distribution

| Congestion Level | Observations |
|---|---:|
| Low | 78 |
| Medium | 14 |
| High | 8 |
| **Total** | **100** |

The dataset contains more low-congestion observations than medium- and high-congestion observations, creating class imbalance.

## 12. Documentation

Detailed explanations of the major functions and project workflows are available in:

[Code Documentation](docs/documentation.md)

This includes documentation for:

- `traffic_level(ratio)`
- `get_weather()`
- `collect()`
- Data-preparation workflow
- Machine-learning workflow
- `bin/run_demo.py`

## 13. Contact Information

**Abhi (Abhiram) Parimi — Data Collection**  
aparimi@charlotte.edu

**Omar Osman — Data Preparation**  
oosman2@charlotte.edu

**Justin Yip — Machine Learning**  
iyip@charlotte.edu

## 14. License

This project is licensed under the MIT License.

[View MIT License](LICENSE)

## 15. Future Improvements

Potential improvements include:

- Collecting more weekday and rush-hour traffic observations.
- Improving the balance between congestion categories.
- Testing additional machine-learning algorithms.
- Evaluating the model on larger datasets.
- Expanding the number of Charlotte roads and weather conditions.
- Exploring cloud storage and deployment options.
