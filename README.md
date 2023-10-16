
## Features:

1. Admin Responsibilities:
   - Add new grocery items to the system
   - View existing grocery items
   - Remove grocery items from the system
   - Update details (e.g., name, price) of existing grocery items
   - Manage inventory levels of grocery items

2. User Responsibilities:
   - View the list of available grocery items
   - Ability to book multiple grocery items in a single order


## Installations and setup

- git clone `https://github.com/PujaShaw123/qp-assessment.git`

- Build the Docker image from the Dockerfile 
    - docker-compose build

- Start the containers
    - docker-compose up -d

- Create the "grocery_app" schema in the PostgreSQL container
    - docker exec -it postgres_container_2 psql -U postgres -c "CREATE SCHEMA grocery_app;"

- Restart the FastAPI container
    - docker-compose restart grocery_app_container_2
