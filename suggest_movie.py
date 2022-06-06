# A program that suggests a movie to watch based on the user's input.
# The program will ask the user for a movie genre and a movie rating.

genre = input("What is your favorite movie genre? ")
rating = input("What is your favorite movie rating? ")


def search_movie(genre, rating):
    """
    This function will search for a movie based on the user's input.
    """
    if genre == "action":
        if rating == "good":
            print("You should watch the movie 'The Matrix'.")
        elif rating == "bad":
            print("You should watch the movie 'The Matrix Revolutions'.")
        elif rating == "average":
            print("You should watch the movie 'The Matrix Reloaded'.")
    elif genre == "comedy":
        if rating == "good":
            print("You should watch the movie 'The Hangover'.")
        elif rating == "bad":
            print("You should watch the movie 'The Hangover Part II'.")
        elif rating == "average":
            print("You should watch the movie 'The Hangover Part III'.")

    elif genre == "drama":
        if rating == "good":
            print("You should watch the movie 'The Shawshank Redemption'.")
        elif rating == "bad":
            print("You should watch the movie 'The Shawshank Redemption Part II'.")
        elif rating == "average":
            print("You should watch the movie 'The Shawshank Redemption Part III'.")

    elif genre == "horror":
        if rating == "good":
            print("You should watch the movie 'The Exorcist'.")
        elif rating == "bad":
            print("You should watch the movie 'The Exorcist Part II'.")
        elif rating == "average":
            print("You should watch the movie 'The Exorcist Part III'.")

    elif genre == "mystery":
        if rating == "good":
            print("You should watch the movie 'The Sixth Sense'.")
        elif rating == "bad":
            print("You should watch the movie 'The Sixth Sense Part II'.")
        elif rating == "average":
            print("You should watch the movie 'The Sixth Sense Part III'.")

    elif genre == "romance":
        if rating == "good":
            print("You should watch the movie 'The Notebook'.")
        elif rating == "bad":
            print("You should watch the movie 'The Notebook Part II'.")
        elif rating == "average":
            print("You should watch the movie 'The Notebook Part III'.")

    elif genre == "scifi":
        if rating == "good":
            print("You should watch the movie 'The Matrix Revolutions'.")
        elif rating == "bad":
            print("You should watch the movie 'The Matrix Reloaded'.")
        elif rating == "average":
            print("You should watch the movie 'The Matrix Revolutions Part II'.")

    elif genre == "thriller":
        if rating == "good":
            print("You should watch the movie 'The Dark Knight'.")
        elif rating == "bad":
            print("You should watch the movie 'The Dark Knight Part II'.")
        elif rating == "average":
            print("You should watch the movie 'The Dark Knight Part III'.")

    elif genre == "war":
        if rating == "good":
            print(
                "You should watch the movie 'The Lord of the Rings: The Return of the King'."
            )
        elif rating == "bad":
            print(
                "You should watch the movie 'The Lord of the Rings: The Return of the King Part II'."
            )
        elif rating == "average":
            print(
                "You should watch the movie 'The Lord of the Rings: The Return of the King Part III'."
            )

    elif genre == "western":
        if rating == "good":
            print("You should watch the movie 'The Good, the Bad and the Ugly'.")
        elif rating == "bad":
            print(
                "You should watch the movie 'The Good, the Bad and the Ugly Part II'."
            )
        elif rating == "average":
            print(
                "You should watch the movie 'The Good, the Bad and the Ugly Part III'."
            )

    elif genre == "zombie":
        if rating == "good":
            print("You should watch the movie 'The Walking Dead'.")
        elif rating == "bad":
            print("You should watch the movie 'The Walking Dead Part II'.")
        elif rating == "average":
            print("You should watch the movie 'The Walking Dead Part III'.")

    else:
        print("I'm sorry, I don't know that movie.")
