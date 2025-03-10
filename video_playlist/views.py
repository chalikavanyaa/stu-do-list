from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Video
from .forms import VideoForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
  video_playlist = Video.objects.all()
  response = {"video_playlist" : video_playlist}
  return render(request, "video_playlist.html", response)

@login_required(login_url='/login')
def add_video(request):
  response = {}
  form = VideoForm(request.POST)
  if request.method == 'POST':
    title = request.POST.get('title')
    link = request.POST.get('link')

    new_video = Video(
      Title = title,
      Link = link
    )

    new_video.save()

    return HttpResponseRedirect('')

  response['form']= form
  return render(request, "video_playlist_form.html", response)