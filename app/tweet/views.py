from django.shortcuts import render, redirect
from .models import Tweet
from .forms import TweetForm
# Create your views here.
from django.shortcuts import get_object_or_404


def index(request):
    return render(request, 'index.html')


def tweet_list(request):
    tweet=Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html',{'tweet':tweet})

def tweet_create(request):
    if request.method == 'POST':
        form = TweetForm(request.POST,request.FILES)
        if form.is_valid():
            tweet  = form(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()

    return render(request, 'tweet_form.html',{'form':form})

def tweet_edit(request, id):
    tweet = get_object_or_404(Tweet, pk=id, user = request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST,request.FILES, instance = tweet)
        if form.is_valid():
            tweet = form(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweet_form.html', {'form':form})

def tweet_delete(request, id):
    tweet = get_object_or_404(Tweet, pk=id, user=request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'tweet_confirm_delete.html',{'tweet':tweet})