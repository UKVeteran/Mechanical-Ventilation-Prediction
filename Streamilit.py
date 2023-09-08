import pandas as pd
import numpy as np
import streamlit as st
import requests
from bs4 import BeautifulSoup
import json
from Api_request import make_api_request

# ------- 1 - Title and info session ---------
#Title
st.title('Mechanical Ventilation Predictor')
#Subtitle
st.subheader('How does this predictor works ?')
#Aim of the predictor
st.write('The aim of this predictor is to forecast the pressure inside lungs :lungs: using differents features. Here is how it work:' )
st.write("1️⃣ First, **have a look** at the different features required")
st.write("2️⃣ Then, **select** the kind of feature that you want to provide")
st.write("3️⃣ **Provide the data** using the method of your choice")
st.write("4️⃣ Click on **'Get prediction'**	 ")
#Let's start text
"""Let's start 👇"""


#------- 2 - Explanation of Data --------
#Title
st.info('1️⃣ In order to use this predictor, you will need the following features:')
#Sentence
"""Here are the list of features use for the calculation:"""
# Making two columns with different widths
col1, col2 = st.columns([1,6])
#Filling the column 1 with the different features
with col1:
     st.write('	:small_blue_diamond: **R**')
     st.write('	:small_blue_diamond: **C**')
     st.write('	:small_blue_diamond: **u_in**')
     st.write('	:small_blue_diamond: **u_out**')
#TODO Filling the column 2 with the description of the different features
with col2:
    st.caption("Change in pressure per change in flow (air volume per time)")
    st.caption("Change in volume per change in pressure")
    st.caption("Explanation of u_in")
    st.caption("Explanation of u_out")
#Sentence
"""	:point_right: If you don't have these features, you can also use the breath_id:"""
# Making two columns with different widths
col1, col2 = st.columns([1,6])
#Filling the column 1 with breath_id
with col1:
     st.write(':small_blue_diamond: **breath_id**')
#TODO Filling the column 2 with description of breath_id
with col2:
    st.caption("Explanation of breath_id")



#------- 3 - Choose kind of features --------
#Title
st.info('2️⃣ Select the kind of data you want to provide:')

#List of three choices
button_data_provide = st.radio('Pick one:', ["I have a breath_id",
                                            "I don't have a breath_id but I have all the features",
                                            ":grey[***I don't have neither one or the other***]"],
                            )
#Conditions depending of the choices of kind of features:
if button_data_provide ==":grey[***I don't have neither one or the other***]":
    st.warning("I am sorry, you can't use this predictor")



#------- 4- General - Select the way to provide data ---------

#-------- 4-A- If the user choose "I have a breath_id", add a text field to fill and do API call --------
if button_data_provide == "I have a breath_id":
    st.info('3️⃣ Please provide your breath_id') #Title
    breath_id = st.text_input('Enter your breath_id') #Input field
    predict_with_breath_id = st.button(":blue[Get prediction]") #Button to get prediction
    if predict_with_breath_id:
        params = dict(breath_id=breath_id) #Params to send to API
        api_url = 'https://mvpapi-azdjuqy4ca-ew.a.run.app/docs#/default/predict_predict_get' #TODO API url (wrong url)
        response = requests.get(api_url, params=params).json() #TODO API response
        st.write(response) #TODO To complete once I have the API

