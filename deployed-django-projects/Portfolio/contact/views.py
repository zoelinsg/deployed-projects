from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from .forms import ContactForm
from .models import ContactMessage
from .serializers import ContactMessageSerializer
from django.core.mail import send_mail
from django.conf import settings
from django.core.cache import cache
from django.http import HttpResponseForbidden

# 留言功能視圖
def contact_view(request):
    ip_address = request.META.get('REMOTE_ADDR')
    cache_key = f'contact_form_{ip_address}'  # 以 IP 位址作為緩存鍵
    if cache.get(cache_key):  # 如果緩存存在
        return redirect('contact-limit')  # 重定向到留言限制視圖

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            ContactMessage.objects.create(name=name, email=email, message=message)  # 保存留言
            send_mail(
                '新留言來自 {}'.format(email),
                message,
                settings.DEFAULT_FROM_EMAIL,
                ['zoelin.sg@gmail.com'],  # 確保這裡是你的接收郵箱
            )
            cache.set(cache_key, True, 900)  # 設置15分鐘的緩存
            return redirect('contact-success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

# 留言成功視圖
def contact_success(request):
    return render(request, 'contact_success.html')

# 留言限制視圖
def contact_limit(request):
    return render(request, 'contact_limit.html')

# 留言 API 視圖
class ContactMessageCreate(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

    def perform_create(self, serializer):
        contact_message = serializer.save()
        send_mail(
            '新留言來自 {}'.format(contact_message.email),
            contact_message.message,
            settings.DEFAULT_FROM_EMAIL,
            ['zoelin.sg@gmail.com'],  # 確保這裡是你的接收郵箱
        )