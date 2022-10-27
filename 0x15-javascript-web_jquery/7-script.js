$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', (res) => {
    $('#character').text(res.name);
})
