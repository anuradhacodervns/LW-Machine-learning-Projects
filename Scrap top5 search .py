from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    if not query:
        return jsonify({'error': 'Query parameter is required'}), 400

    search_url = f'https://www.google.com/search?q={query}'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(search_url, headers=headers)
    if response.status_code != 200:
        return jsonify({'error': 'Failed to retrieve search results'}), 500

    soup = BeautifulSoup(response.text, 'html.parser')

    results = []
    for item in soup.find_all('h3', class_='zBAuLc', limit=5):
        parent = item.find_parent('a')
        title = item.get_text()
        url = parent['href']
        results.append({'title': title, 'url': url})

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
