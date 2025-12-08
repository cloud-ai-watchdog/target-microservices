import streamlit as st
import requests

st.title("Microservices Interaction")

backend_url = "http://target-backend-service:80"

if st.button("Checksum News"):
    response = requests.post(f"{backend_url}/checksum-news/", json=["ai", "machine learning"])
    st.write(response.json())

if st.button("Checksum Images"):
    response = requests.post(f"{backend_url}/checksum-images-news/", json=["cat", "dog"])
    st.write(response.json())

if st.button("Checksum Files"):
    response = requests.post(f"{backend_url}/checksum-files/?depth=2")
    st.write(response.json())
