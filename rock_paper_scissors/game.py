import random
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Prepare data storage
data = {"user_move": [], "opponent_move": []}

# Moves and their counters
moves = ["rock", "paper", "scissors"]
winning_moves = {"rock": "paper", "paper": "scissors", "scissors": "rock"}

# Encode moves for machine learning
encoder = LabelEncoder()
encoder.fit(moves)

# Initialize the model
model = RandomForestClassifier()

# Function to collect and train data
def train_model():
    if len(data["user_move"]) >= 5:  # Train after 5 rounds of data
        X = encoder.transform(data["user_move"]).reshape(-1, 1)
        y = encoder.transform(data["opponent_move"])
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model.fit(X_train, y_train)

# Function to predict the next move
def predict_next_move(user_move):
    if len(data["user_move"]) < 5:
        return random.choice(moves)  # Use random strategy initially
    encoded_move = encoder.transform([user_move]).reshape(-1, 1)
    predicted_move = model.predict(encoded_move)
    return encoder.inverse_transform(predicted_move)[0]

# Main game loop
print("Welcome to Rock-Paper-Scissors with AI!")
while True:
    user_move = input("Enter your move (rock, paper, scissors or 'exit' to quit): ").lower()
    if user_move == "exit":
        print("Thanks for playing!")
        break
    if user_move not in moves:
        print("Invalid move. Try again.")
        continue

    # AI predicts opponent's move
    predicted_move = predict_next_move(user_move)
    ai_move = winning_moves[predicted_move]  # AI chooses the move to counter predicted move

    print(f"AI predicted you might play: {predicted_move}")
    print(f"AI played: {ai_move}")

    # Decide the winner
    if user_move == ai_move:
        print("It's a tie!")
    elif winning_moves[user_move] == ai_move:
        print("You win!")
    else:
        print("AI wins!")

    # Update data
    data["user_move"].append(user_move)
    data["opponent_move"].append(ai_move)

    # Retrain the model
    train_model()
