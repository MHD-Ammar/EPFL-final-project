const userName = document.getElementById("name");
const password = document.getElementById("password");
const loginForm = document.getElementById("login");
if (loginForm) {
    loginForm.addEventListener("click", function () {

        if (userName.value == "doctor" && password.value === "topsecret") {
        }
        else
            alert("Wrong username or password");
    });
}

