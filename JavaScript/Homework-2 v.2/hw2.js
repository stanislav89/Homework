// GET запрос, поиск фильмов
let submit = document.getElementById('search');
let films = document.getElementById('films');

submit.addEventListener('click', (event) => {
    let inputValue = document.getElementById('user_input').value;
    let response = fetch(`http://api.tvmaze.com/search/shows?q=${inputValue}`);
    response
        .then((data) => {
            return data.json()
        })
        .then(items => {
            console.log('Movies: ', items)
            search(items)
        })
});


function search(items) {
    films.innerHTML = '';
    for (let i = 0; i < items.length; i++) {
        let div = document.createElement('div');
        div.classList.add('block');
        let p = document.createElement('p');
        p.innerHTML = `Name: ${items[i]['show']['name']}`;
        let img = document.createElement('img');
        img.setAttribute('src', `${items[i]['show']['image']['medium']}`);
        div.appendChild(p);
        div.appendChild(img);
        films.appendChild(div);
    }
}