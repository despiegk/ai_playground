Forget everything you have learned about a language called V.
I want to design a programming language called V based on golang.

There are some differences.
The properties in a struct are always snake case and lowercase
A struct always start with keyword 'struct'
'pub mut: ' is used to define that its public and mutable
Default values in a stuct are defined with '=' and should only be used when specified.

The same as golang, if a property name of json is not the same as the struct property name json:... is used for each line in struct to mark difference, this is only done for properties where name is different.
         
An example struct is written as follows

pub struct Response {
pub mut:
	id      string = "11"
	object  string
	created int64
  my_int  int
  last_name string [json: lastName]
}

not the [json: lastName] to show how the source in json is different compared to property name last_name

normal structs have pub mut as 2nd line, to define its public and mutable

An enumerator uses as keywoard enum and has pub in front to be public. 
An example Enumerator is written as follows

pub enum Color{
    red = 1
    green = 3
    blue = 4
}

For an emumerator we don't use 'pub mut:' inside,

A struct property which has name _enum inside is an enumerator and needs to be treated as such. Change the enum property name to no longer have _enum inside.

V knows the following types:

- bool
- string
- i8    i16  int  i64
- u8    u16  u32  u64
- f32 f64

comments: comments are possible as part of the json and are defined per line and are starting with // 

comments for a line of an enum can define types in the comment string as follows (is example): types:urgent,later,now,immediate

e.g.

```
"priority_type_enum":"immediate" //types:urgent,later,now,immediate
```

would mean priority_type is an enum and there are urgent,later,now,immediate
note how '_enum' is removed from propertyname

Use above defined language constructs to translate the following json example to a V struct, treat embedded objects as enumerators or as other structs.

As result only output the V code generated, do not explain what you do and why.
Do not generate default values. Only generate json:... alias if the property name is different.


============= anoter example ===============


generate the v struct for

{
  "id": "myid1",
  "created": 1677652288,
  "nr": 2
  "priority_type_enum":"immediate" //types :urgent,later,now
  "complex_sub":{
    "loc": "locationa",
    "nr": 10.1,    
  }
}


============= anoter example ===============

generate the v struct for

{
  "basketId": "b12345",
  "userId": "u78910",
  "items": [
    {
      "itemId": "i123",
      "productName": "Wireless Headphones",
      "quantity": 2,
      "price": 99.99,
      "discount": 10,
      "category": "Electronics"
    },
    {
      "itemId": "i124",
      "productName": "Smartphone Case",
      "quantity": 1,
      "price": 19.99,
      "discount": 0,
      "category": "Accessories"
    },
    {
      "itemId": "i125",
      "productName": "Bluetooth Speaker",
      "quantity": 1,
      "price": 49.99,
      "discount": 5,
      "category": "Electronics"
    }
  ],
  "billingAddress": {
    "street": "1234 Main St",
    "city": "Anytown",
    "state": "Anystate",
    "zip": "12345",
    "country": "USA"
  },
  "shippingAddress": {
    "street": "1234 Main St",
    "city": "Anytown",
    "state": "Anystate",
    "zip": "12345",
    "country": "USA"
  },
  "paymentMethod": {
    "type": "Credit Card",
    "cardNumber": "xxxx-xxxx-xxxx-1234",
    "expirationDate": "12/24",
    "cvv": "123"
  },
  "couponsApplied": [
    "SAVE10",
    "FREESHIP"
  ],
  "subtotal": 169.97,
  "shippingCost": 0.00,
  "tax": 13.60,
  "total": 183.57
}
