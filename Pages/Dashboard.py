import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv('Housing.csv')
 

st.title("Real state and price analysis")


st.dataframe(df)

st.sidebar.header("Filter Option")

Price = st.sidebar.slider('Price',
                              min_value = int(df['price'].min()),
                                max_value = int(df['price'].max()),
                                value = (int(df['price'].min()),int(df['price'].max())))


Area = st.sidebar.slider('sqft_lot',
                                min_value = int(df['sqft_lot'].min()),
                                max_value = int(df['sqft_lot'].max()),
                                value = (int(df['sqft_lot'].min()),int(df['sqft_lot'].max())))

Area = st.sidebar.slider('sqft_basement',
                                min_value = int(df['sqft_basement'].min()),
                                max_value = int(df['sqft_basement'].max()),
                                value = (int(df['sqft_basement'].min()),int(df['sqft_basement'].max())))

filtered_df = df[
    (df['price'].isin(Price))&
    (df['sqft_lot'].isin(Area))&
     (df['sqft_basement'].isin(Area))
]
st.dataframe(filtered_df)
              
             

rooms_lot= df.groupby('bedrooms')['sqft_lot'].count().reset_index()
fig = px.scatter(rooms_lot ,x='sqft_lot',y='bedrooms',title='Relationship between Sqft Lot and Bedrooms')
st.plotly_chart(fig)

bedroom_price = df.groupby('bedrooms')['price'].mean().reset_index()
fig = px.line(bedroom_price ,x='bedrooms',y='price',title='Price trends to no of Bedrooms')

st.plotly_chart(fig)

date_price=df.groupby('date')['price'].count().reset_index()
fig = px.line(date_price,x='date',y='price',title ='Data vs Price')

st.plotly_chart(fig)



bathroom_bedroom = df.groupby('bathrooms')['bedrooms'].mean().reset_index().astype(int)

fig = px.bar( bathroom_bedroom,x='bedrooms',y='bathrooms',title='Bedrooms vs Bathrooms') 

st.plotly_chart(fig)

bathroom_price = df.groupby('bathrooms')['price'].mean().reset_index().astype(int)

fig = px.bar( bathroom_price,x='bathrooms',y='price',title='Price vs Bathrooms')
st.plotly_chart(fig)

floors_price= df.groupby('floors')['price'].mean().reset_index().astype(int)
fig=px.line( floors_price,x='floors',y='price',title='Price trends to no of Floors')
st.plotly_chart(fig)

zipcode_price = df.groupby('zipcode')['price'].median().reset_index()
fig = px.bar(zipcode_price, x='zipcode', y='price', title='House Price by Zipcode')  
st.plotly_chart(fig)

yr_built_price = df.groupby('yr_built')['price'].median().reset_index()
fig=px.line(yr_built_price, x=yr_built_price.index, y='price', title='House Price by Year Built')
st.plotly_chart(fig)

sqft_living_price = df.groupby('sqft_living')['price'].median().reset_index()
fig=px.scatter(sqft_living_price, x='sqft_living', y='price', 
                                   title='Relationship between Sqft Living and Price')
st.plotly_chart(fig)

sqft_lot_price = df.groupby('sqft_lot')['price'].median().reset_index()
fig=px.scatter(sqft_lot_price, x='sqft_lot', y='price', 
                                   title='Relationship between Sqft Lot and Price') 
st.plotly_chart(fig)

waterfront_price = df.groupby('waterfront')['price'].median().reset_index()
fig= px.bar(waterfront_price, x='waterfront', y='price',title='Relationship between Waterfront and Price')
st.plotly_chart(fig)

grade_price = df.groupby('grade')['price'].median().reset_index()
fig=px.bar(grade_price, x='grade', y='price', title='Relationship between Grade and Price')
st.plotly_chart(fig)

condition_price = df.groupby('condition')['price'].median().reset_index()
fig=px.bar(condition_price, x='condition', y='price',title='Relationship between Condition and Price')
st.plotly_chart(fig)

view_price = df.groupby('view')['price'].median().reset_index()
fig=px.scatter(view_price, x='view', y='price',title='Relationship between View and Price')
st.plotly_chart(fig)

floors_price = df.groupby('floors')['price'].median().reset_index()
fig=px.bar(floors_price, x='floors', y='price',title='Relationship between Floors and Price')
st.plotly_chart(fig)