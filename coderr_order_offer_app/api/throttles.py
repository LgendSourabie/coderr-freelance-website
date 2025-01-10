from rest_framework.throttling import UserRateThrottle


class HundredCallsPerSecond(UserRateThrottle):

    scope = 'hundred'