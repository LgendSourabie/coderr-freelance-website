from rest_framework.throttling import UserRateThrottle


class twentyCallsPerSecond(UserRateThrottle):

    scope = 'twenty'