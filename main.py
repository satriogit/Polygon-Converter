import streamlit as st
import pandas as pd
import re



st.header('Polygon Converter')
st.write('Input Data')
st.divider()
uploaded_file = st.file_uploader("Choose a file", type="xlsx")
if uploaded_file is not None:
    try:
        df = pd.read_excel(uploaded_file, "PolygonData")
        # def dms_to_decimal(dms):
        #     try:
        #         if isinstance(dms, float):
        #             return dms
        #         # Split the string into degrees, minutes, and seconds
        #         parts = dms.split('°')
        #         degrees = float(parts[0])
        #         minutes_seconds = parts[1].split("'")
        #         minutes = float(minutes_seconds[0])
        #         seconds = float(minutes_seconds[1].replace('"', ''))
                
        #         # Convert to decimal
        #         decimal = degrees + (minutes / 60) + (seconds / 3600)
        #         return decimal
        #     except ValueError as e:
        #         print(f"Error converting {dms}: {e}")
        #         return None
            
        # # ## Column Selection
        # selected_columns = df[['Corner 1', 'Unnamed: 4', 'Corner 2', 'Unnamed: 6', 'Corner 3', 'Unnamed: 8', 'Corner 4', 'Unnamed: 10', 'Corner 5', 'Unnamed: 12', 'Corner 6', 'Unnamed: 14', 'Corner 7', 'Unnamed: 16', 'Corner 8', 'Unnamed: 18', 'Corner 9', 'Unnamed: 20', 'Corner 10', 'Unnamed: 22', 'Corner 11', 'Unnamed: 24', 'Corner 12', 'Unnamed: 26', 'Corner 13', 'Unnamed: 28', 'Corner 14', 'Unnamed: 30', 'Corner 15', 'Unnamed: 32']]
        
        # regex = re.compile(r'Corner*')
        
        # filtered_list = [item for item in selected_columns if regex.match(item)]

        # print(selected_columns[filtered_list])

        
        # get_value = selected_columns.applymap(dms_to_decimal) * 8388608 / 90
        # get_value = get_value.round()
        
        # if not df[filtered_list].equals(selected_columns):
        #     print("The DataFrames are not equal.")
        #     final_value = '0,' + get_value.astype('string')
        # else:
        #     print("The DataFrames are equal.")
        #     final_value = '-' + get_value.astype('string')
        # # if regex.match(selected_columns):
        # #     final_value = '0,' + get_value.astype('string')
        # # else:
        # #     final_value = '- ' + get_value.astype('string')


        # st.subheader("Data from the Excel file:")
        # st.dataframe(final_value, hide_index=True)
    except Exception as e:
        st.error(f"Error reading the Excel file: {e}")
else:
    st.info("Please upload an Excel file to view its contents.")