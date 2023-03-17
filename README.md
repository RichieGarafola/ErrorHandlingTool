# Error Handling Tool

A simple web application built with Streamlit that utilizes OpenAI's GPT-3 API to provide suggested revisions for error messages. The app also stores all error logs in an SQLite database.

---

Welcome to the Error Handling Tool!

This tool was designed with students in mind, specifically those who are just starting out in programming and may struggle with debugging their code. As anyone who has spent time coding can attest, errors are a common occurrence, and can be incredibly frustrating to deal with. Often, the error messages themselves can be cryptic and unhelpful, leaving the programmer scratching their head and wondering where to even begin.

That's where the Error Handling Tool comes in. By leveraging the power of OpenAI's GPT-3 language model, this tool can suggest revisions to error messages, giving students a starting point for debugging their code. Additionally, the tool provides guidance on how to approach the error and steps to take to resolve it.

The Error Handling Tool isn't just about fixing code, though. It's about empowering students to take control of their own learning and build their problem-solving skills. By providing a clear and straightforward process for debugging errors, students can become more confident in their ability to tackle programming challenges.

Whether you're a seasoned programmer or just starting out, the Error Handling Tool is here to help you on your journey. So go ahead and give it a try - you might just be surprised at how much easier debugging can be with a little help from AI!



## Installation
1. Clone the repository:

    git clone https://github.com/RichieGarafola/ErrorHandlingTool.git

---

2. Navigate to the project directory:

    cd ErrorHandlingTool
    
3. Install the required packages:
    pip install -r requirements.txt

4. Set up your OpenAI API credentials. You will need an API key, which you can obtain from the OpenAI website.

5. Set up the database by running init_db.py. This will create an SQLite database file error_logs.db in the project directory.

    python init_db.py

---

## Usage

1. Start the app:

    streamlit run app.py

2. Enter an error message in the input field and click the "Submit" button.

3. The app will display the original error message, a suggested revision generated by the GPT-3 API, and steps to follow to resolve the error.

4. The app will also log the error message, suggested revision, timestamp, and any other relevant information in the SQLite database.

---

## Built With
Streamlit - The web framework used
OpenAI API - The natural language processing API used
SQLite - The database used to store error logs

---

## Contributing
Contributions are welcome. Please open an issue or submit a pull request if you would like to contribute.

---

## License
This project is licensed under the MIT License.

---

### Acknowledgements
Streamlit documentation
OpenAI GPT-3 API documentation
SQLite documentation
