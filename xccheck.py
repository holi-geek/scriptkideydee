import requests
from bs4 import BeautifulSoup

def main():
    # Get the website URL from the user.
    website_url = input("Enter the website URL: ")

    # Make a request to the website.
    response = requests.get(website_url)

    # Parse the response as HTML.
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all of the forms on the page.
    forms = soup.find_all("form")

    # For each form, check if it is vulnerable to XSS.
    for form in forms:
        # Get the form action.
        action = form.attrs.get("action")

        # If the form action is a URL, check if it is vulnerable to XSS.
        if action is not None:
            # Check if the form action contains any of the following characters:
            # <, >, ", ', &
            if any([c in action for c in ["<", ">", "\"", "'", "&"]]):
                print("The form at {} is vulnerable to XSS.".format(action))

if __name__ == "__main__":
    main()
