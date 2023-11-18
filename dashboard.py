import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title='Explore the Dashboard', page_icon=":bar_chart:", layout="wide")

csv_url = 'https://drive.google.com/uc?id=18vTti-msLZufyR0SnrTW5nBC4TkK3cOT'
dataset = pd.read_csv(csv_url)

st.sidebar.header("Filter")
cab_type = st.sidebar.multiselect(
    "Pilih Jenis Taksi : ",
    options=dataset["cab_type"].unique(),
    default=dataset["cab_type"].unique(),
    
)
name = st.sidebar.multiselect(
    "Pilih Nama Taksi : ",
    options=dataset["name"].unique(),
    default=dataset["name"].unique(),
    
)
short_summary = st.sidebar.multiselect(
    "Pilih Cuaca  : ",
    options=dataset["short_summary"].unique(),
    default=dataset["short_summary"].unique(),
    
)
month = st.sidebar.multiselect(
    "Pilih Bulan  : ",
    options=dataset["month"].unique(),
    default=dataset["month"].unique(),
    
)
day_of_week = st.sidebar.multiselect(
    "Pilih Bulan  : ",
    options=dataset["day_of_week"].unique(),
    default=dataset["day_of_week"].unique(),
    
)

dataset_selection=dataset.query(
    "cab_type==@cab_type & name == @name & short_summary==@short_summary & month==@month & day_of_week==@day_of_week"
)
st.dataframe(dataset_selection)

st.title(":bar_chart: Uber-Lyft Dashboard")
st.markdown("##")

total_price=int(dataset_selection['price'].sum())
avg_price=int(dataset_selection['price'].mean())

left_column, right_column = st.columns(2)
with left_column:
    st.subheader("Total Price : ")
    st.subheader(f"US ${total_price:,}")
with right_column:
    st.subheader("Rata-Rata Harga Pemesanan : ")
    st.subheader(f"US ${avg_price:,}")


st.markdown('---')

# price by cab_type
price_by_cab_type=(
    dataset_selection.groupby(by=['cab_type']).sum()[['price']].sort_values(by='price')

)

# price_by_cab_type = dataset_selection.groupby('cab_type')['price'].sum().sort_values()


fig_price_cabtype=px.bar(price_by_cab_type, x="cab_type", y=price_by_cab_type.index, orientation='h', title="<b>Price by Cab Type</b>", color_continuous_scale='viridis', template="plotly_white")
st.plotly_chart(fig_price_cabtype)










