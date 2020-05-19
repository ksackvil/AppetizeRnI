var axios = require('axios')

API_KEY = 'ecffb07ca4d24d5aba1c90a368d711eb';
PLACE_ID = 'ipEq9ooT'
BASE_ENDPOINT = `https://api.omnivore.io/1.0/locations/${PLACE_ID}`;
GET_ITEMS = `${BASE_ENDPOINT}/menu/items`

axios.defaults.headers.common['Api-Key'] = API_KEY 

async function getItems() {
    try {
        const res = await axios.get(GET_ITEMS)        
        console.log(res);
    } catch(err) {
        console.log(err)
    }
}

getItems()