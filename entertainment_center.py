import fresh_tomatoes
import media

# First instance
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://ca.movieposter.com/posters/archive/main"
                        "/98/MPW-49385",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
# Second instance
avatar = media.Movie("Avatar",
                     " science fiction film ",
                     "https://upload.wikimedia.org/wikipedia/id/b/b0/"
                     "Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=vGNGGBzaNQ0")
# Third instance
Moana = media.Movie("Moana",
                    "a 2016 American 3D computer-animated musical "
                    "fantasy-adventure film",
                    "https://images.pyramidshop.com/images/_popup/"
                    "PP33961-Moana-(Boat).jpg",
                    "https://www.youtube.com/watch?v=LKFuXETZUsI")
# Fourth instance
In_time = media.Movie("In Time",
                      "a 2011 American dystopian science fiction "
                      "action thriller film written",
                      "https://rroyreport.files.wordpress.com/2011/10/"
                      "in-time-movie-poster.jpg?w=1400",
                      "https://www.youtube.com/watch?v=AwhMuHWixZA")
# Fifth instance
I_am_sam = media.Movie("I am Sam ",
                       "a 2001 American drama film ",
                       "https://i.ytimg.com/vi/B_hnk-JJoqc/hqdefault.jpg",
                       "https://www.youtube.com/watch?v=z_AguDqCBvo")
# Sixth instance
If_I_Stay = media.Movie("If I Stay",
                        "a 2014 American teen romantic drama",
                        "http://www.yalsa.ala.org/thehub/wp-content/"
                        "uploads/2014/06/if-i-stay-poster.jpg",
                        "https://www.youtube.com/watch?v=wH6PNeTy6Nc")

# List of Movies
movies_list = [toy_story, avatar, Moana, In_time, I_am_sam, If_I_Stay]
# fresh tomatoes is a python code generate a website that displays these movies
fresh_tomatoes.open_movies_page(movies_list)
