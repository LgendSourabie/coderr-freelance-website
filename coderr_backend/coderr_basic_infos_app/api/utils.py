

def calculate_average_rating(rating_list):
    sum_review = 0

    for el in rating_list:
        sum_review = sum_review + el

    if len(rating_list) !=0:
        avg_rating = sum_review/len(rating_list)
    else:
        avg_rating = 0
        return avg_rating
    return round(avg_rating,1)
    