# Geography Wise Churn
import streamlit as st
import pandas as pd

df = pd.read_csv("European_Bank.csv")

st.title("Customer Segmentation & Churn Analytics Dashboard")

churn_rate = round(df['Exited'].mean()*100,2)
st.metric("Overall Churn Rate (%)", churn_rate)

st.subheader("Geography Wise Churn")
geo_churn = df.groupby('Geography')['Exited'].mean()*100
st.bar_chart(geo_churn)
# gender wise churn
st.subheader("Gender Wise Churn")
gender_churn = df.groupby('Gender')['Exited'].mean()*100
st.bar_chart(gender_churn)
# active member analysis

st.subheader("Active Member Analysis")
active_churn = df.groupby('IsActiveMember')['Exited'].mean()*100
st.bar_chart(active_churn)
# dataset priview
st.subheader("Dataset Preview")
st.dataframe(df.head())
# dataset shape
st.subheader("Dataset Shape")
st.write("Rows",df.shape[0])
st.write("Columns:",df.shape[1])
# churn distribution
st.subheader("Churn Distribution")
churn_count=df['Exited'].value_counts()
st.bar_chart(churn_count)
# age wise churn
st.subheader("Age Wise Churn")
age_churn=df.groupby("Age")["Exited"].mean()*100
st.line_chart(age_churn)
# blance wise analysis
st.subheader("Balance Analysis")
st.bar_chart(df.groupby("Exited")["Balance"].mean())
# creadit score analysis
st.subheader("Creadit Score Analysis")
st.bar_chart(df.groupby("Exited")["CreditScore"].mean())
# churned customer count
st.metric("Churned Customers",df["Exited"].sum())
# tenure Analysis
st.subheader("Tenure Analysis")
st.bar_chart(df.groupby("Tenure")["Exited"].sum())
# retained customer count
st.metric("Retained Customers",len(df)-df["Exited"].sum())
# age & tenure churn comparison
st.subheader("Tenure Wise Churn")

tenure_churn = df.groupby('Tenure')['Exited'].mean()*100
st.bar_chart(tenure_churn)
# segment filter
country = st.sidebar.selectbox(
    "Select Geography",
    ["All"] + list(df["Geography"].unique())
)

if country != "All":
    df = df[df["Geography"] == country]
# high value customer churn
st.subheader("High Value Customer Churn")

high_value = df[df["Balance"] > df["Balance"].median()]
high_value_churn = round(high_value["Exited"].mean()*100,2)

st.metric("High Value Customer Churn Rate (%)", high_value_churn)
