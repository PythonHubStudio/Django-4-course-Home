from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

from goods.models import Products


def q_search(query):
    
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    
    vector = SearchVector("name", "description")
    query = SearchQuery(query)
    
    return Products.objects.annotate(rank=SearchRank(vector, query)).order_by("-rank")


    # keywords = [word for word in query.split() if len(word) > 2]

    # q_objects = Q()

    # for token in keywords:
    #     q_objects |= Q(description__icontains=token)
    #     q_objects |= Q(name__icontains=token)

    # return Products.objects.filter(q_objects)