#-------- 4-B- If the user choose "I don't have a breath_id but I have all the features", add some field to fill and do API call --------
if button_data_provide == "I don't have a breath_id but I have all the features":
    st.info('3️⃣ Please provide your features') #Title
    #Options to provide data
    data_selection = st.radio('Choose a way to provide data:', ["Provide features manually", "Import CSV"])

    # -------- 4-B-1- If user choose : provide data manually ---------
    if data_selection=="Provide features manually":
        #Creation of three columns
        col1, col2, col3 = st.columns([5,1,5])
        #Selection of R and C in two different columns
        with col1:
            R = st.slider('R value', min_value=0, max_value=50)
        with col3:
            C = st.slider('C value', min_value=0, max_value=50)
        #Creation of three columns, only for the display of dataframe
        col1, col2, col3 = st.columns([1,1,1])
        #Dataframe to fill by the user, with u_in and u_out (80 rows)
        with col2:
            df = pd.DataFrame(
            [
            {"u_in": 0, "u_out": 0},
        ]
        ) #Dataframe with only one row
            df = pd.concat([df] * 80, ignore_index=True) #We multiplicate by 80 to have 80 rows
            edited_df = st.data_editor(df) #This command will allow the user to fill the table with new values
            #Once the user click on "Get prediction", give an error if the table is empty, prediction otherwise
            if st.button("Get prediction"):
                if df.equals(edited_df): #If no modification of the table...
                    st.warning("You didn't modify the table !") # ... then we have a warning message
                else:
                    st.success('Here are your results:')
                    df = edited_df #Update the dataframe with the information provide by user
                    st.balloons() #Animation -TODO Change the animation, but maybe we can put something ?
                    u_in = df["u_in"][0] #TODO #Assign varialbe for API call (only first row here)
                    u_out = df["u_out"][0] #TODO #Assign varialbe for API call (only first row here)
                    #Prams for API
                    params = dict(
                    R=R,
                    C=C,
                    u_in=u_in,
                    u_out=u_out)
                    #API call
                    api_url = 'https://mvpapi-azdjuqy4ca-ew.a.run.app/predict' #Take one argument of u_in and u_out TODO: create a dataframe ?
                    api_response = requests.get(api_url, params=params)
                    response_text = api_response.text
                    #End of API call and display of the answer
                    try:
                        response_data = json.loads(response_text)
                        pressure = response_data.get("pressure", "")
                        st.write(f"The predicted pressure is {pressure}")
                    except json.JSONDecodeError:
                        st.warning("Unable to decode JSON response.")



    #-------- 4-B-2- Provide data using a CSV file ---------
    if data_selection=="Import CSV":
        #Tool to upload the file
        up_file = st.file_uploader("Please upload a file with 4 columns: 'R', 'C', 'u_in' and 'u_out'",
                         help="Please provide a file with 4 columns: 'R', 'C', 'u_in' and 'u_out'",
                         type=["csv"]) #Add an if condition if the file is not a csv
        if up_file:
            st.success("File upload successfully!")

        get_prediction_using_csv = st.button(":blue[Get prediction]")

        if get_prediction_using_csv:
            df_to_predict = pd.read_csv(up_file)

            list_of_pressure = []
            list_of_time_step = []
            for i in range(len(df_to_predict)):
                pressure = make_api_request(df_to_predict["R"][i],
                                df_to_predict["C"][i],
                                df_to_predict["u_in"][i],
                                df_to_predict["u_out"][i])
                if pressure is not None:
                    list_of_pressure.append(pressure)
                    list_of_time_step.append(df_to_predict["time_step"][i])
                else:
                    list_of_pressure.append("API doesnt work")

            df_predict_api = pd.DataFrame({'pressure_api': list_of_pressure, 'time_step_api': list_of_time_step})
            merged_df = pd.concat([df_predict_api, df_to_predict], axis=1)

            st.area_chart(
                    merged_df,
                    x='time_step',
                    y=["pressure", "pressure_api"], color=['#FF0000','#CCEEFF']  # Optional
                )

            st.line_chart(
                    merged_df,
                    x='time_step',
                    y=["pressure", "pressure_api"], color=['#FF0000','#CCEEFF']  # Optional
                )


        #TODO Command to read csv, a treatment
        #TODO Put a success message if its correctly load
        #TODO API call, it should look like this:
        #TODO Change the color and template of the graphe


# TODO: Take the answer of the API and plot a graph
# TODO: Take the answer of the API and display a dataframe (only if the user want, add a checkbox to ask the user)
# TODO: Put a download button (I know its possible, see doc) to download either the graph, the dataframe, or both
# TODO: Put it on internet
# TODO: Mettre quelque chose pour afficher les parties une a une
# TODO: Mettre des gifs/videos pour expliquer
# TODO: Changer le nom des variables
# TODO: Under variables, put a click image to describe on click(arrow point below)


#Creer un bouton pour telecharger les données
# If we want to add an image : st.image('./header.png')

# Use this command to plot the graphe: plot_graph = st.line_chart(df1)

# Insert out of order.



# Error message : st.error('Error message')
# Warning message : st.warning('Warning message')


#Ensuite, pour la sortie des informations, mettre un graphe, et mettre l'option "Afficher la table de prediction"
