// function updateProd(el) {
//     memory_id = el.value
//     fetch('/in_memory/' + memory_id, {
//         method: 'patch',
//         headers: {'Content-Type': 'application/json'},
//     })
//     console.log(memory_id)
// }

function addCity() {
    let cityName = document.getElementById('city_name').value
    let date = document.getElementById('date').value
    fetch('/add', {
        method: 'post',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            'city_name': cityName,
            'date': date
        })
    })
//    console.log("Add")
}