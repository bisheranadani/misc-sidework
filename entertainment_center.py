import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A Story of a boy and his toys thay come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.storyline)
#toy_story.show_trailer()

avatar = media.Movie("Avatar", "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

#print(avatar.storyline)
#avatar.show_trailer()

school_of_rock = media.Movie("School of Rock", "Using rock music to learn",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=5afGGGsxvEA")

movies = [toy_story, avatar, school_of_rock]

fresh_tomatoes.open_movies_page(movies)

#print(toy_story.VALID_RATINGS)
#toy_story.VALID_RATINGS = "Lol"
#print(toy_story.VALID_RATINGS)
#print(media.Movie.VALID_RATINGS)

#print(media.Movie.__doc__)
#print(media.Movie.__name__)
#print(media.Movie.__module__)

