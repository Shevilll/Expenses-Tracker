const body = document.getElementById("table-body");

function inserting() {
    fetch("/users")
        .then((response) => response.json())
        .then((data) => {
            data.forEach((row) => {
                const tr = document.createElement("tr");
                tr.innerHTML = `
        <td>${row[0]}</td>
        <td>${row[1]}</td>
        <td>${row[2]}</td>
        <td>${row[3]}</td>
        <td>${row[4]}</td>
        <td>${row[5]}</td>
        <td>${row[6]}</td>
        `;
                body.appendChild(tr);
            });
        })
        .catch((error) => console.error(error));
}
inserting();
