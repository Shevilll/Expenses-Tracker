const homepage = document.getElementById("HomePage");
homepage.style.display = "block";

function displaybuttonformdiv(value) {
    const buttonformdiv = document.querySelectorAll(".button-form-div");
    const buttonfordiv = document.querySelector(".buttonfordiv");
    buttonformdiv.forEach((button) => {
        button.style.display = value;
        console.log(button);
    });
}
