//fetch products


fetch('http://127.0.0.1:5000/menu/').then((res) => {
        console.log(res)
        console.log('returned')
        return res.json()
    }).then((jsonData) => {
        const items = jsonData.menu
        console.log(items, items[0])
        const table_data = document.createElement('tr')

        items.map(function(details) {
            table_data.innerHTML += ` 
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
            document.getElementById('table-body').append(table_data)
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
// mydiv.append(data_table)