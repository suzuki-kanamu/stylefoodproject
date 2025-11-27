from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ReservationForm, ContactForm
from datetime import date

def index(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html')

def about(request):
    return render(request, 'about.html')

def takeout(request):
    return render(request, 'takeout.html')

def thanks(request):
    data = request.session.get('reservation_data')
    return render(request, 'thanks.html', {'data': data})

def review(request):
    return render(request, 'review.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                subject=f"【お問い合わせ】{cd['name']}様より",
                message=cd['message'],
                from_email=cd['email'],
                recipient_list=['ksw2570032@stu.o-hara.ac.jp'],
                fail_silently=False,
            )
            return render(request, 'contact_thanks.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def reserve_view(request):
    today = date.today().isoformat()
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            # JSON化できるように文字列化
            data['date'] = data['date'].isoformat()              # 'YYYY-MM-DD'
            data['time'] = data['time'].strftime('%H:%M')        # 'HH:MM'

            # thanks用にセッション保存
            request.session['reservation_data'] = data

            subject = f"【Feane】{data['name']} 様 ご予約確認メール"
            message = (
                f"{data['name']} 様\n\n"
                f"以下の内容でご予約を承りました。\n\n"
                f"予約日：{data['date']}\n"
                f"来店時間：{data['time']}\n"
                f"人数：{data['people']} 名\n"
                f"電話番号：{data['phone']}\n"
                f"メールアドレス：{data['email']}\n\n"
                "ご来店を心よりお待ちしております。\n"
                "--Feane---スタッフ一同--"
            )

            send_mail(
                subject,
                message,
                'feane@example.com',
                [data['email']],
                fail_silently=False,
            )
            return redirect('thanks')
    else:
        form = ReservationForm()

    return render(request, 'book.html', {'form': form, 'today': today})