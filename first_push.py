
import pandas as pd
import numpy as np
import altair as alt
import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
df = pd.read_csv('WorldCups.csv')


df1 = df
df1.index = df1['Year']
cols = ['Winner', 'Runners-Up', 'Third', 'Fourth']
df2 = df
df2['Number of World Cups Won'] = df2.groupby('Winner')['Winner'].transform('count')
df3 = df
#goals_scored = df3.groupby('Winner')['GoalsScored'].sum().nlargest(10)
df3.index = df3['Country']

if st.sidebar.checkbox('Our project'):
    st.write("Here is where we will write about our project")
elif st.sidebar.checkbox('Show dataframe'):
    st.title('World cups dataset from kaggle.com')
    st.write(df)
elif st.sidebar.checkbox('Countries finishes at the WorldCup'):
    option = st.multiselect('What finishes do you want to display?', cols, cols[0])
    st.bar_chart(df1[option])

elif st.sidebar.checkbox('How many total WorldCups has each country won?'):
    min_year = int(df['Year'].min())
    max_year = int(df['Year'].max())
    year_range = st.slider('Select year range', min_value=min_year, max_value=max_year, value=(min_year,
                                                                                               max_year))
    filtered_df = df2[(df2['Year'] >= year_range[0]) & (df2['Year'] <= year_range[1])]
    fig = px.choropleth(filtered_df, locations='Country', locationmode='country names', color='Number of World Cups Won', 
                    hover_name='Country', color_continuous_scale='Blues', range_color=(0, df['Number of World Cups Won'].max()))
    fig.update_layout(title_text='World Cup Winners by Country', geo=dict(showframe=False, projection_type='equirectangular'))
    st.plotly_chart(fig)

elif st.sidebar.checkbox('Goals scored in the world cup'):
    goals_scored = df.groupby('Winner')['GoalsScored'].sum().nlargest(10)

    fig, ax = plt.subplots()
    ax.barh(goals_scored.index, goals_scored.values)
    ax.set_xlabel('Goals Scored')
    ax.set_ylabel('Country')
    ax.set_title('Most Goals Scored in the World Cup')

    st.pyplot(fig)
else:
    st.subheader("Welcome to team 3's final visualization, if you would like to see our dataframe, learn more about the background of our project, and see our visualizations, simply click the checkboxes to the left!")
