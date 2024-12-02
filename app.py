from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load the CSV file
csv_file_path = 'amazon.csv'
data = pd.read_csv(csv_file_path)

# Define the homepage route
@app.route('/')
def index():
    return render_template('index.html')

# Define the search API route
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').lower()
    if not query:
        return jsonify([])
    
    # Filter the products based on the query
    filtered = data[data['Name'].str.lower().str.contains(query, na=False)]
    results = filtered[['Name', 'discounted_price', 'actual_price', 'rating', 'img_link', 'product_link']].to_dict(orient='records')
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
