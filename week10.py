def validate_rating(rating):

    try:

        rating=float(rating)

        if rating<1 or rating>5:

            raise ValueError

        return rating

    except:

        print("Invalid Rating")
