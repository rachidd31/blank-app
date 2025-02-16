import streamlit as st
import pandas as pd
import plotly.express as px

# Load the CSV data
@st.cache_data
def load_data():
    data = pd.read_csv("data.csv")  # Ensure the CSV file is in the same directory
    return data

data = load_data()

# Title of the dashboard
st.title("Sales Dashboard")

# Display key metrics
st.header("Key Metrics")
total_sales = data["Sales"].sum()
total_profit = data["Profit"].sum()
average_discount = data["Discount"].mean()
total_orders = data.shape[0]

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")
col3.metric("Average Discount", f"{average_discount:.2%}")
col4.metric("Total Orders", total_orders)

# Sales by Product Category
st.header("Sales by Product Category")
sales_by_category = data.groupby("Product_Category")["Sales"].sum().reset_index()
fig1 = px.bar(sales_by_category, x="Product_Category", y="Sales", title="Sales by Product Category")
st.plotly_chart(fig1)

# Order Priority Distribution
st.header("Order Priority Distribution")
order_priority = data["Order_Priority"].value_counts().reset_index()
order_priority.columns = ["Order_Priority", "Count"]
fig2 = px.pie(order_priority, names="Order_Priority", values="Count", title="Order Priority Distribution")
st.plotly_chart(fig2)

# Payment Method Distribution
st.header("Payment Method Distribution")
payment_method = data["Payment_method"].value_counts().reset_index()
payment_method.columns = ["Payment_method", "Count"]
fig3 = px.bar(payment_method, x="Payment_method", y="Count", title="Payment Method Distribution")
st.plotly_chart(fig3)

# Sales Trend Over Time
st.header("Sales Trend Over Time")
data["Order_Date"] = pd.to_datetime(data["Order_Date"])  # Convert to datetime
sales_trend = data.groupby("Order_Date")["Sales"].sum().reset_index()
fig4 = px.line(sales_trend, x="Order_Date", y="Sales", title="Sales Trend Over Time")
st.plotly_chart(fig4)

# Top Products by Sales
st.header("Top 10 Products by Sales")
top_products = data.groupby("Product")["Sales"].sum().nlargest(10).reset_index()
st.write(top_products)