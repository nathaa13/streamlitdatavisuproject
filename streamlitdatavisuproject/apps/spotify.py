import datetime
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)

def get_year(dt):
    return dt.year

def get_month(dt):
    return dt.month

def get_hour(dt):
    return dt.hour

def count_rows(rows): 
        return len(rows)

def app():
    st.title('Data Spotify 🎶')
    df2 = pd.read_csv('Spotifydata.csv', quotechar='"')
    
    st.header('Number of songs listened to by date')



    d = st.date_input('Select the date', datetime.date(2021, 9, 15))
    df2["endTime"]= pd.to_datetime(df2["endTime"])
    
    #créer colonne 'jour' sans l'heure
    df2['jour'] = pd.to_datetime(df2['endTime']).dt.date
    

    #afficher nombre musiques écoutées selon la date

    
    df2['hour']=df2['endTime'].map(get_hour)
    data= df2[df2['jour'] == d]



    by_hour = data.groupby('hour').apply(count_rows)

    st.bar_chart(by_hour)

    st.write('Total music listened to this day:', by_hour.sum())



    st.header('Top Artists/Titles of All Time 🎙️')

    col1, col2 = st.columns(2)
    

    with col1:
        st.header('Top Artists')
        data1 = df2.groupby('artistName').apply(count_rows)
        data1= pd.DataFrame(data1, columns=['count'])
        data1['ArtistName'] = data1.index
        top_artists= data1[['ArtistName','count']].sort_values('count', ascending=False)[0:10]
        top_artists= top_artists.reset_index(drop=True)
        st.write(top_artists)
        
        plt.figure(figsize=(10,5))
        chart1=sns.barplot('ArtistName','count', data=top_artists)
        chart1.set_xticklabels(chart1.get_xticklabels(),rotation=45)
        chart1.set(xlabel='Artist', ylabel='Number of Songs')
        st.pyplot()
        
        
    with col2:
        st.header('Top Titles')

        data2 = df2.groupby('trackName').apply(count_rows)
        data2= pd.DataFrame(data2, columns=['count'])
        data2['trackName'] = data2.index
        top_tracks= data2[['trackName','count']].sort_values('count', ascending=False)[0:10]
        top_tracks=top_tracks.reset_index(drop=True)
        st.write(top_tracks)
        
        plt.figure(figsize=(10,5))
        chart2=sns.barplot('trackName','count', data=top_tracks)
        chart2.set_xticklabels(chart2.get_xticklabels(),rotation=45)
        chart2.set(xlabel='Track', ylabel='Number of Songs')
        st.pyplot()

        df2['Year'] = df2['endTime'].map(get_year)
        df2['Month'] = df2['endTime'].map(get_month)

    
    st.header('Top Artists/Titles per month/year')

    year = st.selectbox("Select a year", df2['Year'].unique())
    month = st.selectbox('Select a month', df2['Month'].unique())

    df2['Year'] = df2['endTime'].map(get_year)
    df2['Month'] = df2['endTime'].map(get_month)
    data = df2.loc[df2['Year'] == year]
    data = df2.loc[df2['Month'] == month]


    col1, col2 = st.columns(2)
    

    with col1:
        st.header('Top Artists')

        data1 = data.groupby('artistName').apply(count_rows)
        data1= pd.DataFrame(data1, columns=['count'])
        data1['artistName'] = data1.index
        top_artists= data1[['artistName','count']].sort_values('count', ascending=False)[0:10]
        top_artists= top_artists.reset_index(drop=True)
        st.write(top_artists)
        
        plt.figure(figsize=(10,5))
        chart1=sns.barplot('artistName','count', data=top_artists)
        chart1.set_xticklabels(chart1.get_xticklabels(),rotation=45)
        chart1.set(xlabel='Artist', ylabel='Number of Songs')
        st.pyplot()
        
        
    with col2:
        st.header('Top Titles')

        data2 = data.groupby('trackName').apply(count_rows)
        data2= pd.DataFrame(data2, columns=['count'])
        data2['trackName'] = data2.index
        top_tracks= data2[['trackName','count']].sort_values('count', ascending=False)[0:10]
        top_tracks=top_tracks.reset_index(drop=True)
        st.write(top_tracks)
    
        
        plt.figure(figsize=(10,5))
        chart2=sns.barplot('trackName','count', data=top_tracks)
        chart2.set_xticklabels(chart2.get_xticklabels(),rotation=45)
        chart2.set(xlabel='Track', ylabel='Number of Songs')
        st.pyplot()

        