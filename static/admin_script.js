const userName = document.getElementById("name");
const password = document.getElementById("password");
const loginForm = document.getElementById("login");

//check to privent error
if (loginForm) {
    //check if the password is correct
    loginForm.addEventListener("click", function () {

        if (userName.value == "doctor" && password.value === "topsecret") {
        }
        else
            alert("Wrong username or password");
    });
}

