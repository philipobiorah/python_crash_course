# Create a copy of a dictionary.

# Iterate through the values of the new dictionary.

# Change each value in the new dictionary, while keeping the same keys




def reset_scores(games_scores):

    # The .copy() dictionary method is used to create a new copy of the "game_scores".
    new_game_scores = games_scores.copy()

    for player, score in new_game_scores.items():
        # The dictionary operation to assign a new value to a key is used
        # to reset the grade values to 0.
        new_game_scores[player] = 0

    return new_game_scores



# The dictionary is defined.
game1_scores = {"Arshi": 3, "Catalina": 7, "Diego": 6}
 
# Call the "reset_scores" function with the "game1_scores" dictionary. 
print(reset_scores(game1_scores))
# Should print {'Arshi': 0, 'Catalina': 0, 'Diego': 0}