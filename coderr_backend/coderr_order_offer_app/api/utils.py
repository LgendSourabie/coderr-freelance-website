
from django.http import Http404
from django.contrib.auth.models import User
from coderr_user_profile_app.models import Profile
from decimal import Decimal


OFFER_TYPE_OPTIONS = (('basic', 'basic'), ('standard', 'standard'), ('premium', 'premium'))
VALID_OFFER_TYPES = [offer_type[0] for _, offer_type in enumerate(OFFER_TYPE_OPTIONS)]
SET_OFFER_TYPE = set(VALID_OFFER_TYPES)
ORDER_STATUS_OPTIONS = (('in_progress', 'in_progress'), ('completed', 'completed'),('cancelled', 'cancelled'))

def get_min_price(details,method='patch'):
    """Get the minimum price from all offers"""
    if method == 'post':
        all_detail_price = [Decimal(detail['price']) for detail in details]
    else:
        all_detail_price = [Decimal(detail.price) for detail in details]
    return min(all_detail_price)


def get_min_delivery_time(details, method='patch'):
    """Get the minimum delivers time in days"""
    if method == 'post':
        all_detail_delivery_time = [Decimal(detail['delivery_time_in_days']) for detail in details]
    else:
        all_detail_delivery_time = [Decimal(detail.delivery_time_in_days) for detail in details]
    return min(all_detail_delivery_time)


def is_order_in_progress(order):
    """Check wether the current order is in progress or not"""
    return order.status == "in_progress"

def is_order_for_business_user(order, user):
    """ Check if an order belongs to a business_user whose ID is provide """
    return order.offer_detail.offer.first().user.id == user.pk


def get_model_or_exception(model, pk:int,error_message:str):
    """ Found object by ID , return the object if found otherwise raise an error """

    try:
        found_model = model.objects.get(pk=pk)
    except model.DoesNotExist:
        raise Http404({"error": f"{error_message}"}) 
    else:
        #check if the user searched is a business user
        if 'Geschäftsnutzer'.lower() in error_message.lower():
            # verify if the user found is a business user 
            if type(found_model) == User and found_model.profile.type != 'business':
                raise Http404({"error": f"{error_message}"}) 
            elif type(found_model) == Profile and found_model.type != 'business':
                raise Http404({"error": f"{error_message}"}) 
    return found_model






















# {
#     "description": "Ich werde Front-End-Webentwicklung in React JS und Javascript durchführen",
#     "title": "Softwareentwicklung",
#     "details": [
#         {
#             "title": "Basic Design",
#             "revisions": "3",
#             "delivery_time_in_days": "14",
#             "price": "30.50",
#             "features": [
#                 "Logo Design"
#             ],
#             "offer_type": "basic"
#         },
#         {
#             "title": "Standard Design",
#             "revisions": "6",
#             "delivery_time_in_days": "15",
#             "price": "99.99",
#             "features": [
#                 "Logo Design",
#                 "Visitenkarte",
#                 "Briefpapier"
#             ],
#             "offer_type": "standard"
#         },
#         {
#             "title": "Premium Design",
#             "revisions": -1,
#             "delivery_time_in_days": "21",
#             "price": "399.99",
#             "features": [
#                 "Logo Design",
#                 "Visitenkarte",
#                 "Briefpapier",
#                 "Flyer"
#             ],
#             "offer_type": "premium"
#         }
#     ]
# }