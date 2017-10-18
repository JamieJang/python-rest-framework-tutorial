from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage

from .models import Post

def post_list(request):
	page_data = Paginator(Post.objects.all(),5)
	page = request.GET.get('page')
	try:
		posts = page_data.page(page)
	except PageNotAnInteger:
		posts = page_data.page(1)
	except EmptyPage:
		posts = page_data.page(page_data.num_pages)
	
	return render(request,'post_service/post_list.html',{'posts':posts,'page':page,'total_page':page_data.num_pages})
