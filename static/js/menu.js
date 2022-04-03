//fetch products


fetch('http://127.0.0.1:5000/menu/').then((res) => {
        console.log(res)
        console.log('returned')
        return res.json()
    }).then((jsonData) => {
        const items = jsonData.menu
        console.log(items)
        items.map(function(details) {
            const table_data = document.createElement('div')
            table_data.innerHTML += `
            <img src=${details[0]}></img>
            <p>${details[1]}<p>
            <p>${details[2]}</p>
            <button class='btn-to-single-food'>View Item</buttton>
      
         `
            console.log(details)
            document.getElementById('card-body').append(table_data)
            const btn = document.getElementsByClassName('btn-to-single-food')

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