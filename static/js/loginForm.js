// const login_form = document.getElementById('login_form')
// const user_email = document.getElementById('user-email')
// const user_password = document.getElementById('user-password')

// login_form.addEventListener('submit', function(e) {
//     e.preventDefault()
//     var formdata = new FormData();
// formdata.append("email", user_email);
// formdata.append("user_password", user_password);

// var requestOptions = {
//   method: 'POST',
//   headers: {
//     'Content-Type': 'multipart/form-data'
//   },
//   body: formdata,
//   redirect: 'follow'
// };

//     const response = await fetch('http://127.0.0.1:5000/auth/login', requestOptions)

//     const result = await response.text();
//     console.log(result)
// })
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("Cookie", "session=.eJyrVopPy0kszkgtVrKKrlZSKAFSSsWlycmpxcVKOkqR-aUKOfnp6akpCpl5ClDxtNKcnEpFpdhanVENRGiIrQUATlN6uQ.Ykla5w.sj6RugwOF-gDnBPLB8LCs35t4Ug");

var raw = JSON.stringify({
  "email": "nabatanzigorret143@gmail.com",
  "user_password": "#golden@"
});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("http://127.0.0.1:5000/auth/login", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));