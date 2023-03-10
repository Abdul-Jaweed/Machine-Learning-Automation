import numpy as np
import pandas as pd
import streamlit as st
import io
import os
# from sklearn.model_selection import train_test_split


# Create space betwwen two context
def space():
    st.markdown("<br>", unsafe_allow_html=True)


st.title(":red[Machine Learning Automation]")
st.subheader("Its a Beta Version more features added soon")

# Main function
def app():

    # Uploading data
    df = st.file_uploader("Upload a Dataset", type=["csv"])
    space()
    if df is not None:
        # Reading data
        df = pd.read_csv(df)
        st.subheader("Phase One")
        data = st.radio('Click to view the Details of the Dataset : ',
                        ('Head', 'Tail','Sample', 'Columns', 'Shape', 'Info', 'Descriptive Statistics'),
                        horizontal=True)
        
        if data == 'Shape':
            st.subheader(":blue[Size of the Dataset]")
            st.write(f"Number of Rows:  {df.shape[0]}")
            st.write(f"Number of Columns:  {df.shape[1]}")
        elif data == 'Head':
            st.subheader(":blue[Top Five Rows]")
            st.write(df.head())
        elif data == 'Tail':
            st.subheader(":blue[Last Five Rows]")
            st.write(df.tail())
        elif data == 'Sample':
            st.subheader(":blue[Random Ten Rows]")
            st.write(df.sample(10))  
        elif data == 'Columns':
            st.subheader(":blue[Columns of the Dataset]")
            for column in list(df.columns):
                st.write(column)
        elif data == 'Info':
            st.subheader(":blue[Infomation of the Dataset]")
            buffer = io.StringIO()
            df.info(buf=buffer)
            s = buffer.getvalue()
            st.text(s)
        else:
            st.subheader(":blue[Statistical information of the Dataset]")
            st.write(df.describe())
            
         
            
        st.subheader("Phase Two")    
                   
        data = st.radio('Click to Preprocess of the Dataset : ',
                        ('Null Values', 'Percentage of Null Values', 'Duplicate Values','Percentage of Duplicate Values'),
                        horizontal=True)



        if data == 'Null Values':
            st.subheader(":blue[Null Values of the Dataset]")
            st.write(df.isnull().sum())
        elif data == 'Percentage of Null Values':
            st.subheader(":blue[Percentage of Null Values of the Dataset]")
            st.write(df.isnull().sum()/df.shape[0]) 
        elif data == 'Duplicate Values':
            st.subheader(":blue[Duplicate Values of the Dataset]")
            st.write(df.duplicated().sum())
        elif data == 'Percentage of Duplicate Values':
            st.subheader(":blue[Percentage of Duplicated Values of the Dataset]")
            st.write(df.duplicated().sum()/df.shape[0]) 




        # st.subheader("Phase Three")
        
        # data = st.multiselect("Select the Columns Name", (df.columns))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        












if __name__ == "__main__":
    app()