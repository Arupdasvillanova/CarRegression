{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyMgh8cj0BjrDyAAp6z0C+vL"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","execution_count":null,"metadata":{"id":"v3wTEoAX2qmQ"},"outputs":[],"source":["# app.py\n","import streamlit as st\n","import pandas as pd\n","import pickle\n","\n","# Load the pre-trained model\n","model = pickle.load(open('Car_Regression_Model_version_1.pkcls', 'rb'))\n","\n","# Define the input fields and their types\n","def user_input_features():\n","    symboling = st.selectbox('Symboling', options=[-3, -2, -1, 0, 1, 2, 3])\n","    carCompany = st.text_input('Car Company')\n","    fueltype = st.selectbox('Fuel Type', options=['gas', 'diesel'])\n","    aspiration = st.selectbox('Aspiration', options=['std', 'turbo'])\n","    doornumber = st.selectbox('Number of Doors', options=['two', 'four'])\n","    carbody = st.selectbox('Car Body', options=['sedan', 'hatchback', 'wagon', 'hardtop', 'convertible'])\n","    drivewheel = st.selectbox('Drive Wheel', options=['fwd', 'rwd', '4wd'])\n","    enginelocation = st.selectbox('Engine Location', options=['front', 'rear'])\n","    wheelbase = st.slider('Wheelbase', min_value=86.6, max_value=120.9, step=0.1)\n","    carlength = st.slider('Car Length', min_value=141.1, max_value=208.1, step=0.1)\n","    carwidth = st.slider('Car Width', min_value=60.3, max_value=72.3, step=0.1)\n","    carheight = st.slider('Car Height', min_value=47.8, max_value=59.8, step=0.1)\n","    curbweight = st.number_input('Curb Weight', min_value=1500, max_value=4000, step=1)\n","    enginetype = st.selectbox('Engine Type', options=['dohc', 'dohcv', 'l', 'ohc', 'ohcf', 'ohcv', 'rotor'])\n","    cylindernumber = st.selectbox('Cylinder Number', options=['two', 'three', 'four', 'five', 'six', 'eight', 'twelve'])\n","    enginesize = st.number_input('Engine Size', min_value=61, max_value=326, step=1)\n","    fuelsystem = st.selectbox('Fuel System', options=['1bbl', '2bbl', '4bbl', 'idi', 'mfi', 'mpfi', 'spdi', 'spfi'])\n","    boreratio = st.number_input('Bore Ratio', min_value=2.54, max_value=3.94, step=0.01)\n","    stroke = st.number_input('Stroke', min_value=2.07, max_value=4.17, step=0.01)\n","    compressionratio = st.number_input('Compression Ratio', min_value=7.0, max_value=23.0, step=0.1)\n","    horsepower = st.number_input('Horsepower', min_value=48, max_value=288, step=1)\n","    peakrpm = st.number_input('Peak RPM', min_value=4150, max_value=6600, step=50)\n","    citympg = st.number_input('City MPG', min_value=13, max_value=49, step=1)\n","    highwaympg = st.number_input('Highway MPG', min_value=16, max_value=54, step=1)\n","\n","    # After adding fields for all features, return the data as a DataFrame\n","    data = {\n","        'symboling': symboling,\n","        'carCompany': carCompany,\n","        'fueltype': fueltype,\n","        'aspiration': aspiration,\n","        'doornumber': doornumber,\n","        'carbody': carbody,\n","        'drivewheel': drivewheel,\n","        'enginelocation': enginelocation,\n","        'wheelbase': wheelbase,\n","        'carlength': carlength,\n","        'carwidth': carwidth,\n","        'carheight': carheight,\n","        'curbweight': curbweight,\n","        'enginetype': enginetype,\n","        'cylindernumber': cylindernumber,\n","        'enginesize': enginesize,\n","        'fuelsystem': fuelsystem,\n","        'boreratio': boreratio,\n","        'stroke': stroke,\n","        'compressionratio': compressionratio,\n","        'horsepower': horsepower,\n","        'peakrpm': peakrpm,\n","      }\n","    features = pd.DataFrame(data, index=[0])\n","    return features\n","\n","# Display the app title and description\n","st.write(\"# Car Price Prediction App\")\n","st.write(\"This app predicts the **Car Price** based on various features!\")\n","\n","# Get user input\n","input_df = user_input_features()\n","\n","# When the 'Predict' button is clicked, make a prediction and display it\n","if st.button('Predict'):\n","    prediction = model.predict(input_df)\n","    st.write(f\"Estimated Car Price: ${prediction[0]:,.2f}\")\n","\n","# If desired, display the input data\n","st.write(\"## Input features\")\n","st.write(input_df)\n"]}]}