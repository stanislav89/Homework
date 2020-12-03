//const text = 'testId';
//const testId = document.getElementById(`${text}`);
//console.log('testId: ', testId);

//const divTest = document.getElementById('test');
//const pElem = document.createElement('p');
//divTest.appendChild(pElem);

//const test = document.getElementById('test');
//test.innerText = 123456789;
//console.log(test.innerText);

//var pass = new Array("123");
//var z;
//if (confirm("Hello")) {
    //z = prompt("Int password:");
    //if ($.inArray(z, pass) != -1){
        //alert("hello " + z);
    //}
    //else {
        //alert("user not found");
    //}
//}

//document.onmousemove = function(){
	//document.write("mouse move <br/>");
//}

//document.onmousedown = function(){
	//document.write("mouse move <br/");
//}

//const divElem = document.getElementById('Element');
//divElem.style.width = '300px';
//divElem.style.height = '300px';
//divElem.style.backgroundColor = 'red';

//const kv1 = document.getElementById('elem1');
//kv1.style.width = '50px';
//kv1.style.height = '50px';
//kv1.style.backgroundColor = 'blue';

//const kv2 = document.getElementById('elem2');
//kv2.style.width = '50px';
//kv2.style.height = '50px';
//kv2.style.backgroundColor = 'yellow';

//Element.addEventListener('click', (event) => {
	//console.log('event! ', event.target.className);
	//if (!event.target.id){
		//event.target.style.backgroundColor = 'white';
	//}
//});

//-----Регистрация-----
document.querySelector('button').addEventListener('click',()=> {
    
    let inputs = document.querySelectorAll('input');
 
    let obj = {
        login : inputs[0].value,
        password : inputs[1].value
    };
 
    console.log(`Логин: ${obj.login}, Пароль : ${obj.password}`);
});

//-----2-----
const test = document.getElementsByClassName('users');
const getName = (event) => {
	console.log(event.target.innerText);
}
for (let i = 0; i < test.length; i++) {
	test[i].addEventListener('click', getName);
}

//-----Таймер 2000 милисекунд на вывод hello в консоль-----
setTimeout(() => {
	console.log('hello');
}, 2000);

//-----GET запрос-----
let text = "test";                                                   // запрос на поиск
let promise = fetch('http://api.tvmaze.com/search/shows?q=${text}'); // поиск
//let promise = fetch('http://api.tvmaze.com/search/shows?q=qirls');
promise
.then((data) => {
	return data.json();
})
.then((items) => {
	console.log('items: ', items);
})