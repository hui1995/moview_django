$(document).ready(function () {






    $("#account").bind("blur",function () {



    //    格式判断
        if ($(this).val().length<6 || $(this).val().length>12){


            $("#user_tip").html('格式错误')
        }

    //    账号是否重复


        $.post("signup/",{"username":$(this).val()},
            function (data,status) {

            if(data.data){

                     $("#user_tip").html('密码已存在')

            }

            }


        )
    //
    //     $.post("/register",{"userAccount":$(this).val()},
    //
    //
    //         function (data,status) {
    //
    //         if (data.data){
    //
    //
    //
    //         alert('ssssssssssss')
    //
    //         }



    })


      $("#account").bind("focus",function () {
          $("#user_tip").html('请输入6-16位用户名 ')


    })






    $("#pass").bind("blur",function () {



        if ($(this).val().length<6||  $(this).val().length>16){
             $("#pwd_tip").html('密码不符合规则')
        }

    })


     $("#pass").bind("focus",function () {
          $(this).val("")
          $("#passwd").html('请输入6位以上拼音字母组合密码 ')

    })


    $("#passwd").bind("blur",function () {

        if ($(this).val()!=$("#pass").val()){

            $("#pwd2_tip").html('两次密码不一致')
        }

    })
    $("#passwd").bind("focus",function () {

            $("#pwd2_tip").html('请再次输入6位以上拼音字母组合密码')

    })



})