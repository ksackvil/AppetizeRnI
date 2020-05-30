var axios = require('axios')

const API_KEY = 'ecffb07ca4d24d5aba1c90a368d711eb';
const PLACE_ID = 'ipEq9ooT'
const BASE_ENDPOINT = `https://api.omnivore.io/1.0/locations/${PLACE_ID}`;
const GET_ITEMS = `${BASE_ENDPOINT}/menu/items`

axios.defaults.headers.common['Api-Key'] = API_KEY 

export async function getItems() {
    try {
        const res = await axios.get(GET_ITEMS)        
        return(res);
    } catch(err) {
        console.log(err)
    }
}