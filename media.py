import webbrowser

# this is a Movie Class contains movie title , poster image , trailer url


class Movie():
    """ This Class Provides a way to store Movie Information """
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# this function to show trailer youtube video in a small window
    def show_trailer(self):

        webbrowser.open(self.trailer_youtube_url)
