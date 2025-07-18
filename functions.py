#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
# Function to make the DataFrame's column names lowercase and replace spaces with underscores
def lower_case(df):
   
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    return df

# Function to rename column 'st' to 'state'
def change_column(df):
    df.rename(columns={"st": "state"}, inplace=True)
    return df

# Function to normalize gender representations
def gender_column(df):
    
    df["gender"] = df["gender"].replace(["female", "Female", "Femal"], "F").replace("Male", "M")
    return df

# Function to map abbreviated state names to full names
def state_func(df):
 
    states = {"cali": "california", "AZ": "Arizona", "WA": "Washington"}
    df["state"] = df["state"].replace(states)
    return df

# Function to standardize education terms
def bachelor_change(df):
    
    df["education"] = df["education"].replace("Bachelors", "Bachelor")
    return df

# Function to remove % characters from 'customer_lifetime_value'
def customer_lifetime(df):
    # Ensure the column is treated as strings
    df['customer_lifetime_value'] = df['customer_lifetime_value'].astype(str).str.replace('%', '')

    return df

# Function to convert 'customer_lifetime_value' to a float type
def changercustomer_value(df):
   
    df['customer_lifetime_value'] = df['customer_lifetime_value'].apply(float)
    return df

# Function to simplify vehicle class names
def change_car_types(df):
   
    df["vehicle_class"] = df["vehicle_class"].replace(["Sports Car", "Luxury SUV", "Luxury Car"], "Luxury")
    return df

# Convert 'number_of_open_complaints' to numeric
def change_column_tonumeric(df):

    df["number_of_open_complaints"] = pd.to_numeric(df["number_of_open_complaints"], errors="coerce")
    return df

def extract_middle_value(complaint_str):
    try:
        complaint_str = str(complaint_str)
        return int(complaint_str.split('/')[1])
    except (IndexError, ValueError, TypeError):
        return pd.NA


# Fill NaNs in 'number_of_open_complaints' with zero
#def filling_nas(df):
  
   # df["number_of_open_complaints"].fillna(0, inplace=True)
    #return df
    
def handle_nulls(df):

    # Identify categorical and numerical columns
    cat_var = df.select_dtypes(include="object").columns
    num_var = df.select_dtypes(include=["float64", "int64"]).columns
    
    # Fill null values in categorical variables with the mode
    for col in cat_var:
        if df[col].isnull().any():
            mode_value = df[col].mode(dropna=True)[0]  # use dropna=True with mode
            df[col].fillna(mode_value, inplace=True)
            
    # Fill null values in numerical columns with the mean
    for col in num_var:
        if df[col].isnull().any():
            mean_value = df[col].mean()
            df[col].fillna(mean_value, inplace=True)

    # Verify that all null values have been handled
    null_cols = df.columns[df.isnull().any()]
    if len(null_cols) == 0:
        print("All null values have been successfully handled")
    else:
        print("Null values still exist in the following columns:", null_cols)

    return df

def filling_nas(df):
    # Fill NaNs in 'number_of_open_complaints' with zero after final transformation
    df["number_of_open_complaints"].fillna(0, inplace=True)
    return df

# Function to remove duplicates
def drop_dupplicates(df):

    df.drop_duplicates(inplace=True)
    return df

def reset(df):
    df.reset_index(drop=True,inplace=True)
    return df

# Main function to run all cleaning functions
def main_cleaning(df):
    df = lower_case(df)
    df = change_column(df)
    df = gender_column(df)
    df = state_func(df)
    df = bachelor_change(df)
    df = customer_lifetime(df)
    df = changercustomer_value(df)
    df = change_car_types(df)
    if 'number_of_open_complaints' in df.columns:
        df['number_of_open_complaints'] = df['number_of_open_complaints'].apply(extract_middle_value)
    df = change_column_tonumeric(df)
    df = filling_nas(df)
    df = filling_nas(df)
    df = drop_dupplicates(df)
    df=reset(df)
    return df  

