//fetch products


fetch('http://127.0.0.1:5000/admin/food').then((res) => {
        console.log(res)
        console.log('returned')
        return res.json()
    }).then((jsonData) => {
        const items = jsonData.food
        console.log(items)
        const table_data = document.createElement('tr')

        items.map(function(details) {
            table_data.innerHTML = ` 
            <td>${details[0]}</td>
            <td>${details[1]}</td>
            <td>${details[2]}</td>
            <td>${details[3]}</td>
            <td>${details[4]}</td>
            <td><img src =${details[5]} alt="food-img"></td>
            <td>${details[6]}</td>
            <td><button>Update</button></td>
            <td><button>Delete</button></td>

         `
            console.log(details)
            document.getElementById('admin-food-table').append(table_data)
        });



    })
    //     const data_table = document.createElement('div')
    //     data_table.innerHTML = ` 


//         <tr>
//         <td>${details[0]}</td>
//         <td>${details[1]}</td>
//         <td>${details[3]}</td>
//         <td>${details[4]}</td>
//         <td>${details[5]}</td>
//         <td>${details[6]}</td>
//         <td>${details[0]}</td>
//         <td>ff</td>
//         <td>ff</td>
//         </tr>
//    `

// const mydiv = document.getElementsByClassName('.mydiv')
// mydiv.append(data_table)// fetch('http://127.0.0.1:5000/admin/food').then((res) => {
//     console.log(res)
//     console.log('returned')
//     return res.json()
// }).then((jsonData) => {

//     console.log(jsonData)
//     jsonData.menu.forEach(function(details) {
//         console.log(details)
//     });
// })

// const admin_menu_items = document.getElementById('admin-menu')
// const data_table = document.createElement('div')

// data_table.innerHTML = `<table class="table">
// <thead>
//     <tr>
//         <th>Food ID</th>
//         <th>Food Name</th>
//         <th>Food Description</th>
//         <th>Food Price</th>
//         <th>Food Stock Quantity</th>
//         <th>Food Image</th>
//         <th>Date Created</th>
//         <th>Edit</th>
//         <th>Delete</th>
//     </tr>
// </thead>
// <tbody id="admin-food-table">
//     <tr>
//     <td>ff</td>
//     <td>ff</td>
//     <td>ff</td>
//     <td>ff</td>
//     <td>ff</td>
//     <td>ff</td>
//     <td>ff</td>
//     <td>ff</td>
//     <td>ff</td>
//     </tr>
// </tbody>
// </table>`

// admin_menu_items.append(data_table)