$.get("https://swapi-api.hbtn.io/api/films/?format=json", (res) => {
    res.results.forEach(i => {
        $('UL#list_movies').append("<li>" + i.title + "</li>")
    });
})
