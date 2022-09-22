#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response using curl
curl -sI "$1" | awk '/Content-Length/{print $2}'
#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response

 EOF
