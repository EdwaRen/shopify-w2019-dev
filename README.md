# shopify-w2019-dev

## Installation
Docker and python are needed to get this project working. Once the prequisites are dealt with, simply run via docker
<br />
It is recommended to run the start script to get a database setup with some prepopulated values for ease of testing
```
$ python start.py 
```


```
$ docker-compose build
$ docker-compose up
```

## API
Browsable API is enabled, hence visiting the API link in your url will simulate a GET request
### Shop
```
http://localhost:8000/Market/shop
```
Supports GET, POST

### Product
```
http://localhost:8000/Market/product/
```
Supports GET, POST

### Order
```
http://localhost:8000/Market/order/'
```
Supports GET, POST


### LineItem
```
http://localhost:8000/Market/line/
```


## Admin GUI
```
http://localhost:8000/admin/Market/shop/
```
Visit the link above in your browser to see the relations between objects and edit them within the browser.

Username: admin<br />
Password: adminadmin