Charlotte Traffic Congestion Prediction — Code Documentation
Course: DTSC 3602 

Group: Group 16

Team Members:
- Omar Osman — Data Preparation
- Justin Yip — Machine Learning
- Abhi (Abhiram) Parimi — Data Collection
Repository: https://github.com/abhiramparimi05-bot/charlotte-traffic
1. Project Overview
This project collects, cleans, analyzes, and predicts traffic congestion at 25 locations across Charlotte, North Carolina.

The project consists of three main components:
1. Data Collection: Retrieves traffic and weather information using external APIs.
2. Data Preparation: Cleans and transforms raw traffic observations.
3. Machine Learning: Trains and evaluates a Random Forest classifier to predict traffic conditions.
The original dataset uses three congestion categories: low, medium, and high.

The current machine-learning model combines these categories into two classes:
- 0: No/low traffic
- 1: Traffic (medium/high combined)
2. Data Collection — collect_traffic.py
Responsible Team Member: Abhi Parimi

The data-collection script retrieves traffic information from the TomTom Traffic Flow API and weather information from Open-Meteo.
Function: traffic_level(ratio)
Purpose: Assigns a congestion category based on the ratio between current traffic speed and free-flow speed.

Parameter:
- ratio (float): Current speed divided by free-flow speed.
Returns:
- "low" when the ratio is greater than 0.8.
- "medium" when the ratio is greater than 0.5 and less than or equal to 0.8.
- "high" when the ratio is less than or equal to 0.5.
Function: get_weather()
Purpose: Retrieves weather conditions for Charlotte from the Open-Meteo API.

Parameters: None.

Returns: Weather information including:
- Temperature in Fahrenheit
- Precipitation in inches
- Rain indicator
- Weather code
- Wind speed in miles per hour
If the weather API request fails, the function uses blank values so traffic collection can continue.
Function: collect()
Purpose: Collects traffic observations from 25 selected Charlotte locations.

Parameters: None. Uses the TomTom API key configured through the .env file.

Process:
1. Requests traffic information for the selected locations.
2. Retrieves weather information.
3. Extracts current speed, free-flow speed, travel time, and road information.
4. Calculates the speed ratio and traffic congestion category.
5. Combines traffic, weather, location, and timestamp information.
6. Appends observations to charlotte_traffic.csv.
Output: Updated charlotte_traffic.csv.
Running Data Collection
One traffic snapshot:

python collect_traffic.py

Repeated collection every 15 minutes:

python collect_traffic.py 15

New data collection requires a valid TomTom API key.
3. Data Preparation — data_preparation.ipynb
Responsible Team Member: Omar Osman

Input: charlotte_traffic.csv

Output: cleaned_Charlotte_traffic.csv
Purpose
The data-preparation notebook cleans and organizes traffic observations before they are used for machine learning.
Main Processing Steps
Step 1 — Data Loading

Uses pandas to load the raw CSV file and inspect the dataset.

Step 2 — Data Validation

Examines column types, missing values, and duplicate observations.

Step 3 — Data Cleaning

Removes duplicate records, standardizes column names, and cleans text fields where necessary.

Step 4 — Timestamp Processing

Converts timestamp information into datetime format and prepares time-related features for analysis.

Step 5 — Exploratory Data Analysis

Uses pandas and matplotlib to examine the distribution of traffic conditions and visualize traffic-related patterns.

Step 6 — Export

Saves the prepared dataset as cleaned_Charlotte_traffic.csv.
Importance
Data preparation helps ensure that the machine-learning component receives a consistent and structured dataset.
4. Machine Learning — Charlotte_Traffic_Prediction.ipynb
Responsible Team Member: Justin Yip

Input: cleaned_Charlotte_traffic.csv
Purpose
The machine-learning notebook trains a Random Forest classifier to predict whether traffic conditions fall into the no/low-traffic category or the combined medium/high-traffic category.
Target Variable
The original traffic_level column contains:
- low
- medium
- high
For binary classification:
- 0 represents low traffic.
- 1 represents medium or high traffic.
The target is created using the equivalent of:

