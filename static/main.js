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

function updatedropdown() {
    const dropdown_menu = document.querySelector(".dropdown-menu");
    const monthyear = JSON.parse(localStorage.getItem("monthyear")) || [];
    const now = new Date();
    const monthNames = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ];
    const monthYear = monthNames[now.getMonth()] + "-" + now.getFullYear();
    if (!monthyear.includes(monthYear)) {
        monthyear.push(monthYear);
        localStorage.setItem("monthyear", JSON.stringify(monthyear));
    }
    monthyear.forEach((item) => {
        const element = document.createElement("li");
        const button = document.createElement("button");
        button.className = "dropdown-item";
        button.role = "button";
        button.name = "monthyear";
        button.value = item.replace("-", "_");
        button.innerText = item;
        element.append(button);
        dropdown_menu.appendChild(element);
    });
}

updatedropdown();
