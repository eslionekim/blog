from django.shortcuts import redirect, render

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