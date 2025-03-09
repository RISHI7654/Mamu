import request

# Replace with your Facebook cookies
cookies = {
    'cookie_name': 'cookie_value',  # Replace with your actual cookie names and values
    'cookie_name2': 'cookie_value2',  # Replace with your actual cookie names and values
    # Add all necessary cookies
}

# Login using cookies
def login_with_cookies():
    url = "https://www.facebook.com"
    session = requests.Session()
    
    # Use cookies for login
    session.cookies.update(cookies)
    
    response = session.get(url)
    
    if response.status_code == 200:
        print("Logged in successfully!")
    else:
        print("Login failed!")
        
    return session

# Function to create Indra Logo with fancy text
def create_indra_logo():
    # Create a new image with a white background
    img = Image.new('RGB', (800, 400), color=(255, 255, 255))  # White background, large canvas

    # Create a drawing object
    draw = ImageDraw.Draw(img)

    # Load a fancy font (you can use any .ttf file here, make sure to place it correctly)
    try:
        font = ImageFont.truetype("arial.ttf", 100)  # You can change this to a fancy font of your choice
    except IOError:
        font = ImageFont.load_default()  # Fallback if custom font is not available
    
    # Text to display
    text = "Indra"
    text_color = (0, 102, 204)  # Blue color for the text
    
    # Position the text (centered in the image)
    text_width, text_height = draw.textsize(text, font)
    text_position = ((img.width - text_width) // 2, (img.height - text_height) // 2)
    
    # Add the text to the image
    draw.text(text_position, text, font=font, fill=text_color)

    # Save the logo as PNG
    img.save("indra_logo.png")
    print("Indra logo created successfully!")

# React to post function (with ID or Page ID)
def react_to_post(session, post_id, page_id=None):
    if page_id:
        url = f"https://graph.facebook.com/{page_id}/reactions"
        params = {
            'access_token': 'YOUR_PAGE_ACCESS_TOKEN',  # Page access token, use cookies for this
            'type': 'LIKE'
        }
    else:
        url = f"https://www.facebook.com/{post_id}/reactions"
        params = {'reaction': 'LIKE'}
    
    response = session.post(url, params=params)
    
    if response.status_code == 200:
        print("Reacted successfully!")
    else:
        print("Failed to react!")

# Comment on post function (with ID or Page ID)
def comment_on_post(session, post_id, comment, page_id=None):
    if page_id:
        url = f"https://graph.facebook.com/{page_id}/comments"
        params = {
            'access_token': 'YOUR_PAGE_ACCESS_TOKEN',  # Use page access token here
            'message': comment
        }
    else:
        url = f"https://www.facebook.com/{post_id}/comments"
        params = {'comment': comment}
    
    response = session.post(url, params=params)
    
    if response.status_code == 200:
        print("Commented successfully!")
    else:
        print("Failed to comment!")

# Poll vote function (with ID or Page ID)
def vote_on_poll(session, poll_id, option_id, page_id=None):
    if page_id:
        url = f"https://graph.facebook.com/{page_id}/polls/{poll_id}/vote"
        params = {
            'access_token': 'YOUR_PAGE_ACCESS_TOKEN',  # Use page access token here
            'option': option_id
        }
    else:
        url = f"https://www.facebook.com/{poll_id}/vote"
        params = {'option': option_id}
    
    response = session.post(url, params=params)
    
    if response.status_code == 200:
        print("Voted successfully!")
    else:
        print("Failed to vote!")

# Main function
def main():
    # Step 1: Create Indra Logo
    create_indra_logo()
    
    # Step 2: Login using cookies
    session = login_with_cookies()
    
    if session:
        # Step 3: React to a post (with or without page)
        post_id = input("Enter the post ID to react: ")
        page_id = input("Enter the Page ID (leave empty if using personal account): ")
        page_id = page_id if page_id else None
        react_to_post(session, post_id, page_id)
        
        # Step 4: Comment on the post (with or without page)
        comment = input("Enter your comment: ")
        page_id = input("Enter the Page ID for commenting (leave empty if using personal account): ")
        page_id = page_id if page_id else None
        comment_on_post(session, post_id, comment, page_id)
        
        # Step 5: Vote on a poll (with or without page)
        poll_id = input("Enter the poll ID: ")
        option_id = input("Enter the option ID to vote for: ")
        page_id = input("Enter the Page ID for voting (leave empty if using personal account): ")
        page_id = page_id if page_id else None
        vote_on_poll(session, poll_id, option_id, page_id)
    
if __name__ == "__main__":
    main()
