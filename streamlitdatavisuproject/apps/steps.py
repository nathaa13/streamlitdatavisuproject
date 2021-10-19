import streamlit as st
import pandas as pd
import seaborn as sns


def get_year(dt):
    return dt.year

def get_month(dt):
    return dt.month

def get_dom(dt):
    return dt.day


def app():
    st.title('Step Data 👣')
    df = pd.read_csv('HealthData.csv')

#Date transformation
    df["Start"]= pd.to_datetime(df["Start"])
    df["Finish"]= pd.to_datetime(df["Finish"])

#récuperer l'année, le mois, et le jour du mois


    df['Year'] = df['Start'].map(get_year)
    df['Month'] = df['Start'].map(get_month)
    df['DoM'] = df['Start'].map(get_dom)
 

    st.header('Number of steps depending on the year')

    st.write("Choose the type of graphs and the years you want to visualize.")


    plot_types = ("Bar","Line","Area chart")
    chart_type = st.selectbox("Choose your chart type", plot_types)
    annee_selec = st.multiselect('Select years', df['Year'].unique())


    if chart_type == "Bar":

        for ele in annee_selec:

            data = df.loc[df['Year'] == ele]
            by_date=data.groupby('Month').sum()
            st.subheader(ele) 
            st.bar_chart(by_date['Steps (count)'])

    elif chart_type == "Line":

        for ele in annee_selec:

            data = df.loc[df['Year'] == ele]
            by_date=data.groupby('Month').sum()
            st.subheader(ele) 
            st.line_chart(by_date['Steps (count)'])

    elif chart_type == "Area chart":
        
        for ele in annee_selec:
    
            data = df.loc[df['Year'] == ele]
            by_date=data.groupby('Month').sum()
            st.subheader(ele) 
            st.area_chart(by_date['Steps (count)'])


#heatmap

    st.header(' Heatmap')
    Année = st.selectbox('Select year:',df['Year'].unique())
    data = df.loc[df['Year'] == Année]

    st.subheader('Heatmap of the number of steps according to the year selected') 

    df0 = data.pivot("Month", "DoM", "Steps (count)")

    y_labels= ['Janvier', 'Fevrier' ,'Mars', 'Avril', 'Mai' ,'Juin' ,'Juillet' ,'Aout ','Septembre', 'Octobre', 'Novembre', 'Decembre']
    

    st.pyplot(st.write(sns.heatmap(df0,yticklabels=y_labels)) )


