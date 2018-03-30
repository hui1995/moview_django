import json
import os
import random
import time

from django.http import JsonResponse
from django.shortcuts import render,redirect

# Create your views here.
from lxml.html.builder import IMG

from moviewsweb.settings import BASE_DIR
from myApp.models import Banner, Moview, User, Like


def test(request):

    url=BASE_DIR
    with open('/home/zhao/Documents/pywebproject/moviewsweb/电影.json','r') as load_f:
        load_dict=json.load(load_f)


        # print(load_dict['data'])
        dicts=load_dict['data']

        for dict in  dicts:
            m =Moview()
            m.postid=dict['postid']
            m.de=dict['wx_small_app_title']
            m.title=dict['title']
            m.pid=dict['pid']
            m.publish_time=dict['publish_time']
            m.like_num=dict['like_num']
            m.share_num=dict['share_num']
            m.post_type=dict['post_type']
            m.image=dict['image']
            m.request_url=dict['request_url']
            m.ispromote=dict['ispromote']
            m.isalbum=dict['isalbum']
            m.save()



    with open('/home/zhao/Documents/pywebproject/moviewsweb/banner.json','r') as load_f:
        load_dict=json.load(load_f)


        # print(load_dict['data'])
        dicts=load_dict['data']

        for dict in  dicts:
            banner= Banner()


            banner.end_time=dict['end_time']
            banner.addtime=dict['addtime']
            banner.title=dict['title']

            banner.userid=dict['userid']
            banner.description=dict['description']
            banner.bannerid=dict['bannerid']
            banner.start_time=dict['start_time']
            banner.count_click=dict['count_click']
            banner.uptime=dict['uptime']
            banner.status=dict['status']
            banner.orderid=dict['orderid']
            banner.type=dict['type']
            banner.cateid=dict['cateid']
            banner.url=dict['url']
            banner.object_id=dict['object_id']
            banner.image=dict['image']
            banner.save()


    return render(request, 'base.html')



def index(request):

    if request.is_ajax():
        moviewList = Moview.objects.all()
        list = []
        for m in moviewList:


            dict = {}
            dict['image'] = m.image
            dict['title'] = m.title
            dict['de'] = m.de
            dict['num']=m.like_num

            list.append(dict)

        return JsonResponse({'data':list})




    else:




        sliderList =Banner.objects.all()
        moviewList =Moview.objects.all()
        userName = request.session.get(request.COOKIES.get('name'))
        if userName:

            user =User.objects.get(usernmae=userName)
            return render(request, 'base.html',
                          {'sliderList': sliderList, 'moviewList': moviewList, 'status': userName,'user':user})

        else:
                return render(request,'base.html',{'sliderList':sliderList,'moviewList':moviewList,'status':userName})



def like(request):
    userName = request.session.get(request.COOKIES.get('name'))


    if  userName:

        if request.is_ajax():
            user = User.objects.get(usernmae=userName)


            status= request.POST.get('status')
            print(status)
            if status=='0':
                moviewsid = request.POST.get('postid')

                moviews= Moview.objects.get(postid=moviewsid)
                try:
                    likes=Like.objects.get(mid_id=moviews.id,uid_id=user.id)
                    like2 = moviews.like_num -1
                    likes.delete()
                    msg='收藏'

                except Exception as e:

                    like2=moviews.like_num+1
                    like = Like()
                    like.uid_id = user.id
                    like.mid_id = moviews.id
                    like.save()
                    msg = '取消收藏'
                moviews.like_num=like2
                moviews.save()

                return JsonResponse({'data':1,"like":like2,'msg':msg})

            else:
                print('----------------------')
                likes = Like.objects.filter(uid_id=user)
                moviews=Moview.objects.all()

                list=[]
                for m in moviews:
                    for l in likes:
                        if m.id==l.mid_id:
                            dict={}
                            dict['image']=m.image
                            dict['title']=m.title
                            dict['de']=m.de



                            list.append(dict)
                print(list)

                return JsonResponse({'data':list})




    else:


        return JsonResponse({'data':0})







def login(request):




    if request.method=='GET':
        return render(request, 'myApp/login.html')

    else:
       print('sssssssss')
       username=request.POST.get('username')
       password=request.POST.get('userPass')
       print(username,type(username))

       try:

           user =User.objects.get(usernmae=username)

       except User.DoesNotExist as e:
           return redirect("/login/")

       if password !=user.password:
           return redirect('/login/')

       user.userToken = str(time.time() + random.randrange(1, 100000))
       user.save()
       response=redirect('/index/')

       request.session["username"] = username
       response = redirect("/index/")
       response.set_cookie("name", "username")
    return response







def signup(request):
    if request.is_ajax():

        userAccont=request.POST.get('username')
        try:
            user=User.objects.get(usernmae=userAccont)
            return JsonResponse({'data':1})
        except User.DoesNotExist as e:
            return JsonResponse({'data':0})

    else:
        if request.method=='GET':
            return render(request,'myApp/register.html')

        else:
            userAccont=request.POST.get('userAccount')
            userpasswd=request.POST.get('userPasswd')
            useremail=request.POST.get('useremail')

            img =request.FILES.get('userImg')
            print(img)

            userToken = str(time.time() + random.randrange(1, 100000))

            user = User.createuser(userAccont, userpasswd, useremail, img, userToken)
            user.save()
            request.session["username"] = userAccont
            response = redirect("/index/")
            response.set_cookie("name", "username")
            response.set_cookie("token", userToken)
            return response


