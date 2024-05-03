import streamlit as st
# import csv
# import datetime
import snowflake.connector

def main():
    
    # Retrieve client's name from session state
    client_name = st.session_state.client_name

    # Retrieve selected solution from session state
    selected_solution = st.session_state.selected_solution

    if selected_solution == "ILA":
        # Retrieve user inputs from session state
        user_inputs_ILA_sa = st.session_state.user_inputs_ILA_sa
    elif selected_solution == "Gen AI":
        # Retrieve user inputs from session state
        user_inputs_Gen_AI_sa = st.session_state.user_inputs_Gen_AI_sa
    
    st.title(f"Overview Summary for *{client_name}*")
 
    # Retrieve captured data from session state
    high_importance_oc = st.session_state.get("high_importance_oc", [])
    moderate_importance_oc = st.session_state.get("moderate_importance_oc", [])
    low_importance_oc = st.session_state.get("low_importance_oc", [])

    high_importance_md = st.session_state.get("high_importance_md", [])
    moderate_importance_md = st.session_state.get("moderate_importance_md", [])
    low_importance_md = st.session_state.get("low_importance_md", [])

    high_importance_mdp = st.session_state.get("high_importance_mdp", [])
    moderate_importance_mdp = st.session_state.get("moderate_importance_mdp", [])
    low_importance_mdp = st.session_state.get("low_importance_mdp", [])

    user_inputs_ILA_sa = st.session_state.get("user_inputs_ILA_sa",[])
    user_inputs_Gen_AI_sa = st.session_state.get("user_inputs_Gen_AI_sa",[])

    st.subheader("Key Challenges - Overall Challenges :")

    st.markdown("**High Importance:**")
    for input in high_importance_oc:
        st.write(input)

    st.markdown("**Moderate Importance:**")
    for input in moderate_importance_oc:
        st.write(input)

    st.markdown("**Low Importance:**")
    for input in low_importance_oc:
        st.write(input)

    st.subheader("Key Challenges - Master Data :")
    st.markdown("**High Importance:**")
    for input in high_importance_md:
        st.write(input)

    st.markdown("**Moderate Importance:**")
    for input in moderate_importance_md:
        st.write(input)

    st.markdown("**Low Importance:**")
    for input in low_importance_md:
        st.write(input)

    st.subheader("Key Challenges - MDP :")
    st.markdown("**High Importance:**")
    for input in high_importance_mdp:
        st.write(input)

    st.markdown("**Moderate Importance:**")
    for input in moderate_importance_mdp:
        st.write(input)

    st.markdown("**Low Importance:**")
    for input in low_importance_mdp:
        st.write(input)
    
    if selected_solution =="ILA":
        st.subheader("**Solution Aspects** :")
        for input in user_inputs_ILA_sa:
            st.write(input)
    elif selected_solution == "Gen AI":
        st.subheader("**Solution Aspects** :")
        for input in user_inputs_Gen_AI_sa:
            st.write(input)       

    if selected_solution == "ILA":
        # Export to Snowflake when the submit button is clicked
        if st.button("Export to Snowflake"):
            export_to_snowflake(client_name, selected_solution, high_importance_oc, moderate_importance_oc, low_importance_oc, high_importance_md, moderate_importance_md, low_importance_md, high_importance_mdp, moderate_importance_mdp, low_importance_mdp, user_inputs_ILA_sa)
    elif selected_solution == "Gen AI":
        if st.button("Export to Snowflake"):
            export_to_snowflake(client_name, selected_solution, high_importance_oc, moderate_importance_oc, low_importance_oc, high_importance_md, moderate_importance_md, low_importance_md, high_importance_mdp, moderate_importance_mdp, low_importance_mdp, user_inputs_Gen_AI_sa)

def export_to_snowflake(client_name, selected_solution, high_importance_oc, moderate_importance_oc, low_importance_oc, high_importance_md, moderate_importance_md, low_importance_md, high_importance_mdp, moderate_importance_mdp, low_importance_mdp, user_inputs):
    # Connect to Snowflake
    conn = snowflake.connector.connect(
        user='PIETERRETIEF',
        password='Snow4261!',
        account='NC34438',
        warehouse='COMPLUTE_WH',
        database='STREAMLIT_APPS',
        schema='PUBLIC'
    )

    # Prepare data for insertion
    data = [
        (client_name, selected_solution, "High Importance", "\n".join(high_importance_oc)),
        (client_name, selected_solution, "Moderate Importance", "\n".join(moderate_importance_oc)),
        (client_name, selected_solution, "Low Importance", "\n".join(low_importance_oc)),
        (client_name, selected_solution, "High Importance", "\n".join(high_importance_md)),
        (client_name, selected_solution, "Moderate Importance", "\n".join(moderate_importance_md)),
        (client_name, selected_solution, "Low Importance", "\n".join(low_importance_md)),
        (client_name, selected_solution, "High Importance", "\n".join(high_importance_mdp)),
        (client_name, selected_solution, "Moderate Importance", "\n".join(moderate_importance_mdp)),
        (client_name, selected_solution, "Low Importance", "\n".join(low_importance_mdp)),
        (client_name, selected_solution, "User Inputs", "\n".join(user_inputs))
    ]

    # Insert data into Snowflake
    try:
        cursor = conn.cursor()
        cursor.executemany("""
            CREATE TABLE IF NOT EXISTS LLM_Proposal (Client_Name, Selected_Solution, Importance_Level, Details);
            GO
            INSERT INTO LLM_Proposal (Client_Name, Selected_Solution, Importance_Level, Details)
            VALUES (%s, %s, %s, %s)
        """, data)
        cursor.close()
        conn.commit()
        st.success("Data successfully exported to Snowflake!")
    except Exception as e:
        st.error(f"Error exporting data to Snowflake: {str(e)}")
    finally:
        conn.close()

if __name__ == "__main__":
    main()


