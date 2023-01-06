from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .serializers import PostsSerializer
from .pagination import StandardResultsSetPagination
from .models import PostsModel
# from .forms import CreatePostForm
from .forms import CreatePostForm, FormForPostModel


class GetAllPostsView(GenericAPIView):

    """View to get all posts with pagination"""

    queryset = PostsModel.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = PostsSerializer

    def get(self, request):
        try:
            paginator = StandardResultsSetPagination()
            paginator.page_size = request.GET['amount']
            result_page = paginator.paginate_queryset(self.queryset, request)
            serializer = self.serializer_class(result_page, many=True)
            return Response({
                "result": serializer.data,
                "count": self.queryset.count()
            })
        except KeyError:
            return Response({'error': 'Enter GET parameter - "amount"!'})


class GetPostsForUser(GenericAPIView):

    """View to get all posts by user with pagination"""

    queryset = PostsModel.objects.all()
    serializer_class = PostsSerializer

    def get(self, request, user):
        try:
            paginator = StandardResultsSetPagination()
            paginator.page_size = request.GET['amount']
            instance = self.queryset.filter(user=user)
            result_page = paginator.paginate_queryset(instance, request)
            serializer = self.serializer_class(result_page, many=True)
            return Response({
                "result": serializer.data,
                "count": instance.count()
            })
        except KeyError:
            return Response({'error': 'Enter GET parameter - "amount"!'})


def create_new_post(request):
    # function to create a new post
    form = CreatePostForm()
    # if request.method == 'POST':
    #     form = CreatePostForm(request.POST)
    #     if form.is_valid():
    #         post = form.save()
    #         return render(request, 'Content/create-post.html', context={'message': "Post created!"})
    #     else:
    #         return render(request, 'Content/create-post.html', context={'message': "Not valid data!"})
    return render(request, 'Content/create-post.html', context={'form': form})


def single_post(request, pk):
    # function to view a single post
    post = PostsModel.objects.get(pk=pk)
    return render(request, 'Content/single-post.html', context={'post': post})



def main_page(request):
    # home page with posts
    posts = PostsModel.objects.all()
    return render(request, 'Content/main-page.html', context={'posts': posts})
