import base64

# Define the variables
api_user = 'f1631760-2cd8-4003-b61c-1ec3954e5575'
api_key = 'dee615e9ba784c72b8d82d978cd9a236'
# Combine the user and key into the auth string
auth = f'{api_user}:{api_key}'

# Encode the auth string in base64
credentials = base64.b64encode(auth.encode('utf-8')).decode('utf-8')

# Print the credentials
print(credentials)
