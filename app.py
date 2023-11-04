import pandas as pd
import streamlit as st
import plotly.express as px

# Read the CSV data
data = pd.read_csv(r"C:\Users\laksh\Downloads\Processed_sales_data (1).csv")
df = pd.DataFrame(data)

st.title("Electronic Sales")

# Group the data by "State" and sum the "Sales"
df2 = df.groupby("State")["Sales"].agg('sum')

# Define a mapping of state names to state codes
state_mapping = {
    'CALIFORNIA': 'CA',
    'GEORGIA': 'GA',
    'MASSACHUSETTS': 'MA',
    'MAINE': 'ME',
    'NEW YORK': 'NY',
    'OREGON': 'OR',
    'TEXAS': 'TX',
    'WASHINGTON': 'WA'
}

# Create a dropdown menu for selecting a state
selected_state = st.selectbox("Select a State:", list(state_mapping.keys()))

if selected_state:
    selected_state_code = state_mapping.get(selected_state, None)

    if selected_state_code:
        st.success(f"{selected_state} Sales: {df2.loc[selected_state_code]}")

        # Filter the data for the selected state
        selected_state_data = df[df["State"] == selected_state_code]

        # Group the data by product and sum the sales
        product_sales = selected_state_data.groupby("Product")["Sales"].agg('sum').reset_index()

        # Sort the products by sales in descending order
        product_sales = product_sales.sort_values(by="Sales", ascending=False)

        # Create a bar chart
        fig = px.bar(product_sales, x="Product", y="Sales", title=f"Product Sales in {selected_state}")
        st.plotly_chart(fig)
    else:
        st.error(f"No data found for selected state: {selected_state}")
