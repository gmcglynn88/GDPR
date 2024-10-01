from flask import Flask, jsonify, request
import requests
import os

app = Flask(__name__)

# Endpoint to get the access token from Genesys Cloud using Client Credentials
@app.route('/get-token', methods=['POST'])
def get_token():
    client_id = request.json.get('client_id')
    client_secret = request.json.get('client_secret')

    # Genesys Cloud OAuth token URL (change region as needed)
    token_url = 'https://login.mypurecloud.ie/oauth/token'

    # Request payload for Client Credentials flow
    data = {
        'grant_type': 'client_credentials',
        'client_id': "80d7c7c9-600e-478e-8d41-1bfb7b8c6bc1",
        'client_secret': "BQQBxTIiCO-mY1RFm9TL0NcmhtRewKlqozD0GUdiMdE"
    }

    # Make request to Genesys Cloud to get the access token
    response = requests.post(token_url, data=data)
    
    if response.status_code == 200:
        token_data = response.json()
        return jsonify(token_data)  # Send back the token to the frontend
    else:
        return jsonify({'error': 'Unable to fetch token'}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
