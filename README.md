# Grand Exchange Marketplace

> This project is based on  <a href="https://github.com/thomaspinckney3/cs4501">CS 4260 (Internet Scale Application)</a> course. This project is a three tier microservice Django Web Application. Layer 1: Models API, Layer 2: Service API, Layer 3: Web API. 

> The Grand Exchange Marketplace is a trading system for players to buy and sell all tradeable items. 

## Members of the Team
- Eric He 
- Dustin Nguyen
- Edward Cheng

## Installation

- This project uses Docker, Django, and Python.

### Clone

- Clone this repo to your local machine using `https://github.com/EricHe2000/GrandExchangeMarketPlace/`

### Setup

> Locate the cloned repo and run the docker-compose file:

```shell
$ cd GrandExchangeMarketPlace/
$ docker start mysql
$ docker-compose build
$ docker-compose up
```

> Check localhost to verify it is working.

```shell
$ localhost
```

---

## API Paths

- `Get`
    - `api/v1/item/<int:itemid>/`: Get item at itemid;
    - `api/v1/user/<int:userid>/`: Get user at userid;
    - `api/v1/item/hottest`: Get hottest item available;
    - `api/v1/item/cheapest`: Get cheapest item available;
    - `api/v1/item/getAll`: Get all of the recommendations for current item;
    - `api/v1/item/getSome`: Get the some of the top recommendations for current item;
    
- `Post`
    - `api/v1/user/create`: creates a new user;
    - `api/v1/item/createRec`: creates a new recommendation for current item;
    - `api/v1/user/login`: Creates authorization token for valid user;
    - `api/v1/auth/logout`: Deletes current authorization token for valid user;
