# Error Response Structure for Invalid Requests

The following error response structure should be used for handling invalid requests in the Student Management Web Application API. This ensures that all error responses are consistent and provide clear information to the clients regarding the nature of the error.

### Error Response Format
For any invalid input or request failure, the API will return the following JSON structure:

```json
{
  "error": {
    "code": "E001",              // A unique error code
    "message": "Invalid input",   // A brief description of the error
    "details": {}                 // Additional details about the error (optional)
  }
}
```

### Explanation of Fields:
- **code**: A unique identifier for the error type. This can be used by client applications for handling specific errors programmatically.
- **message**: A user-friendly message that describes the issue in simple terms, helping the user understand what went wrong.
- **details**: An optional field that can contain further context about the error, such as validation error messages or specific fields that failed validation.

### Example Error Responses

1. **Invalid Student Name**
   If a request to create or update a student contains an invalid name (e.g., an empty string), the API might respond with:

   ```json
   {
     "error": {
       "code": "E001",
       "message": "Invalid input",
       "details": {
         "name": "Name cannot be empty"
       }
     }
   }
   ```

2. **Missing Required Fields**
   If a required field is missing in the request body, the response could look like:

   ```json
   {
     "error": {
       "code": "E001",
       "message": "Invalid input",
       "details": {
         "name": "Field 'name' is required"
       }
     }
   }
   ```

### Implementation Notes
- This error response structure should be applied across all endpoints that handle user inputs.
- Make sure to log the full error context on the server side for debugging purposes, without exposing sensitive information in the response sent to the client.

By following this structured error response format, the Student Management Web Application will facilitate easier error handling and improve the user experience when errors occur.