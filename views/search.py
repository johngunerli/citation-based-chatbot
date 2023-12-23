import streamlit as st
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
import os
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
load_dotenv()
import ssl
import urllib3
import re

# Disable SSL verification
urllib3.disable_warnings()
ssl._create_default_https_context = ssl._create_unverified_context

def load_view():
    
    # Azure Cognitive Search credentials
    search_service = os.getenv("SEARCH_ENDPOINT")
    index_name = os.getenv("AZURE_SEARCH_INDEX_NAME")
    api_key = os.getenv("SEARCH_KEY")

    # Initialize Azure Cognitive Search client
    credential = AzureKeyCredential(api_key)
    search_client = SearchClient(endpoint=search_service, index_name=index_name, credential=credential)

    def search_azure(query):
        results = search_client.search(search_text=query)
        return results

    st.title("Azure Cognitive Search Streamlit App")

    user_query = st.text_input("Enter your query:", value="Type here...")
    
    if st.button("Search"):
        with st.spinner('Searching...'):
            search_results = search_azure(user_query)
            search_results_list = list(search_results)  # Convert SearchItemPaged to list
            results_count = len(search_results_list)  # Get the count of results
            st.write(f'Number of results: {results_count}')  # Display the count of results
            for result in search_results_list:
                content = result.get('content', '')  # Extracting content from the result
                pages = re.split(r'\\t\d+\\t', content)  # Splitting content into pages
                pages = [page for page in pages if page]  # Removing any empty strings
                for i, page in enumerate(pages, start=1):  # Creating expanders for each page
                    with st.expander(f'Excerpt'):
                        # Replace escape sequences with their character representations
                        page_content = page.replace('\\n', '\n').replace('\\t', '\t')
                        st.write(page_content)

