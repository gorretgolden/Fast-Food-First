const url_to =

    fetch("http://127.0.0.1:5000/menu/")
    .then((res) => {
        console.log(res);
        console.log("returned");
        return res.json();
    })
    .then((jsonData) => {
        console.log(jsonData);
        jsonData.menu.map(function(details) {
            console.log(details);
            const data = document.createElement("div");
            data.classList.add("card-body");
            data.innerHTML = `
     <img src=${details[5]}></img>
      <p>${details[1]}</p>
     <p>${details[2]}</p>
    <button id=${details[0]} class="btn-to-single-food" ><a href=${`../templates/single-product.html?id=${details[0]}`}>View Item</a></button>`;
            document.getElementById("food-details").append(data);
        });
    });