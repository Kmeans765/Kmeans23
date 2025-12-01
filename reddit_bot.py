import praw
import time
import os
from dotenv import load_dotenv

# Load environment variables (API keys)
# Ensure you have a .env file with these values
load_dotenv()

def create_reddit_instance():
    """
    Creates and authenticates a Reddit instance using PRAW.
    """
    try:
        reddit = praw.Reddit(
            client_id=os.getenv("REDDIT_CLIENT_ID"),
            client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
            user_agent="KMTechSolutions_Bot/1.0",
            username=os.getenv("REDDIT_USERNAME"),
            password=os.getenv("REDDIT_PASSWORD")
        )
        print(f"Authenticated as: {reddit.user.me()}")
        return reddit
    except Exception as e:
        print(f"Error authenticating: {e}")
        return None

def run_bot(reddit, subreddit_name, search_keywords):
    """
    Monitors a subreddit for new posts containing specific keywords.
    """
    print(f"Monitoring r/{subreddit_name} for keywords: {search_keywords}...")

    subreddit = reddit.subreddit(subreddit_name)

    # stream.submissions() gets new posts in real-time
    for submission in subreddit.stream.submissions(skip_existing=True):
        try:
            # Check if keyword exists in title or body (case insensitive)
            title_text = submission.title.lower()
            body_text = submission.selftext.lower()

            if any(keyword in title_text or keyword in body_text for keyword in search_keywords):
                print(f"\nMatch found! Post: {submission.title}")
                print(f"Link: {submission.url}")

                # TODO: Add your logic here (e.g., comment, send DM, save to DB)
                # Example:
                # submission.reply("This sounds like a job for KM Tech Solutions! DM me if you need help.")

        except Exception as e:
            print(f"Error processing submission: {e}")

if __name__ == "__main__":
    # Configuration
    SUBREDDIT = "python"  # Change to target subreddit
    KEYWORDS = ["help", "error", "bug", "script"]

    reddit_instance = create_reddit_instance()

    if reddit_instance:
        run_bot(reddit_instance, SUBREDDIT, KEYWORDS)
