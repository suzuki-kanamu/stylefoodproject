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

def reserve_view(request):
    return render(request, 'reserve.html')

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

def reserve_seat(request):
    today = date.today().isoformat()

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            # 日付,日時を文字列に変換しないとだめらしいよ
            data['date'] = str(data['date'])
            data['time'] = str(data['time'])

            message = (
                f"名前: {data['name']}\n"
                f"電話番号: {data['phone']}\n"
                f"メールアドレス: {data['email']}\n"
                f"人数: {data['people']}名\n"
                f"予約日: {data['date']}\n"
                f"予約時間: {data['time']}"
            )


            request.session['reservation_data'] = data
            return redirect('thanks')
    else:
        form = ReservationForm()

    return render(request, 'book.html', {'form': form, 'today': today})


def reserve_view(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            # メール本文の作成
            subject = f"【Feane】{data['name']} 様 ご予約確認メール"
            message = (
                f"{data['name']} 様\n\n"
                f"以下の内容でご予約を承りました。\n\n"
                f"予約日：{data['date']}\n"
                f"来店時間：{data['time'].strftime('%H:%M')}\n"
                f"人数：{data['people']} 名\n"
                f"電話番号：{data['phone']}\n"
                f"メールアドレス：{data['email']}\n\n"
                "ご来店を心よりお待ちしております。\n"
                "--Feane---スタッフ一同--"
            )

            # メール送信
            send_mail(
                subject,
                message,
                'feane@example.com',  # 送信元メールアドレス（settings.pyで定義してもOK）
                [data['email']],      # 宛先
                fail_silently=False,
            )

            # thanksページへ遷移
            return render(request, 'thanks.html', {'data': data})
    else:
        form = ReservationForm()

    return render(request, 'book.html', {'form': form})