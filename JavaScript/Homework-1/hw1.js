// 1) while confirm - Сделайте цикл с confirm, который продолжается по Отмена и заканчивается по ОК.
let res = confirm("Press 'OK' to close this window");
while (res === false) {
    let res = confirm("Press 'OK' to close this window");
    if (res === true) {
        break;
    }
}

// 2) cubes - Сформируйте массив из N элементов, содержащий в себе кубы индексов, т. е: [0,1,8,27,64...]
let cubes = [];
for (let i = 0; i < 30; i++) {
    cubes.push(i * i * i);
}
console.log(cubes);

// 3) Подсчитать сумму арифметической прогрессии от 1 до N c шагом 3 (1,4,7....) используя цикл for. N - получайте от юзера
let type = prompt('Input your number:');
let sum = 0;
for (let i = 1; i <= type; i = i + 3) {
    console.log(i); // result in console
    sum += i;
}
document.write(sum)


// 4*) Сформируйте строку с шахматной доской из вложенных циклов. Для перевода строки используйте \n. Код должен поддерживать легкое изменение размеров доски.
let m = 6;
let n = 4;
let text = '.#'
let result = '';
for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
        if (i % 2 === 0) {
            result += text;
        } else {
            result += text.split('').reverse().join('');
        }
    }
    result += '\n'
}
console.log(result);