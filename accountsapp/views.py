from django.shortcuts import render, redirect
from .models import ProfileParent
from django.contrib.auth.decorators import login_required
from .forms import UserForm, ProfileForm, detailForm
import os
from django.conf import settings
# ProfileForm
from .models import ProfileParent, ProfileChild

# Create your views here.
def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'signUp.html')

@login_required
def profil(request):
    # profil = ProfileParent.objects.get(user=request.user)
    # return render(request, 'profil.html', {'profil': profil})


    user = request.user
    try:
        profil = ProfileParent.objects.get(user=user) 
        profil_child = ProfileChild.objects.get(parent=profil)  # Menarik data anak dari orang tua
        # profilchild = profilchild.object.get()
        # profil = ProfileParent.objects.get(user=request.user)
        # children = profil.children.all()
        fullname = f"{profil.user.first_name} {profil.user.last_name}".strip()
        current_avatar = profil.avatar if profil else None
    except ProfileParent.DoesNotExist:
        ()

    if request.method == 'POST':
        # Form untuk User dan Profile
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profil)
        # detail_form = detailForm(request.POST, instance=profil)
        # profile_form = ProfileForm(request.POST, instance=profil)
        fullname = request.POST.get('fullname', '')
        if fullname:
            first_name, last_name = fullname.split(' ', 1) if ' ' in fullname else (fullname, '')
            user.first_name = first_name
            user.last_name = last_name
            user.save()  # Save the updated user info

            # You can also save other profile information here if needed
            if profil:
                profil.save()

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()  # Simpan data User
            profile = profile_form.save()
            # detail_form.save()

            if profile.avatar:
                print(f"Avatar berhasil di-upload: {profile.avatar.url}")
            
            return redirect('profil')  # Redirect setelah menyimpan perubahan
            # return redirect('profil')  # Redirect setelah menyimpan perubahan
    else:
        # Isi form dengan data yang sudah ada
        user_form = UserForm(instance=user)
        # detail_form = detailForm(instance=profil)

        profile_form = ProfileForm(instance=profil)
        # profile_form = ProfileForm(instance=profil)

    # if request.method == 'POST':
    #     form = ProfileForm(request.POST, request.FILES, instance=profil)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('profil')  # Redirect setelah menyimpan

    # else:
    #     form = ProfileForm(instance=profil)

    avatar_dir = os.path.join(settings.MEDIA_ROOT, 'avatar')
    avatars = []
    if os.path.exists(avatar_dir):
        avatars = [f for f in os.listdir(avatar_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]

    if request.method == 'POST':

        # Cek apakah ada avatar yang dipilih
        avatar_name = request.POST.get('avatar')
        if avatar_name:
            # Simpan avatar yang dipilih ke profil pengguna
            if profil:
                profil.avatar = 'avatar/' + avatar_name  # Pastikan atribut avatar sesuai dengan model Anda
                profil.save()
                print(f"Avatar berhasil diperbarui: {profil.avatar}")
            else:
                # Jika profil belum ada, buat profil baru untuk user
                profil = ProfileParent.objects.create(user=user, avatar='avatar/' + avatar_name)
            return redirect('profil')  # Redirect setelah avatar disimpan

    # avatar_dir = os.path.join(settings.MEDIA_ROOT, 'avatar')
    # avatars = []
    # if os.path.exists(avatar_dir):
    #     avatars = [f for f in os.listdir(avatar_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]

    return render(request, 'profil.html', {
        'user_form': user_form,
        # 'profile_form': profile_form,
        # 'form': form,
        # 'detail_form': detail_form,
        'fullname': fullname,
        'profil_child': profil_child,
        'profil': profil,
        'avatars': avatars,
        'current_avatar': current_avatar,
    })

    # context = {
    #     'user_form': user_form,
    #     'profile_form': profile_form,
    #     'fullname': fullname,
    #     'profil': profil,
    #     'profil_child': profil_child,
    #     'current_avatar': current_avatar,
    # }

    # return render(request, 'profil.html', context)


    # try:
    #     profile = ProfileParent.objects.get(user=request.user)
    # except ProfileParent.DoesNotExist:
    #     raise Http404("Profil tidak ditemukan")
    # return render(request, 'profile.html', {'profile': profile})


def beranda(request):
    return render(request, 'beranda.html')

def landingPage(request):
    return render(request, 'landingPage.html')