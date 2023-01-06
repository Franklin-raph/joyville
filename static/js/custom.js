$("document").ready(function(){
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


})