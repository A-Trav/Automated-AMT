
# Automated AMT

Automated AMT is a console-based server application, designed with the purpose to provide users with the ability to integrate with a consistently updated database consisting of the AMT (Australian Medical Terminology) distribution, via a light-weight http server. This server aims to provide users with a RESTful API, allowing the integrated users of the service to manage and query the AMT distribution in-order to support their Clinical decision support needs. Furthermore, this project also provided a mapping between the AMT distribution, to the SNOMED (Systematized Nomenclature of Medicine) distribution, to allow users to make inference via their own Clinical decision support software.


## Authors

- Ashley Travaini


## Documentation

View the source code documentation here: [https://a-trav.github.io/Automated-AMT](https://a-trav.github.io/Automated-AMT)


## API Reference

## General Access Endpoints

All endpoints listed here require no authentication headers.

```bash
  GET /search/amt
  GET /search/amt/id
  GET /search/amt/unmapped
  GET /search/snomed/id
  GET /search/snomed
  GET /export
```

### Authentiation Endpoint

Authentication endpoint returns the required JWT token to be used to gain access to Admin
restricted endpoints.

```bash
  POST /auth
```

### Admin Restricted Endpoints

All endpoints listed here require a Bearer Authorization token generated from the application
authentication endpoint. 

```bash
  POST /create/amt
  POST /create/snomed
  POST /delete/amt
  POST /delete/amt/id
  PUT /update/snomed/AU_Substance_SCTID/id
  PUT /update/snomed/AU_Substance_SCTID
  PUT /update/snomed/Int_Substance_SCTID/id
  PUT /update/snomed/Int_Substance_SCTID
  DELETE /delete/snomed/id
  DELETE /delete/snomed
```

To see examples on how to interact with the applications endpoints, import the Postman collection
found here: [Automated AMT postman collection](https://github.com/A-Trav/Automated-AMT/blob/master/docs/Automated%20AMT.postman_collection.json)

## Features

- Built-in mapping from AMT distribution to SNOMED codings
- Admin User Context to protect distributions CRUD functionality
- Automated monthly retrieval of new AMT distributions, directly from the NCTS
- Suite of integration endpoints 
- Built-in email service to notify admin of critical application failures
- Export endpoint to easily download the AMT distribution with it's SNOMED codings as a CSV


## Installation

This application does not require any installation other than an installation of the projects
dependencies found in the Pipfile.lock. To setup this application for deployment, simply install 
python, followed by pipenv from this link: [pipenv install guide](https://pipenv.pypa.io/en/latest/).
Then simply run the following command in the project root directory: 

```bash
  pipenv shell
  pipenv install
```
    
## Deployment

Automated AMT has been built with the intent for users to deploy their own REST API locally.
To deploy this project, simply run the following command from the projects root directory:

```bash
  python ./Src/app.py
```

The application will now be hosted on the machine that it has been deployed on, and can be found 
via the **host machines IP Address on Port 8080**.

### _Optional deployment flags_

The application can be deployed and run with the following command line arguments:

```bash
  -debug        Runs the application with Flasks development server
  -set-admin    Force reset of the API's admin user, required a new admin user to be set on startup
```
## Running Tests

To run the applications test suite, use the following command in the applications root 
directory:

```bash
  pytest
```

