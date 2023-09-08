import streamlit as st
import pandas as pd
import requests
import json

def make_api_request(R, C, u_in, u_out):
    params = dict(R=R, C=C, u_in=u_in, u_out=u_out)
    #API call
    api_url = 'https://mvpapi-azdjuqy4ca-ew.a.run.app/predict'
    api_response = requests.get(api_url, params=params)
    response_text = api_response.text
    #End of API call and display of the answer
    try:
        response_data = json.loads(response_text)
        pressure = response_data.get("pressure", "")

    except json.JSONDecodeError:
        st.warning("Unable to decode JSON response.")
        pressure = None

    return pressure
