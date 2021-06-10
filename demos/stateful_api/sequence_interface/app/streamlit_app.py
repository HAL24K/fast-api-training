import streamlit as st

import numpy as np
import requests
import json

# Base URI of the Sequencer API
root_uri = "http://web_api:80"

def get_latest_data():
    response = requests.get(f"{root_uri}/sequence")
    return response.json()


def add_number_to_sequence(number):
    response = requests.post(f"{root_uri}/sequence/add_to_last/{int(number)}")


def load_local_cache():
    with open("local_numbers.json", "r") as numbers_file:
        numbers = json.load(numbers_file)
        return numbers

def save_local_cache(my_numbers):
    with open("local_numbers.json", "w") as numbers_file:
        numbers = json.dump(my_numbers, numbers_file)


def reset_local_cache():
    with open("local_numbers.json", "w") as numbers_file:
        numbers = json.dump({"number_list": [0]}, numbers_file)


my_numbers = load_local_cache()

st.title("Sequence API Interface")

st.subheader("Submit a new number")
with st.form(key="my_submit_form"):
    number_input = st.number_input(label="Enter an integer value", step=1)
    submit_button = st.form_submit_button(label="Submit")
    if submit_button:
        add_number_to_sequence(number_input)
        my_numbers.get("number_list").append(number_input)
        save_local_cache(my_numbers)

    clear_button = st.form_submit_button(label="Clear sequence")
    if clear_button:
        response = requests.delete(f"{root_uri}/sequence")
        reset_local_cache()

data = get_latest_data()

st.subheader("Current Sequence in Memory")
st.write(', '.join([str(i) for i in data]))

st.subheader("Last 10 numbers submitted to the sequence")
st.write(", ".join([str(i) for i in my_numbers.get("number_list", [])[0:10]]))

st.subheader("Cumulative sum of submitted sequence (last 10)")
data = np.cumsum(my_numbers.get("number_list", []))
st.write(", ".join(str(i) for i in data[-10:]))

st.button(label="Refresh page")