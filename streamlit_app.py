

import streamlit as st
import pandas as pd

# Read the clustered data and pivot table
df = pd.read_csv("Clustered_data.csv")
pivot_total = pd.read_csv("Clustered_pivot.csv")

def get_recommendations(user_id , num_recommendations):
    # Check if the user exists in the data
    if df["User_Id"].isin([int(user_id)]).any():
    # Get the cluster assigned to the user
        cluster = df.loc[df["User_Id"] == int(user_id) , "Cluster"].unique()[0]
    
    # Filter the data for the user's cluster and calculate the sum of transaction values
        recommendations = df.loc[df["Cluster"] == cluster].groupby("Mer_Id")["Trx_Vlu"].sum().nlargest(int(num_recommendations))
    
        return recommendations
    else:
        return None

def main():
    # set the title of the streamlit app
    st.title("Loyalty Rewards: Personalized Recommendations")
    # User input for user ID and number of recommendations
    user_id = st.text_input("Enter User Id")
    num_recommendations = st.text_input("Enter number of recommendations")
    
    # Button to trigger recommendation generation
    if st.button("Recommend"):
        recommendations = get_recommendations(user_id , num_recommendations)
        
    # Check if the user exists
        if recommendations is not None:
    # Display the recommendations
            for index , mer_id in enumerate(recommendations.index):
                st.text(f"Recommendation number {index + 1} for user {user_id} is {mer_id}")
        else:
            st.text("User not found")

main()
