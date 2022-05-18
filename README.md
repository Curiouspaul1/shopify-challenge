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


