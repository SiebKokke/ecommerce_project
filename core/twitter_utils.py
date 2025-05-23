def post_tweet(text, image_path=None):
    """
    Mock tweet function.
    """
    print("----TWEET----")
    print(text)
    if image_path:
        print(f"Image path: {image_path}")
    print("----END----\n")
