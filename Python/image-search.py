from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace with your own Unsplash API access key
UNSPLASH_ACCESS_KEY = "your_access_key"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    query = request.form['query']
    if not query:
        return "No query provided for search."

    url = f"https://api.unsplash.com/search/photos"
    headers = {"Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"}
    params = {"query": query}
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Check for any HTTP error
        data = response.json()
        image_urls = [result['urls']['regular'] for result in data['results']]
        return render_template('result.html', image_urls=image_urls, query=query)
    except requests.RequestException as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)
