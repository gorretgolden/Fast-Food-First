let url = window.location.href;
let id = url.split("=")[1];


fetch(`http://127.0.0.1:5000/menu/${id}`).then((res) => {
    
    return res.json()
})
.then((jsonData) => {
    console.log(jsonData)
   const data = document.createElement('div')
   data.innerHTML = `    
   <form method = "POST">
   <div class = "card">
   <img class="products"  src=${jsonData.image} alt = "food-image" >
   <div class="name" >
   <p>${jsonData.name} </p> 
   <p> USH </p>
    <p> ${jsonData.description} </p>
     <br>
   <input type = "hidden" name = "food_id" value = "${jsonData.id}"/>

   <input minlength = "1"
   required style = "width:100px"
   type = "text"
   name = "quantity"
   value = "1" />

   <input style = "width:100px;height:50px" type = "submit" value= "Make Order "/>
   </div>
    </div>
     </form>`
     document.getElementById('singleitem').append(data)
  
}).catch(err=>alert(err.message))


