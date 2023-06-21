import streamlit as st
import pandas as pd

def calculate_inhalation_dose(radionuclide, activity_concentration, data):
    # Find the corresponding row for the radionuclide
    row = data[data['Radionuclide'] == radionuclide].index
    
    # Check if the radionuclide exists in the data
    if len(row) == 0:
        return "Radionuclide not found in the data."
    
    # Calculate the inhalation dose per liter
    inhalation_dose = activity_concentration * data.loc[row, 'Inhalation Dose coefficient ICRP 68 (mrem/curie)'].values[0]
    
    return inhalation_dose

# Read the data from the CSV file
data = pd.read_csv('rad.csv')

# Create a list of radionuclides for the dropdown menu
radionuclides = data['Radionuclide'].tolist()

# Streamlit app
st.title('Inhalation Dose Calculator')

# Radionuclide selection
radionuclide = st.selectbox('Select Radionuclide', radionuclides)

# Activity concentration input
activity_concentration = st.number_input('Enter Activity Concentration (Ci/L)')

# Calculate and display the inhalation dose per liter
if st.button('Calculate'):
    dose = calculate_inhalation_dose(radionuclide, activity_concentration, data)
    st.write(f'Inhalation Dose Per Liter: {dose:.4f} mrem/L')
