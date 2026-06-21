# E-commerce platform
I will build an e-commerce platform that is scalable enough to handle 10000+ concurrent users.That is honestly for my learning process for stuff like Redis caching, Docker deployment, Docker compose, Nginx which is a traffic director, PostgreSQL which will be my main database and so many more.

# Project title and description
This project simulates a real-world online shopping platform where users can register, browse products, add items to the cart and place orders, or vice versa.
The main challenge to this problem is scalability - what happens when thousands of users want to the app at the same time and browse the same product information. This project tackles that by using:
- ** Redis ** to cache the frequently requested data so that the database does not get overwhelmed
- ** Docker ** to package the app so it runs identically on any machine
- ** Nginx ** 

## Tech Stack
- ** Backend: ** FastAPI (Python)
- ** Frontend: ** HTML, CSS, and JavaScript
- ** Database: ** PostgreSQL
- ** Cache: ** Redis
- ** Containers: ** Docker and Docker compose
- ** Load Balancer: ** Nginx
## How backend and frontend will connect together
* The user will push "View the products button" that will be written by HTML, CSS
* JavaScript will send a request to the backend
* Fast-API will handle it, checks Redis, if the information is in the Redis which is a super high speed memory that checks the demanded information in the RAM, because RAM is a high speed memory, if the information is not in the Redis, it will ask the database for the required info, return it to the user, and later save a copy of that information in Redis.
## 


