Project Description
This project implements a classic Rock-Paper-Scissors game with a twist: an AI opponent that learns and predicts your moves using machine learning. The AI adapts over time to counter your strategies, providing a dynamic and engaging gameplay experience.

Features
Interactive Gameplay: Play against the AI in real time.
Machine Learning Integration:
The AI uses a Random Forest Classifier from scikit-learn to predict your next move based on previous patterns.
Initially, the AI plays randomly, but as you play more rounds, it trains and adjusts its predictions.
Dynamic Learning: The AI gets smarter as it gathers more data about your moves.
Prerequisites
Python 3.7 or higher
Required Python libraries:
scikit-learn
numpy (installed as part of scikit-learn)
Gameplay Instructions
The program will prompt you to input one of the following moves:
rock
paper
scissors
Type your move and press Enter.
The AI will:
Predict your next move based on past rounds.
Choose the best counter move.
The result of each round is displayed:
Win
Lose
Tie
To exit the game, type exit.
How It Works
Data Collection: The AI stores your moves and its own responses after each round.
Training:
After collecting at least 5 rounds of data, the AI trains a RandomForestClassifier using your past moves as input and its counter moves as labels.
Prediction:
The AI predicts your next move based on patterns in the training data.
It selects the counter move to maximize its chances of winning.
Example Gameplay
vbnet
Copy code
Welcome to Rock-Paper-Scissors with AI!
Enter your move (rock, paper, scissors or 'exit' to quit): rock
AI predicted you might play: paper
AI played: scissors
You win!
Customizations
Change the AI Model: Experiment with other models like DecisionTree, LogisticRegression, or neural networks.
Enhance Data: Include sequences of moves or additional features to make predictions more accurate.
Add Variants: Expand the game with moves like "lizard" and "spock."
Known Limitations
The AI may struggle with completely random human playstyles.
Requires sufficient rounds to make reliable predictions.
Future Enhancements
Save the AI’s training data between sessions for persistent learning.
Add a graphical user interface (GUI) for better user interaction.
Output Image:
![Screenshot 2024-12-06 193921](https://github.com/user-attachments/assets/ca4fabe6-5ffe-4a45-9b46-cca32def7edb)


