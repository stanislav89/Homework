// GET запрос, поиск фильмов
let submit = document.getElementById('search');

submit.addEventListener('click', (event) => {
    let inputValue = document.getElementById('user_input').value;
    let response = fetch(`http://api.tvmaze.com/search/shows?q=${inputValue}`);
    response
        .then((data) => {
            return data.json()
        })
        .then(items => {
            console.log('Movies: ', items)
            for (let i = 0; i < items.length; i++ ) {
                document.write(`<p>Name: ${items[i]['show']['name']}</p>`)
                document.write(`<img src="${items[i]['show']['image']['medium']}" alt="${items[0]['show']['name']}" \>`)
            }
        })
});