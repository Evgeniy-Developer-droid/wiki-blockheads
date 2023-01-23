from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .serializers import PostsSerializer
from .pagination import StandardResultsSetPagination
from .models import PostsModel, CommentsModel, Settings
from django.shortcuts import get_object_or_404
# from .forms import CreatePostForm
from .forms import CreatePostForm, UpdatePostForm
from datetime import datetime


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
    if request.user.is_authenticated:
        form = CreatePostForm()
        if request.method == 'POST':
            form = CreatePostForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('main-page')
            else:
                return render(request, 'Content/create-post.html', context={'message': "Not valid data!", 'form': form})
        return render(request, 'Content/create-post.html', context={'form': form})
    return redirect('login')


def single_post(request, pk):
    # function to view a single post
    post = PostsModel.objects.get(pk=pk)
    settings = Settings.objects.latest('id')
    post.count_views = post.count_views + 1
    # post.update = datetime.now()
    post.save()
    comments = CommentsModel.objects.filter(post=post)
    return render(request, 'Content/single-post.html', context={
        'post': post,
        'comments_count': comments.count,
        'comments': comments,
        'time_published': post.timestamps,
        'count_views': post.count_views,
        'settings': settings
        })



def main_page(request):
    # home page with posts
    all_posts = PostsModel.objects.all().filter(status='active').order_by('-timestamps')
    popular_posts = all_posts.order_by('-count_views')
    settings = Settings.objects.latest('id')
    return render(request, 'Content/main-page.html', context={
        'posts': all_posts,
        'settings': settings,
        'popular_posts': popular_posts
    })


def update_post(request, pk):
    form = UpdatePostForm()
    instance = get_object_or_404(PostsModel, id=pk)
    if request.method == 'POST':
        form = UpdatePostForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('main-page')
    return render(request, 'Content/update-post.html', context={
        'post': instance
    })