y = (df["traffic_level"] != "low").astype(int)
Feature Selection
The model uses traffic-related, location, time, and weather features, including:
- Hour and minute
- Weekend indicator
- Rush-hour indicator
- Road and road type
- Road classification
- Temperature
- Precipitation
- Rain indicator
- Weather code
- Wind speed
- Road closure indicator
- Location
Data Preprocessing
ColumnTransformer

Applies different preprocessing operations to categorical and numerical features.

OneHotEncoder

Converts categorical features, such as road name and location, into a format suitable for machine learning.

StandardScaler

Standardizes numerical features.

Pipeline

Combines the preprocessing steps and Random Forest classifier into one machine-learning workflow.
Model Training
The notebook uses a chronological split:
- 80% training observations
- 20% testing observations
The Random Forest model uses 300 decision trees and balanced class weighting.

The training process fits the model using:

model.fit(X_train, y_train)
Model Evaluation
The notebook evaluates the trained model using:
- Accuracy
- Balanced accuracy
- Classification report
- Confusion matrix
These metrics provide information about prediction performance, including how well the model identifies both traffic categories.
Running the Machine-Learning Notebook
1. Install the required Python libraries.
2. Open Charlotte_Traffic_Prediction.ipynb in Jupyter Notebook or VS Code.
3. Ensure cleaned_Charlotte_traffic.csv is available in the project directory.
4. Run the notebook cells in order.
5. Review the model's training results and evaluation metrics.
5. Example Script — bin/run_demo.py
Purpose: Provides a simple command-line demonstration of the cleaned traffic dataset.
How It Works
1. Identifies the project directory using Python's pathlib.
2. Loads cleaned_Charlotte_traffic.csv using pandas.
3. Displays the first five rows of the dataset.
4. Counts observations in each traffic congestion category.
Example Output
For the included 100-observation dataset:
Congestion Level	Observations
Low	78
Medium	14
High	8
Total	100


How to Run
From the project directory, execute:

python3 bin/run_demo.py
Important Distinction
bin/run_demo.py does not train the Random Forest model.

It demonstrates that the cleaned dataset can be loaded and inspected successfully.

Model training is performed in Charlotte_Traffic_Prediction.ipynb.
6. Project File Structure
File or Folder	Purpose
README.md	Main project overview, installation, and usage instructions
collect_traffic.py	Traffic and weather data collection
charlotte_traffic.csv	Original traffic observations
data_preparation.ipynb	Data cleaning and preparation
cleaned_Charlotte_traffic.csv	Cleaned dataset
Charlotte_Traffic_Prediction.ipynb	Random Forest model training and evaluation
requirements.txt	Python dependency information
bin/run_demo.py	Example dataset demonstration
docs/documentation.md	Detailed project documentation
LICENSE	MIT License
archive/	Earlier project files and experiments


7. Dataset Description
The dataset contains observations from selected Charlotte roads.

Important fields include:
Column	Description
timestamp	Observation date and time
location	Traffic observation location
road	Road name
road_type	Road category
latitude, longitude	Geographic coordinates
current_speed_mph	Current traffic speed
free_flow_speed_mph	Free-flow traffic speed
speed_ratio	Current speed divided by free-flow speed
delay_s	Additional travel delay
temperature_f	Weather temperature
precipitation_in	Precipitation amount
is_raining	Rain indicator
wind_speed_mph	Wind speed
traffic_level	Low, medium, or high congestion


The sample dataset contains 100 observations, with more low-congestion observations than medium- or high-congestion observations.

This class imbalance should be considered when evaluating the machine-learning model.
8. Dependencies
The project uses Python 3 and the following primary libraries:
- requests
- python-dotenv
- pandas
- scikit-learn
- matplotlib
- notebook
Install the repository dependencies:

pip install -r requirements.txt

The updated requirements.txt includes the data-preparation and machine-learning libraries (pandas, scikit-learn, matplotlib, and notebook), so no additional installation command is needed.
9. Contact Information
Abhi (Abhiram) Parimi — Data Collection
aparimi@charlotte.edu

Omar Osman — Data Preparation
oosman2@charlotte.edu

Justin Yip — Machine Learning
iyip@charlotte.edu
10. License
This project is distributed under the MIT License.

License File:

https://github.com/abhiramparimi05-bot/charlotte-traffic/blob/main/LICENSE
