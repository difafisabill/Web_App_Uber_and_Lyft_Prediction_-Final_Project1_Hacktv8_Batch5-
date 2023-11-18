import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
# st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")
def display_explore():
    st.title("Uber and Lyft Boston, MA")
    st.header("Dataset")
    st.text("Dataset ini sudah melalui proses data cleaning sehingga dapat dilakukan pemodelan")

    csv_url = 'https://drive.google.com/uc?id=18vTti-msLZufyR0SnrTW5nBC4TkK3cOT'
   
    dataset = pd.read_csv(csv_url)
 
    @st.cache_data
    def load_dataset():
        df = pd.read_csv(csv_url)
        return df

    page_size = 10
    page_number = st.slider("Halaman", 1, len(load_dataset()) // page_size + 1, 1)
    start_idx = (page_number - 1) * page_size
    end_idx = start_idx + page_size
    data = load_dataset().iloc[start_idx:end_idx]
    st.table(data)

    # Filter data 'cab_type Uber'
    uber_data = dataset[dataset['cab_type'] == 'Uber']
    st.subheader('Summary Statistics Uber')
    st.dataframe(uber_data.describe())

    # Filter data 'cab_type Uber'
    lyft_data = dataset[dataset['cab_type'] == 'Lyft']
    st.subheader('Summary Statistics Lyft')
    st.dataframe(lyft_data.describe())

    st.subheader('Perbandingan Uber VS Lyft')
    st.caption('Perbandingan jumlah pemesan antara Uber dan Lyft')
    bar_cab_type = px.bar(dataset['cab_type'].value_counts(), color=dataset['cab_type'].value_counts().index, color_continuous_scale='viridis')
    st.plotly_chart(bar_cab_type, use_container_width=True)

    st.caption('Perbandingan jumlah pemesan mingguan')
    bar_week=px.bar(dataset['day_of_week'].value_counts(), color=dataset['day_of_week'].value_counts().index, color_continuous_scale='viridis')
    st.plotly_chart(bar_week, use_container_width=True)

    

    st.caption('Perbandingan jumlah pemesan Per Jam berdasarkan Harga')
    sum_prices = dataset.groupby(['cab_type', 'hour']).sum().reset_index()
    fig, ax = plt.subplots()
    for cab_type, group in sum_prices.groupby('cab_type'):
        lines = ax.plot(group['hour'], group['price'], marker='o', label=cab_type)
    ax.set_xlabel('Jam')
    ax.set_ylabel('Total Harga')
    ax.legend()
    st.pyplot(fig)
    
   
   

