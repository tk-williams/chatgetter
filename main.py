from gitterpy.client import GitterClient
from gitterpy.client import GitterTokenError

# Create an instance of the Gitter client from a token received from the CLI
login_success = False
while not login_success:
    try:
        print("Please provide a valid Gitter API token")
        token = input()
        gitter = GitterClient(token)

        # Check for a valid id
        gitter.auth.get_my_id

        # If valid, the login was successful
        login_success = True
    except GitterTokenError:
        print("Invalid key. Please try again. \n")

