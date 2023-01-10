$("document").ready(function(){
    console.log("hbxvhbzhxv")
    let onetime=document.querySelector("#onetime")
// Get csrf_token cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');
// end the csrf_token function
console.log("sabfh")
// send newletter email to the backend to process

$("#newsletterform").on("submit",function(e){
    e.preventDefault();
    console.log("submitted")
    $.ajax({
        type:"POST",
        url:"/newsletter/",
        data:{
            "email":$("#newsletter").val()
        },
        headers: {'X-CSRFToken': getCookie('csrftoken')},
        success:function(resp){
            alert(resp)
            document.querySelector("#newsletterform").reset()
        },
        error:function(err){
            console.log(err)
            alert("Email already a subscriber !")
        }
    })
})

// sending contact mail

$("#contactform").on("submit",function(e){
    e.preventDefault()
    console.log("contact processing")
    $.ajax({
        type:"POST",
        url:"/contactmail/",
        data:{
            "email":$("#formemail").val(),
            "name":$("#formname").val(),
            "subject":$("#formsubject").val(),
            "phone":$("#formphone").val(),
            "message":$("#formmessage").val(),
            

        },
        headers: {'X-CSRFToken': getCookie('csrftoken')},
        success:function(resp){
            alert(resp)
            document.querySelector("#contactform").reset()
        },
        error:function(err){
            console.log(err)
            alert("Network error !")
        }

    })

})

// room booking email submission function

$("#roombooking").submit(function(e){
    e.preventDefault();
    $.ajax({
        type:"POST",
        url:"/bookroom/",
        data:{
            "firstname":$(".firstname").val(),
            "lastname":$(".lastname").val(),
            "arrival":$("#arrival").val(),
            "depature":$("#depature").val(),
            "email":$(".email").val(),
            "PhoneNumber":$("#PhoneNumber").val(),
            "adults":$("#adults").val(),
            "childern":$("#childern").val(),
            "roomPrefrence":$("#roomPrefrence").val(),

        },
        headers: {'X-CSRFToken': getCookie('csrftoken')},
        success:function(resp){
            console.log(resp)
             $(".booking").html(`<div class="alert alert-success" role="alert">
              ${resp.msg}
            </div>`)
            document.querySelector("#roombooking").reset()
            $(".booking").fadeOut(20000)

        },
        error:function(err){
            $(".booking").html(`<div class="alert alert-danger" role="alert">
              Room Booking not successful trt again later !!
            </div>`)
            $(".booking").fadeOut(20000)
        }
    })
})



})


