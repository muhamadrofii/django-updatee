from django.shortcuts import render, get_object_or_404
from .models import YouTubeVideo
# get_object_or_404
from .models import Quiz, Choice
# get_object_or_404

def kids(request):
    category_filter = request.GET.get('category', None)

    if category_filter:
        # Validasi apakah kategori ada di database
        valid_categories = YouTubeVideo.objects.values_list('category', flat=True).distinct()
        if category_filter in valid_categories:
            videos = YouTubeVideo.objects.filter(category=category_filter)
        else:
            # Jika kategori tidak valid, kosongkan daftar video
            videos = YouTubeVideo.objects.none()
    else:
        # Tampilkan semua video jika tidak ada kategori
        videos = YouTubeVideo.objects.all()
        # YouTubeVideo.objects.none()

    return render(request, 'kids.html', {'videos': videos, 'selected_category': category_filter})



def parents(request):
    category_filter = request.GET.get('category', None)

    if category_filter:
        # Validasi apakah kategori ada di database
        valid_categories = YouTubeVideo.objects.values_list('category', flat=True).distinct()
        if category_filter in valid_categories:
            videos = YouTubeVideo.objects.filter(category=category_filter)
        else:
            # Jika kategori tidak valid, kosongkan daftar video
            videos = YouTubeVideo.objects.none()
    else:
        # Tampilkan semua video jika tidak ada kategori
        videos = YouTubeVideo.objects.all()

    return render(request, 'parents.html', {'videos': videos, 'selected_category': category_filter})

def parent(request):
    return render(request, 'parent.html')

def watch_video(request, youtube_id):
    video = get_object_or_404(YouTubeVideo, youtube_id=youtube_id)  # Ambil video berdasarkan ID
    return render(request, 'watch_video.html', {'video': video})

def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.prefetch_related('choices').order_by('order')

    if request.method == 'POST':
        score = 0
        total_questions = questions.count()
        
        for question in questions:
            selected_choice_id = request.POST.get(f'question_{question.id}')
            if selected_choice_id:
                selected_choice = Choice.objects.get(id=selected_choice_id)
                if selected_choice.is_correct:
                    score += 1
        
        score_percentage = (score / total_questions) * 100 if total_questions > 0 else 0

        return render(request, 'quiz_result.html', {
            'quiz': quiz,
            'score': score,
            'total_questions': total_questions,
            'score_percentage': score_percentage
        })

    # Inisialisasi variabel hanya jika diperlukan
    total_questions = questions.count()  # Untuk GET ini aman
    print("Quiz:", quiz)
    print("Questions:", questions)
    return render(request, 'quiz.html', {
        'quiz': quiz,
        'questions': questions
    })


# def quiz(request):
    # return render(request, 'quiz.html')

    # quiz = get_object_or_404(Quiz, id=quiz_id)
    # questions = quiz.questions.prefetch_related('choices').order_by('order')
    # return render(request, 'quiz_detail.html', {
    #     'quiz': quiz,
    #     'questions': questions