import time

def greet():
    print("Hello! I'm here to help you relieve stress. How are you feeling today?")
    feeling = input("Please describe your current mood (e.g., happy, sad, stressed): ").lower()

    # Mapping the user mood to respective suggestions
    if feeling in ["happy", "good", "great", "awesome", "excited"]:
        happy()
    elif feeling in ["sad", "down", "unhappy", "depressed"]:
        sad()
    elif feeling in ["stressed", "overwhelmed", "anxious", "burnt out"]:
        stressed()
    elif feeling in ["angry", "irritated", "frustrated"]:
        angry()
    elif feeling in ["bored", "uninspired", "listless"]:
        bored()
    elif feeling in ["hopeful", "motivated", "optimistic"]:
        hopeful()
    else:
        print("I'm not sure I understand how you're feeling. Can you tell me more?")
    return feeling

# Functions for mood-specific suggestions
def happy():
    print("\nThat's great! Here are some things you can do to celebrate your happiness:")
    time.sleep(0.5)
    print("- Share your joy with a friend or family member.")
    time.sleep(0.5)
    print("- Do something you love, like listening to music.")
    time.sleep(0.5)
    print("- Celebrate your happiness by treating yourself!")
    time.sleep(0.5)
    print("- Try something new that excites you!")
    
def sad():
    print("\nI'm here for you. Here are some things that might help lift your spirits:")
    time.sleep(0.5)
    print("- Talk to someone you trust about what's bothering you.")
    time.sleep(0.5)
    print("- Watch a feel-good movie or listen to uplifting music.")
    time.sleep(0.5)
    print("- Write in a journal to process your emotions.")
    time.sleep(0.5)
    print("- Take a warm bath or engage in some self-care.")
    time.sleep(0.5)
    print("- Try doing a creative activity like drawing or painting.")

def stressed():
    print("\nTake a deep breath. Here are some stress-relief activities you can try:")
    time.sleep(0.5)
    print("- Take a short walk to clear your mind.")
    time.sleep(0.5)
    print("- Practice deep breathing exercises or try meditation.")
    time.sleep(0.5)
    print("- Organize your workspace for a sense of control.")
    time.sleep(0.5)
    print("- Listen to calming music or nature sounds.")
    time.sleep(0.5)
    print("- Try some yoga or stretching exercises to release tension.")
    
def angry():
    print("\nIt's okay to feel angry. Here are some ways to calm down:")
    time.sleep(0.5)
    print("- Take a break and step away from the situation.")
    time.sleep(0.5)
    print("- Try deep breathing exercises or progressive muscle relaxation.")
    time.sleep(0.5)
    print("- Go for a run or engage in another physical activity.")
    time.sleep(0.5)
    print("- Express your feelings through writing or talking to someone.")
    time.sleep(0.5)
    print("- Practice mindfulness or listen to calming music.")

def bored():
    print("\nBoredom can be an opportunity to explore new things. Try these:")
    time.sleep(0.5)
    print("- Try a new hobby or revisit an old one.")
    time.sleep(0.5)
    print("- Read a book or watch an interesting documentary.")
    time.sleep(0.5)
    print("- Call or meet up with a friend to break the monotony.")
    time.sleep(0.5)
    print("- Start a creative project, like drawing, writing, or crafting.")
    time.sleep(0.5)
    print("- Explore something you've always wanted to learn, like a new language.")

def hopeful():
    print("\nThat's wonderful! Here are some ideas to channel your optimism:")
    time.sleep(0.5)
    print("- Set new goals for yourself and take steps towards achieving them.")
    time.sleep(0.5)
    print("- Help someone else by volunteering or supporting a cause you care about.")
    time.sleep(0.5)
    print("- Share your positivity with others and encourage them.")
    time.sleep(0.5)
    print("- Start a new project or dive into something you're passionate about.")
    time.sleep(0.5)
    print("- Reflect on your progress and the positive things in your life.")

# Main loop
def main():
    print("Welcome to your personal stress relief assistant!")
    greet()
       

if __name__ == "__main__":
    main()
