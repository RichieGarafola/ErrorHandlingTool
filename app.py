import openai
import streamlit as st
import sqlite3
import datetime
# from config import *

# Set up OpenAI API credentials
openai.api_key = API_KEY

# Create a connection to the database
conn = sqlite3.connect('error_logs.db')

# Create tables to store error information if it doesn't already exist

#Error Logs
conn.execute('''CREATE TABLE IF NOT EXISTS error_logs
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  timestamp TEXT,
                  input TEXT,
                  output TEXT,
                  other_info TEXT);''')
# Runtime Errors
conn.execute('''CREATE TABLE IF NOT EXISTS runtime_errors
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  timestamp TEXT,
                  input TEXT,
                  output TEXT,
                  other_info TEXT);''')

#Logical Errors
conn.execute('''CREATE TABLE IF NOT EXISTS logical_errors
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  timestamp TEXT,
                  input TEXT,
                  output TEXT,
                  other_info TEXT);''')
# Define function to handle errors
@st.cache_data
def handle_error(error_message):
    try:
        # Call OpenAI GPT-3 API to get suggested revisions
        # model_engine = "text-davinci-002"
        model_engine = "text-curie-001" # cost effective alternative 
        prompt = f"Fix the following error message: {error_message}"
        completions = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )
        suggestion = completions.choices[0].text.strip()

        # Display suggested revision and explanation to user
        st.write("Original error message:")
        st.error(error_message)
        st.write("Suggested revision:")
        st.success(suggestion)
        st.code(suggestion)
        st.write("Here are some steps you can follow to resolve the error:")
        st.write("1. Read the error message carefully and try to understand what caused it.")
        st.write("2. Look at the suggested revision and compare it to the original error message.")
        st.write("3. Make any necessary changes to your code based on the suggested revision.")
        st.write("4. Test your code to see if the error has been resolved. If not, repeat steps 1-3 until the error is fixed.")

        # Get current date/time
        now = datetime.datetime.now()

        # Insert record into the database
        if "SyntaxError" in error_message:
            conn.execute("INSERT INTO syntax_errors (timestamp, input, output, other_info) \
                           VALUES (?, ?, ?, ?)",
                           (now.strftime("%Y-%m-%d %H:%M:%S"), error_message, suggestion, "Other relevant info here"))
        elif "NameError" in error_message:
            conn.execute("INSERT INTO runtime_errors (timestamp, input, output, other_info) \
                           VALUES (?, ?, ?, ?)",
                           (now.strftime("%Y-%m-%d %H:%M:%S"), error_message, suggestion, "Other relevant info here"))
        else:
            conn.execute("INSERT INTO logical_errors (timestamp, input, output, other_info) \
                           VALUES (?, ?, ?, ?)",
                           (now.strftime("%Y-%m-%d %H:%M:%S"), error_message, suggestion, "Other relevant info here"))


        # Commit changes
        conn.commit()

    except Exception as e:
        st.error("An error occurred while processing your request.")
        st.write(e)

# Set up Streamlit app
st.title("Error Handling Tool")
error_message = st.text_input("Enter an error message:")
if error_message:
    handle_error(error_message)
    
# Close connection
conn.close()
