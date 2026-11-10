
import json
import boto3

# Connect to DynamoDB
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("StudentRecords")


def response(status_code, data):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(data, default=str)
    }


def lambda_handler(event, context):
    try:
        method = event.get("httpMethod", "GET")
        path_params = event.get("pathParameters") or {}
        student_id = path_params.get("id")

        body = event.get("body")
        data = json.loads(body) if isinstance(body, str) else (body or {})

        # CREATE student
        if method == "POST":
            if not data.get("id") or not data.get("name"):
                return response(400, {
                    "message": "id and name are required"
                })

            table.put_item(
                Item={
                    "ID": int(data["id"]),
                    "name": data["name"],
                    "course": data.get("course", "")
                },
                ConditionExpression="attribute_not_exists(ID)"
            )

            return response(201, {
                "message": "Student created successfully",
                "student": data
            })

        # READ all students
        elif method == "GET" and not student_id:
            result = table.scan()
            return response(200, result.get("Items", []))

        # READ one student
        elif method == "GET" and student_id:
            result = table.get_item(
                Key={"ID": int(student_id)}
            )

            item = result.get("Item")

            if not item:
                return response(404, {
                    "message": "Student not found"
                })

            return response(200, item)

        # UPDATE student
        elif method == "PUT" and student_id:
            updates = {
                key: value
                for key, value in data.items()
                if key in ["name", "course"]
            }

            if not updates:
                return response(400, {
                    "message": "Provide name or course to update"
                })

            expression_names = {
                f"#{key}": key for key in updates
            }

            expression_values = {
                f":{key}": value for key, value in updates.items()
            }

            result = table.update_item(
                Key={"ID": int(student_id)},
                UpdateExpression="SET " + ", ".join(
                    f"#{key} = :{key}" for key in updates
                ),
                ExpressionAttributeNames=expression_names,
                ExpressionAttributeValues=expression_values,
                ConditionExpression="attribute_exists(ID)",
                ReturnValues="ALL_NEW"
            )

            return response(200, {
                "message": "Student updated successfully",
                "student": result["Attributes"]
            })

        # DELETE student
        elif method == "DELETE" and student_id:
            table.delete_item(
                Key={"ID": int(student_id)},
                ConditionExpression="attribute_exists(ID)"
            )

            return response(200, {
                "message": "Student deleted successfully"
            })

        return response(400, {
            "message": "Invalid API request"
        })

    except ValueError:
        return response(400, {
            "message": "Student ID must be a valid number"
        })

    except dynamodb.meta.client.exceptions.ConditionalCheckFailedException:
        return response(404, {
            "message": "Student not found or already exists"
        })

    except Exception as error:
        print("Error:", str(error))
        return response(500, {
            "message": "Internal server error"
        })
