import axios from "axios";

//typed data
export interface User {
    id:       number;
    name:     string;
    username: string;
    email:    string;
    address:  Address;
    phone:    string;
    website:  string;
    company:  Company;
}

export interface Address {
    street:  string;
    suite:   string;
    city:    string;
    zipcode: string;
    geo:     Geo;
}

export interface Geo {
    lat: string;
    lng: string;
}

export interface Company {
    name:        string;
    catchPhrase: string;
    bs:          string;
}

const getUserId = async(idUser:number):Promise<User> => {
    const response = await axios.get<User>(`https://jsonplaceholder.typicode.com/users/${idUser}`);
    return response.data;
}

getUserId(1)
    .then((data) => console.log(data))
    .catch((err) => console.log(err))

    // {
    //     id: 1,
    //     name: 'Leanne Graham',
    //     username: 'Bret',
    //     email: 'Sincere@april.biz',
    //     address: {
    //       street: 'Kulas Light',
    //       suite: 'Apt. 556',
    //       city: 'Gwenborough',
    //       zipcode: '92998-3874',
    //       geo: { lat: '-37.3159', lng: '81.1496' }
    //     },
    //     phone: '1-770-736-8031 x56442',
    //     website: 'hildegard.org',
    //     company: {
    //       name: 'Romaguera-Crona',
    //       catchPhrase: 'Multi-layered client-server neural-net',
    //       bs: 'harness real-time e-markets'
    //     }
    //   }
      