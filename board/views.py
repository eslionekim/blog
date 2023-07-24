from django.shortcuts import get_object_or_404, redirect, render

from board.models import boardList

# Create your views here.
def boards(request):
    boardlist = boardList.objects.all()
    return render(
		request,
		'board/boards.html', 
    {
	  'boardlist': boardlist,
  }
	)
    
def index(request):
	boardlist = boardList.objects.all()
	return render(
		request,
		'board/index.html',
		{
	
			'boardlist': boardlist,
		}
	)
 
def post(request):
  mypost = boardList()
  if request.method == 'POST':
    mypost.title = request.POST['title']
    mypost.subtitle = request.POST['subtitle']
    mypost.content = request.POST['content']
    mypost.save()
    return redirect('boards')
  return render(
		request,
  'board/post.html'
	)
  
def update(request, pk):
    curPost = get_object_or_404(boardList,pk=pk)
    if request.method == 'POST':
      curPost.title = request.POST['title']
      curPost.subtitle = request.POST['subtitle']
      curPost.content = request.POST['content']
      curPost.save()
      return redirect('boards')
    return render(
		request,
  'board/update.html',
  {
    'curPost':curPost,
  },
	)
    
def delete(request, pk):
  delPost = get_object_or_404(boardList, pk=pk)
  delPost.delete()
  return redirect('boards')
  
