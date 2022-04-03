fetch('http://127.0.0.1:5000/users/').then((res) => {
        console.log(res)
        console.log('returned')
        return res.json()
    }).then((jsonData) => {
        const items = jsonData.users
        console.log(items)
        const table_data = document.createElement('tbody')

        items.map(function(details) {
            table_data.innerHTML += `
          
            <tr>
            <td>${details[0]}</td>
            <td>${details[1]}</td>
            <td>${details[2]}</td>
            <td>${details[3]}</td>
            <td>${details[4]}</td>
            <td>${details[6]}</td>
            <td><button>Update</button></td>
            <td><button>Delete</button></td>
            </tr>
         `
            console.log(details)
            document.getElementById('users').append(table_data)
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