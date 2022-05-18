# shopify-challenge

The following documentation describes the usage for a REST API built using flask.

## API Documentation

### Definitions
- *Parcel*: Resource in the database that represents a product that needs to be shipped by the logistics company
- *Shipment*: Resource used to represent a "shipment" made by the logistics company
- *Category*: Resource used to represent categories that producs (parcels) belong to


### Create Parcel

A POST endpoint that allows the client to create a new parcel
<br>

- `Path`: `<host_address>/admin/parcel`

![image](https://user-images.githubusercontent.com/45743339/168908318-72694734-beb8-47cb-9888-226786a9c3bf.png)


### Edit Parcel

A PATCH endpoint that allows the client to edit an existing parcel.
<br>

- `Path`: `<host_address>/admin/parcel/<parcel_id>`
- "<parcel_id>" This refers to a dynamic path, that's passed as part of the url when calling the API on that endpoint.

![image](https://user-images.githubusercontent.com/45743339/168909534-66a84df2-0ac1-45f3-bd1d-ae1e06400818.png)

### Delete Parcel

A DELETE endpoint that allows the client to delete an existing parcel.
<br>

- `Path`: `<host_address>/admin/parcel/<parcel_id>`
- "<parcel_id>" This refers to a dynamic path, that's passed as part of the url when calling the API on that endpoint.

![image](https://user-images.githubusercontent.com/45743339/168911121-a2783e87-395a-40d2-86dd-3ae0fc088199.png)

### Fetch Single Parcel

This endpoint allows the client to fetch a single parcel item by its id, similar to the "delete" and "edit" endpoints the path
also has a dynamic part where the client specifies the id of the parcel to be fetched.

- `Path`: `<host_address>/admin/parcel/<parcel_id>`
- "<parcel_id>"  This refers to a dynamic path, that's passed as part of the url when calling the API on that endpoint.

<br>
![image](https://user-images.githubusercontent.com/45743339/168911345-44166691-d3d4-47a5-9ec8-648bb71282e1.png)


### Fetch Parcels by page

Here we can request for a list of all parcels in pages. Each page contains 10 parcels at most.

- `Path`: `<host_address>/admin/parcel/<page_no>`
- "<page_no>" This refers to a dynamic path, that's passed as part of the url when calling the API on that endpoint.

<br>

![image](https://user-images.githubusercontent.com/45743339/168911733-6430c273-37a6-43e5-a5de-67a92273c1b1.png)

### Create new shipment

This enpoint is responsible for creating a new shipment, using the parcel id.

- `Path`: `<host_address>/shipment/<parcel_id>`
- "<parcel_id>": This refers to a dynamic path, that's passed as part of the url when calling the API on that endpoint.

<br>

![image](https://user-images.githubusercontent.com/45743339/169054865-12bb7f04-21cb-4081-b8bc-9be2c74f89e9.png)


### Update Shipment Status

This endpoint can be used to update a shipment's status and other information as needed, via a PATCH request

- `path`: `<hostname>/shipment/<shipment_id>/<status_id>
- "<shipment_id>": This refers to a dynamic path, that's passed as part of the url when calling the API on that endpoint.
- "<status_id>":  This refers to a dynamic path, that's passed as part of the url when calling the API on that endpoint. This in particular is
 typically one of 3 numbers, where each one represents a distinct status as shown below:
 
 
 ![image](https://user-images.githubusercontent.com/45743339/169057721-43892b7b-a03a-4750-93ee-c535bd0cd964.png)
 
 <br>
 
 Example request
 <br>
 

![image](https://user-images.githubusercontent.com/45743339/169057967-06f19916-a961-4b7b-bad8-54bc00cee03b.png)

<br>

### Add new category

Allows admin to add new parcel category

- `path`: `<hostname>/admin/category`
- method: POST

<br>

![image](https://user-images.githubusercontent.com/45743339/169058973-a2ac66a9-2858-461e-bdb6-9dd1b01658c0.png)

