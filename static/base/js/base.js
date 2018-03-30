$(document).ready(function () {




    var swiper = new Swiper('#topslider',{

        direction:"horizontal",
        loop:true,
        speed:500,
        autoplay:2000,
        pagination:{
            el:'.swiper-pagination',
        }
    })


    $(".now").bind('click',function () {
        $(this).addClass('active')
        $(this).siblings().removeClass('active')

    })

    $('.like').bind('click',function () {

        var aa= $(this).attr('pd')

            $.post("/like/",{'status':0,'postid':aa},
                function (data,status) {

              if (data.data==0) {
                    location.href='/login/'

              }else{
                     $('#like'+aa).html(data.msg+data.like)
              }

                })
    })

    $('#likels').bind('click',function () {


        $.post('/like/',{'status':1,},function (data) {
            post =data.data;
            var htmls='';

            for(var i=0;i<post.length;i++){


                htmls+="<div class='item'><div class='left'>" +
                    "<img src=' "+post[i].image+"'></div>" +
                    "<div class='right'> <h3> "+post[i].title+"</h3><p>"+post[i].de+"</p></div></div><br>"


            }
            $('#maindiv').html(htmls)

        })
    })

        $('#mvies').bind('click',function () {


        $.post('/index/',function (data) {
            post =data.data;
            var htmls='';

            for(var i=0;i<post.length;i++){


                htmls+="<div class='item'><div class='left'>" +
                    "<img src=' "+post[i].image+"'></div>" +
                    "<div class='right'> <h3> "+post[i].title+"</h3><p>"+post[i].de+"</p></div></div><br>"


            }
            $('#maindiv').html(htmls)

        })
    })








})
