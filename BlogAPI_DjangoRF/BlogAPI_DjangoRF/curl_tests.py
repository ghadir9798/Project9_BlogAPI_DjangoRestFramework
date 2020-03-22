'''

curl -X POST -d "username=ghadir9798&password=ghadir9798" http://127.0.0.1:8000/api/auth/token/

curl -X POST -H "Content-Type: application/json" -d '{"username":"ghadir9798","password":"ghadir9798"}' http://127.0.0.1:8000/api/auth/token/

"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImdoYWRpcjk3OTgiLCJleHAiOjE1ODQ4NTIxMTMsImVtYWlsIjoiZ2hhZGlyLnNoYXllZ2FuQGdtYWlsLmNvbSJ9.Ug5R1jqrAnrpHdO0yqY_G7gMi6yWpk49ITRbsGGbxiw"

curl -H "Authorization: JWT <your_token>" http://127.0.0.1:8000/api/comments/

curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImdoYWRpcjk3OTgiLCJleHAiOjE1ODQ4NTIxMTMsImVtYWlsIjoiZ2hhZGlyLnNoYXllZ2FuQGdtYWlsLmNvbSJ9.Ug5R1jqrAnrpHdO0yqY_G7gMi6yWpk49ITRbsGGbxiw" http://127.0.0.1:8000/api/comments/

curl -X POST -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImdoYWRpcjk3OTgiLCJleHAiOjE1ODQ4NTY5MjgsImVtYWlsIjoiZ2hhZGlyLnNoYXllZ2FuQGdtYWlsLmNvbSJ9.ImVcjvjssJ1rh8-P8cqp3wE8dmPAdiZzo1y5Cspj5Gk" -H "Content-Type: application/json" -d '{"content":"First comment on Post 3"}' "http://127.0.0.1:8000/api/comments/create/?slug=post-3&type=post"



'''