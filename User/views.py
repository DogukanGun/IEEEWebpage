from .forms import RegisterForm,LoginForm,ForgotPassword
from .models import User
from django.contrib.auth.models import User as user
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from IEEEwebpage.settings import EMAIL_HOST_USER
from django.views.decorators.csrf import csrf_protect
from django.core.mail import EmailMessage
# Create your views here.
def courses(request):
    return render(request,"Courses.html")
@csrf_protect
def register(request,id):
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            name=form.cleaned_data["name"]
            password = form.cleaned_data["password"]
            email=form.cleaned_data.get("email")
            newUser = User(username=username,name=name,password=password,email=email)
            newUser.save()
            userFromDjango=user(username=username)
            userFromDjango.set_password(password)
            userFromDjango.save()
            login(request, userFromDjango)
            messages.info(request,"Başarıyla Kayıt Oldunuz...")
            return redirect('mainPage')
    else:
            form=RegisterForm()
    context = {
            "form" : form,
            "id":id
    }
    return render(request,"SignupLogin.html",context)
@csrf_protect
def loginUser(request,id):
    form = LoginForm(request.POST)
    context = {
        "form":form,
        "id":id
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username = username,password = password)
        if user is None:
            messages.info(request,"Kullanıcı Adı veya Parola Hatalı")
            return render(request,"PatchPanel.html",context)

        messages.success(request,"Başarıyla Giriş Yaptınız")
        login(request,user)
        return redirect("index")
    return render(request,"SignupLogin.html",context)
def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yaptınız")
    return redirect('mainPage/')

def Projects(request):
    return render(request,'Projects.html')
def ReleatedClubs(request):
    return render(request,'ReleatedClubs.html')
def Ieee(request):
    title="IEEE TURKIYE"
    context="The Institute of Electrical and Electronics Engineers ya da kısaca IEEE (Türkçe: Elektrik ve Elektronik Mühendisleri Enstitüsü)./nElektrik, elektronik, bilgisayar, otomasyon, telekomünikasyon ve diğer birçok alanda, mühendislik teori ve uygulamalarının gelişimi için çalışan, kar amacı olmayan, dünyanın önde gelen teknik organizasyonudur. 1884 yılında kurulan IEEE insanlık yararına teknolojiyi geliştirmeyi hedefleyen bir topluluktur./nDünyanın en büyük teknik organizasyonu olarak, IEEE üyeleri arasında mühendisler, bilim insanları ve diğer uzmanlar bulunur. Kurucu unsur olan elektrik elektronik mühendisleri dışında, günümüzde bilgisayar mühendisleri, yazılım geliştiricileri, bilişim teknolojileri uzmanları, fizikçiler, hekimler ve daha birçok meslekten insan IEEE çatısı altında bulunmaktadır. Bu nedenle topluluğun tam adı artık geçerliliğini yitirmiştir ve resmi evraklar dışında pek kullanılmamaktadır. Bu uzun isim yerine IEEE kısaltması daha çok tercih edilmektedir."
    content={
        'title':title,
        'context':context
    }
    print(content)
    return render(request,"About.html",content)
def members(request):
    return render(request,"Members.html")
def about(request):
    title="IEEE DEU"
    context="Dokuz Eylül Üniversitesinde 2001 yılından beri aktif olan kulübümüz IEEE DEU SB, gönüllülük esaslı çalışan, teknik ve sosyal konularda gelişmeleri takip edip uygulayan; birden fazla komitesiyle her alanda kendini yeterli bir şekilde geliştirmeyi hedefleyen bir IEEE öğrenci koludur. Temel kitlesi mühendislik öğrencileri olan kulübümüz hem okulumuz öğrencileri hem de mezunlarıyla işbirliği halinde çalışmaya devam etmektedir. Computer Society (CS), Power and Energy Society (PES), Robotics and Automation Society (RAS), Aerospace and Electronic Systems Society (AESS), Engineering in Medicine and Biology Society (EMBS), Women in Engineering (WIE), Educational Activities (EA), IEEE Türkiye Kardeş Öğrenci Kolları (KÖK) ve Entrepreneurship alt komitelerine sahip iken aynı zamanda bir bütün halinde çalışan kulübümüz, sene içinde alanlarının en iyileriyle düzenledikleri konferanslar ve etkinliklerle büyük başarılara imza atıp; üye öğrencilere profesyonel bir network ağı kazandırmaktadır. Yıl içinde düzenlenen onlarca etkinlikte görev alıp üyelerimize sorumluluk bilinci kazandırarak ve bir etkinlik ortaya çıkarırken karşılaşılabilecek problemleri aşma tecrübesi elde etmelerine imkan sağlayarak kişisel gelişimlerine katkıda bulunuyoruz. Öğrencilere mesleki geleceklerine dair farklı bakış açıları kazandırıyor, sektörün önde gelen firmalarıyla iletişim kurmalarını sağlayıp onlara çeşitli fırsatlar sunuyoruz."
    content={
        "title":title,
        "context":context
    }
    return render(request,"About.html",content)
def welcomePage(request):
    return render(request,"WelcomePage.html")
def forgotPassword(request):
    if request.method=='POST':
        print("geldi2")
        form=ForgotPassword(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            print(username)
            user_=User.objects.filter(username=username)
            if user_ is None:
                messages.info(request, "Username could not found")
                return render(request, "PatchPanel.html")
            print(user_)
            print("geldi")

            email = EmailMessage('Password Reset','To reset your password please click the address below.\n\nhttp://127.0.0.1:8000/user/reset/', to=["vildan_gundogan@hotmail.com"])
            email.send()
            return redirect('/user/mainPage')
    else:
        print("geldi3")
        form=ForgotPassword()
    context={
        'form':form,
        'id':3
    }
    return render(request, "SignupLogin.html", context)
def resetPassword(request):
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            newUser=user.objects.filter(username=username).first()
            newUser.set_password(password)
            newUser.save()
            newUser=User.objects.filter(username=username).first()
            newUser.password=password
            newUser.save()
    else:
        form=LoginForm()
    context={
        'form':form,
    }
    return render(request,"forgotPassword.html", context)


def mainPage(request):
    return render(request,"PatchPanel.html")
def joinUs(request):
    return render(request,"JoinUs.html")
