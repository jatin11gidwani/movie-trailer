import media
import fresh_tomatoes

spiderman = media.Movie(
    "Spiderman Homecoming",
    "A story of a teenager bit by spider and gained awesome powers.",
    "https://upload.wikimedia.org/wikipedia/en/f/f9/Spider-Man_Homecoming_poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=H1wVask5neY")

ironman = media.Movie(
    "Iron Man",
    "A story of a billionare who creates an awesome suit to fight crimes.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/7/70/Ironmanposter.JPG/220px-Ironmanposter.JPG",  # noqa
    "https://www.youtube.com/watch?v=8hYlB38asDY")

hulk = media.Movie(
    "Hulk",
    "A scientist gets hit by Gamma raditations which gives him incredible"
    "powers.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/5/59/Hulk_movie.jpg/220px-Hulk_movie.jpg",  # noqa
    "https://www.youtube.com/watch?v=xbqNb2PFKKA")

internship = media.Movie(
    "The Internship",
    "The 2 old times salesmen gets an internship at big tech giant Google.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/e/ed/The-internship-poster.jpg/220px-The-internship-poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=cdnoqCViqUo")

grown_ups = media.Movie(
    "Grown Ups",
    "Long time friends meet after a long time with their families.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/f/fe/Grownupsmovie.jpg/220px-Grownupsmovie.jpg",  # noqa
    "https://www.youtube.com/watch?v=e01NVCveGkg")

# here deadpool is an instance of class Movie taking arguments
# movie_title, movie_storyline, poster_image and trailer_youtube
deadpool = media.Movie(
    "Deadpool",
    "A story of a normal guy turned mutant and little insane.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/4/46/Deadpool_poster.jpg/220px-Deadpool_poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=0e847PHeAw0")

# List to hold the instance varibles
movies = [
    spiderman,
    ironman,
    hulk,
    internship,
    grown_ups,
    deadpool]

# calling the open_movies_page from fresh_tomatoes class passing a list
# as argument to create a static web page of movies present in the list.
fresh_tomatoes.open_movies_page(movies)
