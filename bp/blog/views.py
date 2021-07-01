from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog, Comment
from django.utils import timezone
# Create your views here.
def blog(request):
    blogs = Blog.objects.all()
    return render(request,'blog.html', { 'blogs' : blogs })

# R
def detail(request, blog_id):
    detail = get_object_or_404(Blog, pk=blog_id)
    comments = Comment.objects.all().filter(post=detail)

    # like => 순서쌍('현재 blog.id', '현재 user.id')
    # 이 순서쌍이 Like모델에 있다면 좋아요를 누를 것! -> 좋아요 취소 message를 전달
    #이 순서쌍이 Like모델에 없다면 좋아요를 누르지 않은 것! -> 좋아요 message를 전달
    if detail.likes.filter(id=request.user.id):
        message="좋아요 취소"
    else:
        message="좋아요"
        
    return render(request ,'detail.html', { 'detail' : detail, 'comments':comments, 'message':message } )

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog() # 객체 틀 하나 가져오기
    blog.title = "NoTitle"  # 내용 채우기
    if request.GET['title']:
        blog.title=request.GET['title']
    blog.body = request.GET['body'] # 내용 채우기
    blog.pub_date = timezone.datetime.now() # 내용 채우기
    blog.writer = request.user  #지금 접속하고 있는 user의 정보가 writer에 담김
    blog.save() # 객체 저장하기

    # 새로운 글 url 주소로 이동
    return redirect('/blog/' + str(blog.id))

#삭제
def delete(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    return redirect('/blog/')
#update

def update(request, blog_id):
    blog = get_object_or_404(Blog, pk =blog_id)

    if request.method == "POST":
        if request.POST['title']:
            blog.title=request.POST['title']
        blog.body = request.POST['body']
        blog.pub_date = timezone.datetime.now()
        blog.save()
        return redirect('/blog/' +str(blog.id))
    else:
        return render(request,'update.html')

def comment(request, blog_id):
    if request.method=="POST":
        comment = Comment()
        comment.body = request.POST['body']
        comment.pub_date = timezone.datetime.now()
        comment.writer = request.user
        comment.post = get_object_or_404(Blog, pk=blog_id)
        comment.save()

        return redirect('/blog/'+str(blog_id))
    else:
        return redirect('/blog/'+str(blog_id))

def comment_delete(request, comment_id):
    comment=get_object_or_404(Comment, pk=comment_id)
    blog_id = comment.post.id # 그 댓글이 연결되어 있는 블로그 객체(post)의 id
    comment.delete()

    return redirect('/blog/'+str(blog_id))

#like 관련 함수
def post_like(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    user = request.user

    # admin에서 add하고 remove하는 거랑 동일
    if blog.likes.filter(id=user.id):
        blog.likes.remove(user)
    else:
        blog.likes.add(user)

    return redirect('/blog/'+str(blog_id))