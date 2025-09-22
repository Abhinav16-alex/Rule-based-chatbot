#  BroskieBot - Rule-Based Chatbot

**Task 8: Python Developer Interview Challenge**

A simple, friendly rule-based chatbot built using Python if-else statements for natural language processing and user interaction.

##  Project Overview

**Objective:** Create a rule-based chatbot that can engage in basic conversations with users.

**Tools:** Python 3.x

**Deliverable:** A Python script that simulates an interactive chatbot experience.

## Features

- **Personalized Interaction**: Remembers and uses user's name throughout the conversation
- **Multiple Response Types**: Handles greetings, questions, math calculations, and general chat
- **Randomized Responses**: Provides varied responses to avoid repetitive interactions
- **Error Handling**: Graceful handling of unexpected inputs and errors
- **Clean Exit**: Multiple ways to end the conversation politely
- **Time/Date Information**: Can tell current time and date
- **Basic Math**: Performs simple arithmetic calculations
- **Friendly Personality**: Engaging and helpful conversational style

## Installation & Setup

### Prerequisites
- Python 3.6 or higher
- No external libraries required (uses only built-in Python modules)

### Quick Start

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/broskiebot-chatbot.git
cd broskiebot-chatbot
```

2. **Run the chatbot:**
```bash
python chatbot.py
```

3. **Start chatting:**
   - Type your messages and press Enter
   - Type 'bye', 'exit', or 'quit' to end the conversation
   - Use Ctrl+C for emergency exit

## Usage Examples

```
roskieBot: Hello! I'm BroskieBot, your friendly chatbot!
What's your name? John

 BroskieBot: Nice to meet you, John! 😊

John: Hello!
BroskieBot: Hey there, John! What's on your mind?

John: What time is it?
 BroskieBot: The current time is 02:30 PM

John: Calculate 15 + 25
 BroskieBot: The result is: 40

John: How are you?
BroskieBot: I'm doing great, thanks for asking! How about you?
```

##  How It Works

The chatbot uses a rule-based approach with if-elif-else statements to:

1. **Input Processing**: Converts user input to lowercase for pattern matching
2. **Pattern Recognition**: Uses keyword matching and string operations
3. **Response Generation**: Selects appropriate responses based on detected patterns
4. **Context Awareness**: Maintains user name and conversation flow

### Key Components:

- **Greeting System**: Recognizes various greeting patterns
- **Question Handling**: Processes different types of questions
- **Math Calculator**: Extracts numbers and operators for basic calculations
- **Fallback Responses**: Handles unrecognized inputs gracefully

##  Interview Questions & Answers

### 1. How do you collect user input?
Using Python's `input()` function with prompts and validation to ensure non-empty responses.

### 2. What is the difference between == and =?
- `=` is assignment operator (assigns values)
- `==` is comparison operator (checks equality)

### 3. What is a chatbot?
A computer program designed to simulate conversation with human users through text or voice interactions.

### 4. What is the limitation of rule-based bots?
- Limited to predefined patterns
- Cannot learn or adapt
- Struggles with complex queries
- Requires manual rule creation
- No contextual understanding

### 5. How can you exit a loop on command?
Using `break` statement or condition-based loop control with flags.

### 6. What's the use of lower()?
Converts strings to lowercase for consistent pattern matching and case-insensitive comparisons.

### 7. How would you handle multiple intents?
Using multiple if-elif conditions with keyword lists and priority-based matching.

### 8. How would you test this?
- Unit tests for individual functions
- Integration tests for conversation flow
- Edge case testing (empty inputs, special characters)
- User acceptance testing

### 9. How to organize code better?
- Separate classes for different functionalities
- Use configuration files for responses
- Implement logging
- Add documentation
- Follow PEP 8 standards

### 10. How can this evolve into an ML bot?
- Add training data collection
- Implement NLP libraries (NLTK, spaCy)
- Use machine learning models (TensorFlow, PyTorch)
- Add intent recognition and entity extraction
- Implement context management

## Key Concepts Demonstrated

- **Control Flow**: If-elif-else statements for decision making
- **Loops**: While loops for continuous conversation
- **Input Handling**: User input processing and validation
- **String Operations**: Pattern matching and text processing
- **Error Handling**: Try-catch blocks for robust operation
- **Modular Design**: Class-based organization

##  Future Enhancements

- Add more conversation topics
- Implement sentiment analysis
- Add file-based response storage
- Create web interface
- Add voice interaction capabilities
- Implement learning mechanisms

## File Structure

```
broskiebot-chatbot/
│
├── chatbot.py          # Main chatbot application
├── README.md          # Project documentation
└── requirements.txt   # Python dependencies (if any)
```

##  Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push to branch (`git push origin feature/improvement`)
5. Create a Pull Request

## License

This project is created for educational purposes as part of a Python developer interview challenge.

## Author

Created for BroskiesHub Python Developer Interview - Task 8
