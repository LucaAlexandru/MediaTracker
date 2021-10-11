# BOOKS

STATUS_CHOICES = (
    ("read", "read"), ("to-read", "to-read"), ("currently-reading", "currently-reading")
)

GENRE_CHOICES = (
     ("fiction", "Fiction"), ("fantasy", "Fantasy"), ("educational", "Educational"),
     ("science_fiction", "Science Fiction"), ("thriller", "Thriller"),
     ("psychology", "Psychology"), ("business_and_management", "Business and Management"),
     ("productivity", "Productivity"), ("comics_and_manga", "Comics and Manga"),
     ("biography", "Biography"), ("philosophy", "Philosophy"), ("cooking", "Cooking"),
     ("self-help", "Self-help"), ("history", "History"), ("science", "Science"),
     ("math", "Math"), ("finance_and_investment", "Finance and Investment"),
     ("classics", "Classics"),("cooking", "Cooking"),
     ("nutrition_and_health", "Nutrition and Health"), ("programming", "Programming"),
     ("other", "Other")
)

RATING = (
     ("unrated", "Unrated"), ("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")
)

# FILMS
RATING_TEN = (
     ("unrated", "Unrated"), ("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5"),
     ("6", "6"), ("7", "7"), ("8", "8"), ("9", "9"), ("10", "10")
)

FILM_TYPE = (
    ("movie", "Movie"), ("tv_show", "TV Show"), ("animated_film", "Animated film"),
    ("animated_show", "Animated show")
)

# GAMES

GAME_STATUS_CHOICES = (
    ("played", "Played"), ("wishlist", "Wishlist"), ("playing", "Playing"),
    ("unplayed", "Unplayed")
)

GAME_PLATFORM = (
    ("pc", "PC"), ("console", "Console"), ("other", "Other")
)