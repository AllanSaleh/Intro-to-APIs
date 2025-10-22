# JSON stands for: JavaScript Object Notation
# despite this, it can read translate across all languages not just javascript

# -- This makes it an incredibly useful language for apis
# It is also very lightweight making it east to pass back and forth between server and client
# Structured into objects that look like dictionaries

# ---------------- Status Codes ------------------
#  - 200 OK - request was successful
#  - 201 - Successful creation
#  - 204 - No Content - Send the request successfully, but didn't get any data back

# 300 - Redirect
# 301 - Moved around permanently: continuous redirection

# 400s - Client Error (Your mistake)
# 400 - Bad Request: either malformed or missing data
# 401 - Unauthorized: You don't have the proper credentials
# 404 - Not Found: The resource does not exist
# 429 - Too many requests: exceeded the max amount of requests for a certain resource

# 500 - Server Error (Their problem)

# 500 - Internal server error - something broke on their end
# 503 - Service unavailable - Temporarily down for maintenance
# 504 - Gateway timeout - Server took too long to respond