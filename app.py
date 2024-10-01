from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Endpoint to get the access token from Genesys Cloud using Client Credentials
@app.route('/get-token', methods=['POST'])
def get_token():
    # Hardcoded Client ID and Client Secret for testing purposes
    client_id = "80d7c7c9-600e-478e-8d41-1bfb7b8c6bc1"
    client_secret = "BQQBxTIiCO-mY1RFm9TL0NcmhtRewKlqozD0GUdiMdE"

    # Genesys Cloud OAuth token URL (change region as needed)
    token_url = 'https://login.mypurecloud.ie/oauth/token'

    # Request payload for Client Credentials flow
    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }

    # Make request to Genesys Cloud to get the access token
    response = requests.post(token_url, data=data)

    if response.status_code == 200:
        token_data = response.json()
        return jsonify(token_data)  # Send back the token to the frontend
    else:
        error_message = response.json().get('error_description', 'Unable to fetch token')
        return jsonify({'error': error_message}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
