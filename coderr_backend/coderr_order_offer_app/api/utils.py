
from django.http import Http404


OFFER_TYPE_OPTIONS = (('basic', 'basic'), ('standard', 'standard'), ('premium', 'premium'))
VALID_OFFER_TYPES = [offer_type[0] for _, offer_type in enumerate(OFFER_TYPE_OPTIONS)]
SET_OFFER_TYPE = set(VALID_OFFER_TYPES)

ORDER_STATUS_OPTIONS = (('in_progress', 'in_progress'), ('completed', 'completed'))


def is_order_in_progress(order):
    return order.status == "in_progress"

def is_order_for_business_user(order, user):
    return order.offer_detail.offer.first().user.id == user.pk


def get_model_or_exception(model, pk:int,flag:str):

    try:
        found_model = model.objects.get(pk=pk)
    except model.DoesNotExist:
        raise Http404({"error": f"{flag} not found."}) 
    else:
        #check if the user searched is a business user
        if flag.lower() != 'user':
            # verify if the user found is a business user 
            if found_model.profile.type != 'business':
                raise Http404({"error": f"{flag} not found."}) 
    return found_model
