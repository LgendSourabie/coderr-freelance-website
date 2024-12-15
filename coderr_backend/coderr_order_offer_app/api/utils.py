
OFFER_TYPE_OPTIONS = (('basic', 'basic'), ('standard', 'standard'), ('premium', 'premium'))
VALID_OFFER_TYPES = [offer_type[0] for _, offer_type in enumerate(OFFER_TYPE_OPTIONS)]
SET_OFFER_TYPE = set(VALID_OFFER_TYPES)