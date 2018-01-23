import webbrowser


class Movie():
    """This class contains methods and feild to create objects
    and a single static web page"""

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """class constructor to create different
        objects containg information about a movie."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """This method opens the browser with trailer of the movie"""
        webbrowser.open(self.trailer_youtube_url)
