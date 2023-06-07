import streamlit as st

import requests
from decouple import config

DJANGO_URL = config('DJANGO_URL')

# Function to reduce credits
def submit_button(user_token):

    if st.button("Reduce credits"):
        response = requests.post(DJANGO_URL + 'reduce-credits/', data={'user_token': user_token})

        if response.status_code == 200: # User is logged in and has enough credits, now you can give him his data.
            st.success("User found, and 1 credit removed.")
            st.write('Woo')
        elif response.status_code == 403: # User is logged in but doesnt have enough credits.
            st.error("Not enough credits, buy more!")
        elif response.status_code == 404: # This is when the user is not found, either his token is expired, or he tampered with the url, do not delete this it is must have for security
            st.error("User not found")
        

def main():
    query_params = st.experimental_get_query_params() # get the parameters in the url
    user_token = str(query_params['user'][0]) if "user" in query_params else None # this is the unique identificator for the django user, which we will use in our post request  to django api call.
    if user_token == None: # check if user is not logged in or doesn't have a token
        st.title("You must be logged in to access this page!")
        st.write("---")
    else:
        st.title("Hello world")
        st.write("---")

        submit_button(user_token)


if __name__ == '__main__':
    main()