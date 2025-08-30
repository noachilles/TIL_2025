

from rest_framework.decorators import api_view
from django.http import JsonResponse
import random

books = [
    {
        "pk": 1,
        "title": "Python Programming for Beginners",
        "description": "An introductory guide to Python programming.",
        "published_date": "2020-05-15",
        "rating": 8.2
    },
    {
        "pk": 2,
        "title": "Advanced Python Techniques",
        "description": "Explore advanced features and techniques in Python.",
        "published_date": "2021-08-22",
        "rating": 9.0
    },
    {
        "pk": 3,
        "title": "Data Science with Python",
        "description": "Learn data science concepts and tools using Python.",
        "published_date": "2019-11-30",
        "rating": 5.5
    },
    {
        "pk": 4,
        "title": "Machine Learning with Python",
        "description": "A comprehensive guide to machine learning with Python.",
        "published_date": "2018-07-10",
        "rating": 7.2
    },
    {
        "pk": 5,
        "title": "Web Development with Django",
        "description": "Build powerful web applications using Django and Python.",
        "published_date": "2022-01-15",
        "rating": 8.1
    },
    {
        "pk": 6,
        "title": "Python for Data Analysis",
        "description": "Techniques and tools for data analysis with Python.",
        "published_date": "2017-03-20",
        "rating": 6.6
    },
    {
        "pk": 7,
        "title": "Automate the Boring Stuff with Python",
        "description": "Automate common tasks and improve productivity with Python.",
        "published_date": "2015-04-14",
        "rating": 9.4
    },
    {
        "pk": 8,
        "title": "Fluent Python",
        "description": "Write efficient, high-quality Python code.",
        "published_date": "2019-09-05",
        "rating": 5.5
    },
    {
        "pk": 9,
        "title": "Effective Python",
        "description": "59 specific ways to improve your Python skills.",
        "published_date": "2017-12-11",
        "rating": 7.7
    },
    {
        "pk": 10,
        "title": "Python Crash Course",
        "description": "A hands-on, project-based introduction to Python.",
        "published_date": "2016-06-17",
        "rating": 6.5
    }
]

# Create your views here.
@api_view(['GET'])
def recommend_books(request):
    high_rated_books = [book for book in books if book['rating'] >= 6.0]
    recommended_books = random.sample(high_rated_books, 1)
    return JsonResponse(recommended_books[0])

@api_view(['GET'])
def books_list(request):
    '''
    - 쿼리 파라미터 'page'를 통해 페이지 번호를 받는다.
    - 단, page 파라미터가 없을 경우에도 첫번째 페이지로 간주하여 결과값을 반환한다.
    - 요청 받은 페이지 수가 전체 도서 정보 수를 넘어서면, 별도 예외 처리 없이 빈 리스트가 반환되어도 무관하다.
    '''    
    page_str = request.GET.get('page', '1')
    page = int(page_str)
    page_size = 5
    start = (page - 1) * page_size
    end = start + page_size
    
    # 만약 전체 도서 정보 수를 넘어서면
    if start >= len(books):
        res = []
    else:
        res = books[start:end]
    
    return JsonResponse(res, safe=False)