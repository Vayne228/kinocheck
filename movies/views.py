from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import ListView, DetailView

from .forms import ReviewForm
from .models import Movie
# Create your views here.

class MovieView(ListView):
	model = Movie
	queryset = Movie.objects.filter(draft=False)
	#template_name = "movies/movies.html"

class MovieDetailView(DetailView):
	model = Movie
	slug_field = "url"


class AddReview(View):
	"""docstring for AddReview"""
	def post(self, request, pk):
		form = ReviewForm(request.POST)
		movie = Movie.objects.get(id=pk)
		if form.is_valid():
			form = form.save(commit=False)
			form.movie = movie
			form.save() 
		return redirect(movie.get_absolute_url())


