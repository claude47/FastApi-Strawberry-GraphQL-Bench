## Simple FastApi with Strawberry GraphQL Bench

This repository contains a simple **GraphQL** implementation built with **FastAPI** and the **Strawberry** library. It's a practice project demonstrating GraphQL best practices and how to integrate these technologies effectively.
##

You can run the project locally by configuring a **.env** file and connecting to a **PostgreSQL** database, or alternatively, use the provided **docker-compose** setup for an easy, containerized environment.

After successfully running the application,
You can just access your running host and port with /graphQL endpoint. 

e.g. http://0.0.0.0:8000/graphql

Then you can proceed on doing the sample requests below.

**Query**

      query {
        getProducts {
          id
          productCode
          productName
          productDescription
        }
      }

**Mutation**
      
      mutation {
        createProduct(input: {
          productCode: "TEST-ITEM-CODE-1",
          productName: "TEST ITEM",
          productDescription: "This is a description for Test Item 1."
        }) {
          id
          productCode
          productName
          productDescription
        }
      }
