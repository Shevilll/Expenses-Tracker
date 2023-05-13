const homepage = document.getElementById("HomePage");
homepage.style.display = "block";

function displaybuttonformdiv(value) {
    const buttonformdiv = document.querySelectorAll("#button-form-div");
    const buttonfordiv = document.querySelector("#buttonfordiv");
    const buttonforremovediv = document.querySelector("#buttonforremovediv");
    const buttoncheckeditems = document.querySelector("#buttoncheckeditems");

    buttonformdiv.forEach((button) => {
        button.style.display = value;
    });
    if (value == "none") {
        buttonfordiv.style.display = "block";
        buttonforremovediv.style.display = "none";
        buttoncheckeditems.style.display = "none";
    } else {
        buttonfordiv.style.display = "none";
        buttonforremovediv.style.display = "block";
        buttoncheckeditems.style.display = "block";
    }
}
