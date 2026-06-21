# E-commerce platform
I will build an e-commerce platform that is scalable enough to handle 10000+ concurrent users.That is honestly for my learning process for stuff like Redis caching, Docker deployment, Docker compose, Nginx which is a traffic director, PostgreSQL which will be my main database and so many more.

# Project title and description
This project simulates a real-world online shopping platform where users can register, browse products, add items to the cart and place orders, or vice versa.
The main challenge to this problem is scalability - what happens when thousands of users want to the app at the same time and browse the same product information. This project tackles that by using:
- ** Redis ** to cache the frequently requested data so that the database does not get overwhelmed
- ** Docker ** to package the app so it runs identically on any machine
- ** Nginx ** to direct the traffic 

## Tech Stack
- ** Backend: ** FastAPI (Python)
- ** Frontend: ** HTML, CSS, and JavaScript
- ** Database: ** PostgreSQL which will store all the info about users, orders, products permenantly
- ** Cache: ** Redis which stores hot data temporarily for speed 
- ** Containers: ** Docker and Docker compose
- ** Load Balancer: ** Nginx

## How backend and frontend will connect together
* The user will push the button in the frontend part called "View the products button" that will be written with the HTML, CSS and JavaScript by me
* JavaScript will send a request to the backend every time the user performs an action 
* Fast-API will handle it, checks Redis, if the information is in the Redis which is a super high speed memory that checks the demanded information in the RAM, because RAM is a high speed memory, if the information is not in the Redis, it will ask the database for the required info, return it to the user, and later save a copy of that information in Redis.

## Structure of the project
ecommerce-platform/
│
├── docs/                        # All documentation
│   ├── architecture.md          # System design and diagrams
│   ├── api-spec.md              # Full API reference
│   └── data-model.md            # Database tables explained
│
├── frontend/                    # Everything the user sees
│   ├── index.html               # Home page
│   ├── css/
│   │   └── style.css  # Page styling
│   └── js/
│       └── main.js    # Sends requests to backend
│
├── backend/                     # Server side of the app
│   ├── Dockerfile               # Instructions to build backend container
│   ├── requirements.txt         # Python libraries the app needs
│   └── app/
│       ├── main.py              # Starting point of the app
│       ├── routes/              # Defines all API endpoints
│       ├── models/              # Defines database table structures
│       ├── services/            # Core business login
│       └── cache/               # All Redis caching logic
│
├── nginx/
│   └── nginx.conf               # Load balancer configuration
│
├── docker-compose.yml           # Runs all containers together
├── .env.example                 # Template for environment variables
└── README.md                    # This file

## Features
- User registration with JWT authentication 



