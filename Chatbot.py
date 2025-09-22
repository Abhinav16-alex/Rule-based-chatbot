# Rule-Based Chatbot using if-else statements
# Task 8: Python Developer - BroskiesHub

import re
import random
from datetime import datetime

class SimpleChatbot:
    def __init__(self):
        self.name = "BroskieBot"
        self.user_name = ""
        
    def greet_user(self):
        """Initial greeting and get user name"""
        print(f"🤖 Hello! I'm {self.name}, your friendly chatbot!")
        print("Let's have a conversation. Type 'bye' or 'exit' to end our chat.\n")
        
        while not self.user_name:
            name_input = input("What's your name? ").strip()
            if name_input:
                self.user_name = name_input.title()
                print(f"Nice to meet you, {self.user_name}! 😊\n")
                break
            else:
                print("Please tell me your name!")
    
    def process_input(self, user_input):
        """Process user input and generate appropriate response"""
        # Convert to lowercase for easier matching
        user_input_lower = user_input.lower().strip()
        
        # Exit conditions
        if user_input_lower in ['bye', 'exit', 'quit', 'goodbye']:
            return "exit"
        
        # Greeting responses
        elif any(greeting in user_input_lower for greeting in ['hello', 'hi', 'hey', 'greetings']):
            responses = [
                f"Hello again, {self.user_name}! How can I help you?",
                f"Hey there, {self.user_name}! What's on your mind?",
                f"Hi {self.user_name}! Great to chat with you!"
            ]
            return random.choice(responses)
        
        # How are you responses
        elif any(phrase in user_input_lower for phrase in ['how are you', 'how do you do', 'whats up']):
            responses = [
                "I'm doing great, thanks for asking! How about you?",
                "I'm fantastic! Ready to help you with anything.",
                "I'm doing well! What brings you here today?"
            ]
            return random.choice(responses)
        
        # Name related questions
        elif any(phrase in user_input_lower for phrase in ['your name', 'who are you', 'what are you']):
            return f"I'm {self.name}, a rule-based chatbot created to help and chat with you!"
        
        # Time related questions
        elif any(word in user_input_lower for word in ['time', 'date', 'today']):
            current_time = datetime.now()
            if 'time' in user_input_lower:
                return f"The current time is {current_time.strftime('%I:%M %p')}"
            elif 'date' in user_input_lower or 'today' in user_input_lower:
                return f"Today is {current_time.strftime('%B %d, %Y')}"
        
        # Help requests
        elif any(word in user_input_lower for word in ['help', 'assist', 'support']):
            return """I can help you with:
• General conversation and questions
• Telling you the time or date
• Simple math calculations
• Just chatting about your day
What would you like to talk about?"""
        
        # Math calculations (simple)
        elif any(op in user_input_lower for op in ['+', '-', '*', '/', 'calculate', 'math']):
            try:
                # Extract numbers and operators for basic math
                if '+' in user_input_lower:
                    numbers = re.findall(r'\d+', user_input)
                    if len(numbers) >= 2:
                        result = int(numbers[0]) + int(numbers[1])
                        return f"The result is: {result}"
                elif '-' in user_input_lower:
                    numbers = re.findall(r'\d+', user_input)
                    if len(numbers) >= 2:
                        result = int(numbers[0]) - int(numbers[1])
                        return f"The result is: {result}"
                elif '*' in user_input_lower:
                    numbers = re.findall(r'\d+', user_input)
                    if len(numbers) >= 2:
                        result = int(numbers[0]) * int(numbers[1])
                        return f"The result is: {result}"
                return "I can do simple math! Try: '5 + 3' or 'calculate 10 - 4'"
            except:
                return "Sorry, I couldn't understand that math problem. Try something like '5 + 3'"
        
        # Compliments
        elif any(word in user_input_lower for word in ['good', 'great', 'awesome', 'nice', 'cool']):
            responses = [
                "Thank you! That's very kind of you to say! 😊",
                "I appreciate the compliment! You're pretty great too!",
                "Thanks! You just made my day better!"
            ]
            return random.choice(responses)
        
        # Questions about feelings
        elif any(phrase in user_input_lower for phrase in ['how do you feel', 'are you happy', 'are you sad']):
            responses = [
                "As a chatbot, I don't have feelings like humans, but I enjoy our conversations!",
                "I'm always happy to chat and help people like you!",
                "I feel great when I can be helpful and have good conversations!"
            ]
            return random.choice(responses)
        
        # Weather (mock response since we can't get real weather)
        elif 'weather' in user_input_lower:
            responses = [
                "I don't have access to real weather data, but I hope it's nice where you are!",
                "Sorry, I can't check the weather, but I hope you're having a beautiful day!",
                "I wish I could tell you the weather! Maybe try a weather app?"
            ]
            return random.choice(responses)
        
        # Thank you responses
        elif any(phrase in user_input_lower for phrase in ['thank you', 'thanks', 'appreciate']):
            responses = [
                "You're very welcome! Happy to help!",
                "No problem at all! Anytime!",
                "My pleasure! That's what I'm here for!"
            ]
            return random.choice(responses)
        
        # Default responses for unrecognized input
        else:
            default_responses = [
                "That's interesting! Tell me more about that.",
                "I'm not sure I understand completely. Could you explain that differently?",
                "Hmm, that's a new one for me! Can you give me more details?",
                f"Sorry {self.user_name}, I didn't quite catch that. Could you rephrase?",
                "I'm still learning! Could you try asking that in a different way?",
                "That sounds fascinating! I wish I knew more about that topic."
            ]
            return random.choice(default_responses)
    
    def run_chatbot(self):
        """Main chatbot loop"""
        self.greet_user()
        
        print("💬 Start chatting! (Type 'bye' to exit)")
        print("-" * 50)
        
        while True:
            try:
                # Get user input
                user_input = input(f"{self.user_name}: ").strip()
                
                # Check if user wants to exit
                if not user_input:
                    print("Please say something! 😊")
                    continue
                
                # Process the input and get response
                response = self.process_input(user_input)
                
                # Check for exit condition
                if response == "exit":
                    print(f"\n🤖 {self.name}: Goodbye, {self.user_name}! It was great chatting with you! 👋")
                    print("Have a wonderful day!")
                    break
                
                # Display chatbot response
                print(f"🤖 {self.name}: {response}\n")
                
            except KeyboardInterrupt:
                print(f"\n\n🤖 {self.name}: Goodbye, {self.user_name}! Thanks for chatting! 👋")
                break
            except Exception as e:
                print(f"🤖 {self.name}: Oops! Something went wrong. Let's keep chatting! 😊\n")

def main():
    """Main function to run the chatbot"""
    print("=" * 60)
    print("    WELCOME TO BROSKIEBOT - RULE BASED CHATBOT")
    print("    Task 8: Python Developer Interview")
    print("=" * 60)
    
    # Create and run the chatbot
    bot = SimpleChatbot()
    bot.run_chatbot()
    
    print("\nThanks for using BroskieBot! 🚀")

if __name__ == "__main__":
    main()
