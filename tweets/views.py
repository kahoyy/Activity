from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TweetForm

@login_required
def create_tweet(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_success')
    else:
        form = TweetForm()
    return render(request, 'tweets/create_tweet.html', {'form': form})


def tweet_success(request):
    return render(request, 'tweets/success.html')