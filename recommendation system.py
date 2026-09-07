# ============================================================
#        CODSOFT - ARTIFICIAL INTELLIGENCE INTERNSHIP
#              TASK 4 - RECOMMENDATION SYSTEM
# ============================================================

print("=" * 60)
print("          MOVIE RECOMMENDATION SYSTEM")
print("=" * 60)

print("\nWelcome to the Movie Recommendation System!")
print("Enter a movie name and I will recommend similar movies.")
print("You can type the movie name in uppercase or lowercase.")
print()


# ------------------------------------------------------------
# MOVIE DATABASE
# ------------------------------------------------------------

movies = {

    "Inception": {
        "genres": ["sci-fi", "thriller", "action"],
        "description": "A thief enters people's dreams to steal information."
    },

    "Interstellar": {
        "genres": ["sci-fi", "space", "drama"],
        "description": "A team travels through space to find a new home for humanity."
    },

    "The Matrix": {
        "genres": ["sci-fi", "action", "thriller"],
        "description": "A hacker discovers the truth about the world around him."
    },

    "Avengers": {
        "genres": ["action", "superhero", "adventure"],
        "description": "Superheroes join together to save the world."
    },

    "Iron Man": {
        "genres": ["action", "superhero", "sci-fi"],
        "description": "A billionaire builds a powerful armored suit."
    },

    "Spider-Man": {
        "genres": ["action", "superhero", "adventure"],
        "description": "A young hero uses his powers to protect people."
    },

    "Titanic": {
        "genres": ["romance", "drama"],
        "description": "A love story set aboard the Titanic."
    },

    "The Notebook": {
        "genres": ["romance", "drama"],
        "description": "A romantic story about two people who fall in love."
    },

    "Jurassic Park": {
        "genres": ["adventure", "sci-fi", "thriller"],
        "description": "A theme park with genetically recreated dinosaurs."
    },

    "Avatar": {
        "genres": ["sci-fi", "action", "adventure"],
        "description": "A human explores an alien world and its culture."
    },

    "Gladiator": {
        "genres": ["action", "drama", "adventure"],
        "description": "A Roman general becomes a gladiator seeking revenge."
    },

    "The Dark Knight": {
        "genres": ["action", "thriller", "superhero"],
        "description": "Batman faces a dangerous criminal in Gotham."
    },

    "Toy Story": {
        "genres": ["animation", "comedy", "adventure"],
        "description": "Toys come alive when humans are not around."
    },

    "Frozen": {
        "genres": ["animation", "adventure", "comedy"],
        "description": "Two sisters face an extraordinary magical adventure."
    },

    "Finding Nemo": {
        "genres": ["animation", "adventure", "comedy"],
        "description": "A father searches for his missing son."
    }
}


# ------------------------------------------------------------
# FUNCTION TO DISPLAY ALL MOVIES
# ------------------------------------------------------------

def display_movies():

    print("\nAvailable Movies:")
    print("-" * 40)

    for movie in movies:
        print("-", movie)

    print("-" * 40)


# ------------------------------------------------------------
# FUNCTION TO FIND MOVIE
# ------------------------------------------------------------

def find_movie(user_input):

    user_input = user_input.strip().lower()

    for movie in movies:

        if movie.lower() == user_input:
            return movie

    return None


# ------------------------------------------------------------
# FUNCTION TO RECOMMEND MOVIES
# ------------------------------------------------------------

def recommend_movies(selected_movie):

    selected_genres = set(movies[selected_movie]["genres"])

    recommendations = []

    for movie_name, movie_data in movies.items():

        # Do not recommend the movie the user already selected
        if movie_name == selected_movie:
            continue

        movie_genres = set(movie_data["genres"])

        # Find common genres
        common_genres = selected_genres.intersection(movie_genres)

        # Calculate similarity score
        score = len(common_genres)

        if score > 0:

            recommendations.append(
                (
                    movie_name,
                    score,
                    common_genres
                )
            )

    # Sort recommendations from highest score to lowest
    recommendations.sort(
        key=lambda item: item[1],
        reverse=True
    )

    return recommendations


# ------------------------------------------------------------
# MAIN PROGRAM
# ------------------------------------------------------------

while True:

    print("\n" + "=" * 60)
    print("MENU")
    print("=" * 60)

    print("1. Get Movie Recommendations")
    print("2. Show Available Movies")
    print("3. Exit")

    choice = input("\nEnter your choice (1-3): ").strip()

    # --------------------------------------------------------
    # OPTION 1 - RECOMMENDATION
    # --------------------------------------------------------

    if choice == "1":

        print("\n" + "-" * 60)

        user_movie = input(
            "Enter a movie you like: "
        )

        selected_movie = find_movie(user_movie)

        if selected_movie is None:

            print("\n❌ Movie not found in our database.")
            print("Please choose a movie from the available list.")

            display_movies()

        else:

            print("\n" + "=" * 60)
            print("SELECTED MOVIE")
            print("=" * 60)

            print("Movie:", selected_movie)

            print(
                "Genres:",
                ", ".join(movies[selected_movie]["genres"])
            )

            print(
                "Description:",
                movies[selected_movie]["description"]
            )

            # Get recommendations
            recommendations = recommend_movies(
                selected_movie
            )

            print("\n" + "=" * 60)
            print("RECOMMENDED MOVIES")
            print("=" * 60)

            if len(recommendations) == 0:

                print("No recommendations available.")

            else:

                # Display top 5 recommendations
                for index, recommendation in enumerate(
                    recommendations[:5],
                    start=1
                ):

                    movie_name = recommendation[0]
                    score = recommendation[1]
                    common_genres = recommendation[2]

                    print(
                        f"\n{index}. {movie_name}"
                    )

                    print(
                        "   Similarity Score:",
                        score
                    )

                    print(
                        "   Common Genres:",
                        ", ".join(common_genres)
                    )

                    print(
                        "   Description:",
                        movies[movie_name]["description"]
                    )

            print("\n" + "=" * 60)

    # --------------------------------------------------------
    # OPTION 2 - DISPLAY MOVIES
    # --------------------------------------------------------

    elif choice == "2":

        display_movies()

    # --------------------------------------------------------
    # OPTION 3 - EXIT
    # --------------------------------------------------------

    elif choice == "3":

        print("\n" + "=" * 60)
        print("Thank you for using the Movie Recommendation System!")
        print("Goodbye!")
        print("=" * 60)

        break

    # --------------------------------------------------------
    # INVALID CHOICE
    # --------------------------------------------------------

    else:

        print("\n❌ Invalid choice.")
        print("Please enter 1, 2, or 3.")