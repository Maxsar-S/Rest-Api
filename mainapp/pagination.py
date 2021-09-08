from rest_framework.pagination import LimitOffsetPagination


class LimitOffsetPaginationByTwenty(LimitOffsetPagination):
    default_limit = 20


class LimitOffsetPaginationByTen(LimitOffsetPagination):
    default_limit = 10



