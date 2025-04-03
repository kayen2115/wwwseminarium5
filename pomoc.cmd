fetch('http://localhost:5000/api/user/kasia/entries')
  .then(res => res.json())
  .then(data => console.log(data));