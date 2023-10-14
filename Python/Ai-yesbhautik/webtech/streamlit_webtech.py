import streamlit as st
import pandas as pd
import webtech

# Set page title and favicon
st.set_page_config(page_title="WebTech", page_icon="📱", layout="centered")

# Set the layout to wide
st.markdown(
    """
<style>
    .reportview-container .main .block-container {
        max-width: 100%;
        padding: 0rem;
    }
</style>
""",
    unsafe_allow_html=True,
)

# Input field for URL and analyze button
url = st.text_input("Enter the URL of the website you want to scan")
analyze = st.button("Analyze")

# Execute when 'Analyze' button is clicked
def analyze_website(url):
    try:
        wt = webtech.WebTech(options={"json": True})
        report = wt.start_from_url(url)
        technologies = report["technologies"]
        
        if technologies:
            df = pd.DataFrame(technologies)
            df["categories"] = df["categories"].apply(lambda x: x[0])
            df = df.rename(columns={"name": "Technology", "version": "Version", "categories": "Category"})
            df = df.sort_values(by=["Category", "Technology"]).reset_index(drop=True)

            st.dataframe(df)
        else:
            st.warning("No technologies found in the scan result.")

    except webtech.utils.ConnectionException:
        st.error("Connection error")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Main Streamlit app
if analyze:
    if not url:
        st.error("Please enter a URL")
    else:
        analyze_website(url)