import streamlit as st
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
# st.set_page_config(page_title="Eksplore", page_icon=":bar_chart:", layout="wide")


csv_url = 'https://drive.google.com/uc?id=1KLYx2M0YDM5ede7Hk_kW_v3nIGkKNzQ1'

# Membaca data
data = pd.read_csv(csv_url)


# Encode training data
le_training_cab_type = preprocessing.LabelEncoder()
le_training_name = preprocessing.LabelEncoder()

data['cab_type'] = le_training_cab_type.fit_transform(data['cab_type'])
data['name'] = le_training_name.fit_transform(data['name'])

# Train-test split
X = data[['cab_type', 'name', 'distance', 'surge_multiplier']]
y = data['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the LinearRegression model
model = LinearRegression()
model.fit(X_train, y_train)

# Streamlit app code
def display_predict():
    def predict_page():
        st.title("Uber and Lyft Price Prediction")

        st.write("""### Fitur Penting yang dibutuhkan""")

        cab_type_options = ["Uber", "Lyft"]
        name_options = [
            'Shared', 'Lux', 'Lyft', 'Lux Black XL', 'Lyft XL', 'Lux Black',
            'UberXL', 'Black', 'UberX', 'WAV', 'Black SUV', 'UberPool'
         ]

        cab_type_selected = st.selectbox("Jenis Taksi", cab_type_options)
        name_selected = st.selectbox("Nama taksi", name_options)
        distance = st.slider("Jarak", 0.0, 7.860, 1.0)
        surge_multiplier = st.slider("Surge Multiple", 0.0, 3.0, 1.0)

        # Transform user inputs using pre-trained LabelEncoders
        cab_type_encoded = le_training_cab_type.transform([cab_type_selected])
        name_encoded = le_training_name.transform([name_selected])

        important_feature = {
            'cab_type': cab_type_encoded[0],
            'name': name_encoded[0],
            'distance': distance,
            'surge_multiplier': surge_multiplier,
         }

        report_data = pd.DataFrame(important_feature, index=[0])
        return report_data

    user_feature = predict_page()
    st.header('Report')
    st.write(user_feature)

    calculate = st.button('Calculate Price')
    if calculate:
        # Prepare input array for prediction
        X_pred = np.array([[user_feature['cab_type'].iloc[0], user_feature['name'].iloc[0], user_feature['distance'].iloc[0], user_feature['surge_multiplier'].iloc[0]]])
        X_pred = X_pred.astype(float)

        # Make prediction using the trained model
        prediction = model.predict(X_pred)

        # Display the prediction
        st.write(f"Predicted Price: ${prediction[0]:.2f}")
