# Objective : To learn about Horizontal concat of dataframes in pandas

import pandas as pd

# Assuming these are different sensor types for the same 4 vehicles (VehicleID set as index)
data_sensor_a = {
    'Sensor_A_Reading_Temp': [25.5, 26.1, 24.9, 27.0],
    'Sensor_A_Error_Code': [0, 1, 0, 0]
}
# Set VehicleID as index so concat can align rows
df_sensor_a_readings = pd.DataFrame(data_sensor_a, index=[101, 102, 103, 104])
df_sensor_a_readings.index.name = 'VehicleID'

data_sensor_b = {
    'Sensor_B_Reading_Pressure': [101.2, 100.5, 101.1, 100.8],
    'Sensor_B_Status': ['OK', 'WARN', 'OK', 'OK']
}
# Set VehicleID as index to match df_sensor_a_readings
df_sensor_b_readings = pd.DataFrame(data_sensor_b, index=[101, 102, 130, 140])
df_sensor_b_readings.index.name = 'VehicleID'


print("df_sensor_a_readings:\n", df_sensor_a_readings)
print("\ndf_sensor_b_readings:\n", df_sensor_b_readings)

print("\n\n---------Columnwise concat-----------------")

df_horiz_concat =  pd.concat([df_sensor_a_readings, df_sensor_b_readings],axis = 1)
print(df_horiz_concat)

print("Columnwise concat indexes")
print(f"{df_horiz_concat.index}")