module petstore

import json
import clients.httpconnection

pub struct Pet {
pub mut:
    id   i64
    name string
    tag  string
}q

pub struct Pets {
pub mut:
    data []Pet
}

pub struct Error {
pub mut:
    code    int
    message string
}


pub struct PetstoreClient {
pub mut:
    connection &httpconnection.HTTPConnection
}

// Constructor for PetstoreClient
pub fn new_petstore_client() !PetstoreClient {
    return PetstoreClient{
        connection: httpconnection.new(name: 'petstore', url: 'http://petstore.swagger.io/v1')!
    }
}

// Method to list pets
pub fn (mut client PetstoreClient) list_pets(limit int) ![]Pet {
    params := if limit > 0 { map{'limit': limit.str()} } else { map{} }
    response := client.connection.get(prefix: '/pets', params: params)!

    if response.code != 200 {
        return error('Failed to list pets: $response.text')
    }

    return json.decode([]Pet, response.text)!
}

// Method to create a pet (assuming the API supports sending pet details in the request body)
pub fn (mut client PetstoreClient) create_pet(pet Pet) ! {
    pet_json := json.encode(pet)
    response := client.connection.post(prefix: '/pets', data: pet_json)!

    if response.code != 201 {
        return error('Failed to create pet: $response.text')
    }
}

//or also did

// Method to create a pet
pub fn (mut client PetstoreClient) create_pet(name string, tag string) ! {
    pet_json := json.encode(map{
        'name': name,
        'tag': tag
    })
    response := client.connection.post(prefix: '/pets', data: pet_json)!

    if response.code != 201 {
        return error('Failed to create pet: $response.text')
    }

    // Optionally, decode and return the created pet object if the API provides it in the response
    return json.decode(Pet, response.text)!
}
