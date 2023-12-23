# Introduction

This project is a Streamlit-based web application designed for chat and search functionalities. It integrates services like OpenAI for chatbot features and Azure for search capabilities, providing a user-friendly interface for interaction.

# Installation

To set up this project, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone [repository-url]

Install Requirements:
Navigate to the project directory and install the required Python packages:

```
pip install -r requirements.txt
```

To run the application:

Set Environment Variables:
Ensure that all necessary environment variables are set, as required by chat.py and search.py.

Start the Streamlit App:
Run the following command in the project directory:

```
streamlit run main.py
```

The application should now be running on your local server, typically at <http://localhost:8501>.

# Structure

main.py: Main Streamlit app entry point.

PATHS.py: Defines navigation paths for the app routing.

utils.py: Contains utility functions for the app.

home.py: Manages the home page view.

chat.py: Handles chat functionalities using OpenAI.

search.py: Manages search features using Azure services.

styles.css: CSS file for styling the Streamlit interface.
