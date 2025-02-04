// MILAN DASHBOARD

let season_win_count = null;

// get ac milan image
console.log('about to get milan logo');


getLogo()
    .then(response => {
        console.log('funcion ran!')
    })
    .catch(error =>{
        console.log('error message incoming:')
        console.log(error)
    });

async function getLogo() {
    const response = await fetch('https://media.api-sports.io/football/teams/489.png');
    console.log(response);
    const blob = await response.blob();
    document.getElementById('img_milan').src = URL.createObjectURL(blob);
};

const local_data = "../output.json";
console.log("accessing local json")
console.log(local_data)
skewer.log(local_data)
