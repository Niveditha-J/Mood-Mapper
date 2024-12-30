import json
from textblob import TextBlob
import emoji

# Function to analyze sentiment and map to emoji
def get_sentiment_and_emoji(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity  # Polarity: -1 (negative) to 1 (positive)

    if sentiment > 0.5:
        mood = "Very Positive 😄"
        mood_emoji = emoji.emojize(":star-struck:")
    elif sentiment > 0:
        mood = "Positive 😊"
        mood_emoji = emoji.emojize(":smiley:")
    elif sentiment == 0:
        mood = "Neutral 🤔"
        mood_emoji = emoji.emojize(":neutral_face:")
    elif sentiment > -0.5:
        mood = "Negative 😔"
        mood_emoji = emoji.emojize(":pensive_face:")
    else:
        mood = "Very Negative 😡"
        mood_emoji = emoji.emojize(":angry:")

    return mood, mood_emoji, sentiment

# Save mood data to file
def save_mood_data(mood, mood_emoji, sentiment, filename="mood_history.json"):
    try:
        # Load existing data from the file
        with open(filename, "r") as file:
            mood_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        mood_data = []

    # Add the new mood to the list
    mood_data.append({"mood": mood, "emoji": mood_emoji, "sentiment": sentiment})

    # Save updated mood data back to the file
    with open(filename, "w") as file:
        json.dump(mood_data, file, indent=4)

# Main program loop
def main():
    while True:
        print("Welcome to the Emoji Mood Mapper!")
        print("Enter some text, and I will show you your mood based on sentiment analysis.\n")

        # Take user input
        user_text = input("How are you feeling today? Write something below: ")

        # Get mood and emoji
        if user_text.strip():
            mood, mood_emoji, sentiment = get_sentiment_and_emoji(user_text)
            print(f"\n**Your Mood:** {mood}")
            print(f"**Emoji:** {mood_emoji}")
            print(f"**Sentiment Score:** {sentiment}")

            # Save to mood history
            save_mood_data(mood, mood_emoji, sentiment)

            # Ask for feedback
            feedback = input("Does this emoji represent your mood? (yes/no): ")
            if feedback.lower() == "no":
                print("Thank you for the feedback! I'll try to improve next time.")

            # Ask if they want to analyze another mood
            play_again = input("\nWould you like to analyze another mood? (yes/no): ")
            if play_again.lower() != "yes":
                print("Thank you for using the Emoji Mood Mapper! Goodbye!")
                break
        else:
            print("\nYou did not enter any text. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
