import streamlit as st
from config import load_config, get_language_config
import os

def initialize_session_state():
    """Initialize session state variables if they don't exist."""
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "current_data" not in st.session_state:
        st.session_state.current_data = None
    if "current_query" not in st.session_state:
        st.session_state.current_query = ""
    if "language" not in st.session_state:
        st.session_state.language = "da"  # Default to Danish

def create_sidebar():
    """Create and populate the sidebar."""
    with st.sidebar:
        st.title("Settings")
        
        # Language selector
        lang = st.selectbox(
            "Language / Sprog",
            options=["Danish / Dansk", "English"],
            index=0
        )
        st.session_state.language = "da" if "Danish" in lang else "en"
        
        # Add some information about the app
        st.subheader("About")
        st.markdown(
            "This application provides access to Statistics Denmark data through "
            "natural language queries. Ask any question about Danish statistics "
            "and get interactive visualizations."
        )
        
        # Add some example queries
        st.subheader("Example Queries")
        example_queries = [
            "What is the population of Denmark?",
            "Show unemployment rates for the last 5 years",
            "Compare GDP growth across different regions"
        ]
        
        for query in example_queries:
            if st.button(query):
                st.session_state.current_query = query

def chat_interface():
    """Display the chat interface."""
    # Display chat history
    for message in st.session_state.chat_history:
        role = message["role"]
        content = message["content"]
        
        with st.chat_message(role):
            st.markdown(content)
    
    # Chat input
    user_query = st.chat_input("Ask a question about Danish statistics...")
    
    # If there's input from chat_input or a query was selected from examples
    if user_query or st.session_state.current_query:
        # Prioritize direct input over selected examples
        query = user_query if user_query else st.session_state.current_query
        st.session_state.current_query = ""  # Reset current_query
        
        # Add user message to chat history
        st.session_state.chat_history.append({"role": "user", "content": query})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(query)
        
        # Process query and generate response (placeholder for now)
        with st.chat_message("assistant"):
            with st.spinner("Searching for data..."):
                # This will be replaced with actual query processing in later steps
                response = f"I'll help you find information about: {query}\n\nThis is a placeholder response. The actual data retrieval and analysis will be implemented in future steps."
                st.markdown(response)
        
        # Add assistant response to chat history
        st.session_state.chat_history.append({"role": "assistant", "content": response})

def main():
    """Main application entry point."""
    # Load configuration
    config = load_config()
    lang_config = get_language_config(config)
    
    # Set page configuration
    st.set_page_config(
        page_title="Statistics Denmark Explorer",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Initialize session state
    initialize_session_state()
    
    # Create sidebar
    create_sidebar()
    
    # Main content area
    st.title("Statistics Denmark Data Explorer")
    st.markdown("Ask questions about Danish statistics and get interactive visualizations.")
    
    # Chat interface
    chat_interface()
    
    # Placeholder for future data display
    if st.session_state.current_data is not None:
        st.subheader("Data Preview")
        st.info("Data visualization will be implemented in future steps.")

if __name__ == "__main__":
    main() 