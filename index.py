python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the public transportation dataset
transport_data = pd.read_csv('Public_Transportation_Usage_AbuDhabi.csv')

# Load the air quality dataset
aqi_data = pd.read_json('Air_Quality_Index_AbuDhabi.json')

# Load the renewable energy production dataset
energy_data = pd.read_excel('Renewable_Energy_Production_AbuDhabi.xlsx')

# Analyze peak travel times
def analyze_peak_travel_times(data):
    data['Hour'] = pd.to_datetime(data['Time']).dt.hour
    peak_times = data.groupby('Hour').size()
    peak_times.plot(kind='bar', color='orange')
    plt.title('Peak Travel Times')
    plt.xlabel('Hour of Day')
    plt.ylabel('Number of Passengers')
    plt.show()

analyze_peak_travel_times(transport_data)

# Correlate AQI with transport data
def correlate_aqi_transport(aqi, transport):
    combined_data = pd.merge(aqi, transport, how='inner', left_on='Location', right_on='Area')
    correlation = combined_data['AQI'].corr(combined_data['Passengers'])
    print(f'Correlation between AQI and Passenger Numbers: {correlation}')

correlate_aqi_transport(aqi_data, transport_data)

# Renewable energy output analysis
def renewable_energy_analysis(energy):
    energy['Year'] = pd.to_datetime(energy['Date']).dt.year
    yearly_output = energy.groupby('Year').sum()
    yearly_output['Solar'].plot(label='Solar Energy', color='yellow')
    yearly_output['Wind'].plot(label='Wind Energy', color='blue')
    plt.title('Yearly Renewable Energy Output')
    plt.xlabel('Year')
    plt.ylabel('Energy Output (MWh)')
    plt.legend()
    plt.show()

renewable_energy_analysis(energy_data)
