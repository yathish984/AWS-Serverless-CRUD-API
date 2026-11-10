
# AWS Serverless CRUD API

A serverless REST API built using AWS Lambda, Amazon API Gateway, Amazon DynamoDB, and Python (Boto3) to perform Create, Read, Update, and Delete (CRUD) operations on student records.

## Project Overview

This project demonstrates how to build and deploy a serverless application on AWS. It allows users to manage student information through REST API endpoints without managing any physical servers.

The application uses AWS Lambda to execute Python business logic, API Gateway to expose REST endpoints, and DynamoDB to store student records.

## Technologies Used

- **AWS Lambda** – Executes Python CRUD operations.
- **Amazon API Gateway** – Creates and manages REST API endpoints.
- **Amazon DynamoDB** – NoSQL database for storing student records.
- **AWS IAM** – Manages permissions and access control.
- **Python** – Backend programming language.
- **Boto3** – AWS SDK for Python.
- **Postman** – API testing tool.
- **Git & GitHub** – Version control and project hosting.

## Architecture

```text
             Client / Postman
                    |
                    |
             Amazon API Gateway
                    |
                    |
               AWS Lambda
                (Python)
                    |
                    |
             Amazon DynamoDB
              StudentRecords
```

## Project Features

- Create new student records.
- Retrieve all student records.
- Retrieve a student using their ID.
- Update student details.
- Delete student records.
- Secure AWS resource access using IAM permissions.
- REST API integration with AWS Lambda.

## DynamoDB Configuration

**Table Name:** StudentRecords

| Attribute | Type | Description |
|---|---|---|
| ID | Number | Partition Key |
| name | String | Student Name |
| course | String | Student Course |

## API Endpoints

Base URL:

```text
https://nkjgyjzcei.execute-api.us-east-1.amazonaws.com/test/students
```

| HTTP Method | Endpoint | Description |
|---|---|---|
| POST | /students | Create a student |
| GET | /students | Retrieve all students |
| GET | /students/{id} | Retrieve a student by ID |
| PUT | /students/{id} | Update student details |
| DELETE | /students/{id} | Delete a student |

## API Testing Using Postman

### 1. Create Student (POST)

Endpoint:

```text
/test/students
```

Request Body:

```json
{
  "id": "101",
  "name": "Yathish",
  "course": "Cloud Computing"
}
```

Expected Response:

```json
{
  "message": "Student created successfully",
  "student": {
    "id": "101",
    "name": "Yathish",
    "course": "Cloud Computing"
  }
}
```

### 2. Get All Students (GET)

Endpoint:

```text
/test/students
```

### 3. Get Student By ID (GET)

Endpoint:

```text
/test/students/101
```

### 4. Update Student (PUT)

Endpoint:

```text
/test/students/101
```

Request Body:

```json
{
  "name": "Yathish Gowda",
  "course": "AWS Cloud Computing"
}
```

### 5. Delete Student (DELETE)

Endpoint:

```text
/test/students/101
```

## Project Folder Structure

```text
AWS-Serverless-CRUD-API/
│
├── lambda/
│   └── lambda_function.py
│
├── screenshots/
│   ├── dynamodb-table.png
│   ├── lambda-function.png
│   ├── api-gateway.png
│   ├── postman-create.png
│   └── postman-read.png
│
├── README.md
└── .gitignore
```

## AWS Deployment Steps

1. Create a DynamoDB table named `StudentRecords`.
2. Configure the partition key as `ID` with Number data type.
3. Create an IAM role with the required DynamoDB permissions.
4. Create an AWS Lambda function using Python.
5. Add the CRUD Python code to Lambda.
6. Connect Lambda with Amazon API Gateway.
7. Configure POST, GET, PUT, and DELETE methods.
8. Deploy the API to the `test` stage.
9. Test all API endpoints using Postman.

## Security

- IAM roles are used to grant Lambda only the required DynamoDB permissions.
- AWS credentials and secret keys must never be committed to GitHub.
- API access should be configured with appropriate authentication and authorization before production use.

## Learning Outcomes

- Understanding serverless architecture.
- Working with AWS Lambda and Python.
- Creating REST APIs using API Gateway.
- Performing CRUD operations using DynamoDB.
- Configuring IAM roles and policies.
- Testing REST APIs using Postman.
- Deploying cloud-based applications on AWS.

## Author

**Yathish Gowda M**

Information Science and Engineering

GitHub: https://github.com/yathish984

LinkedIn: https://www.linkedin.com/in/yathish984/

---

⭐ If you find this project useful, feel free to explore the repository!
