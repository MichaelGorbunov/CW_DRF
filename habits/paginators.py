from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    """Пагинация - вывод 5 привычек на страницу"""

    page_size = 15
    page_query_param = "page_size"
    max_page_size = 30
