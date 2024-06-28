//SignUp SignUpName SignUpEmail SignUpPassword signInEmail signInPassword

var SignUp =document.getElementById("SignUp");
var SignUpName =document.getElementById("SignUpName");
var SignUpEmail =document.getElementById("SignUpEmail");
var SignUpPassword =document.getElementById("SignUpPassword");
var MessageFail =document.querySelector(".MessageFail");
var MessageSuccess=document.querySelector(".MessageSuccess");
var signInEmail =document.getElementById("signInEmail");
var signInPassword =document.getElementById("signInPassword");
var login =document.getElementById("login");
var message=document.querySelector(".message");
var incorrect =document.querySelector(".incorrect");
// var username =document.getElementById("username");
var PersonContainer ;
// console.log(username);
if( localStorage.getItem("persons")==null ){
    PersonContainer=[];
}
else{
    PersonContainer = JSON.parse(localStorage.getItem("persons"));
}
if(SignUp != null){
SignUp.addEventListener("click",function(){
    AddPerson()
})
}
function AddPerson(){
    // console.log(SignUpName.value ,SignUpEmail.value ,SignUpPassword.value);
    if(SignUpName.value=="" || SignUpEmail.value =="" ||SignUpPassword.value ==""){
        MessageFail.classList.replace("d-none","d-block");

    }
    else if(SignUpName.value!="" && SignUpEmail.value !="" &&SignUpPassword.value !=""){
        MessageFail.classList.replace("d-block","d-none");
        var person={
            name:SignUpName.value,
            email:SignUpEmail.value,
            pass:SignUpPassword.value,
        }
        
        PersonContainer.push(person);
        localStorage.setItem("persons",JSON.stringify(PersonContainer));
        MessageSuccess.classList.replace("d-none","d-block");
        clear()
        location.href="login";
    }
    
    // console.log(PersonContainer);
}

if(login != null){
    login.addEventListener("click",function(){
        checkPerson();
    })
}

function  checkPerson(){
    if(signInEmail.value !="" && signInPassword.value!=""){
        message.classList.replace("d-block","d-none");
       if( check()){
        incorrect.classList.replace("d-block","d-none");
        location.href="prediction.html"
        // console.log("true");

       }
       else{
        incorrect.classList.replace("d-none","d-block");
       }
        
    }
    else{
        // console.log("error")
        message.classList.replace("d-none","d-block");
    }
}
function check(){
    // console.log(signInEmail.value ,signInPassword.value)
    for(var i=0 ;i<PersonContainer.length;i++){
        if(PersonContainer[i].email.toLowerCase()==signInEmail.value.toLowerCase() &&PersonContainer[i].pass.toLowerCase()==signInPassword.value.toLowerCase() ){
            // console.log(PersonContainer[i].name);
            localStorage.setItem("name",JSON.stringify(PersonContainer[i].name));
            return true;
        }
        
    }
}




function clear(){
    SignUpName.value="" ;
    SignUpEmail.value="" ;
    SignUpPassword.value ="";
}

document.addEventListener('DOMContentLoaded', function() {
    var iframe = document.getElementById('iframe');

    // استهداف الروابط وتحويلها للانتقال داخل الإطار
    var links = document.querySelectorAll('a[target="iframe"]');
    links.forEach(function(link) {
        link.addEventListener('click', function(event) {
            event.preventDefault(); // منع الانتقال الافتراضي
            var url = this.getAttribute('href');
            iframe.src = url; // تحديث عنوان الإطار ليعرض الصفحة المطلوبة
        });
    });
});