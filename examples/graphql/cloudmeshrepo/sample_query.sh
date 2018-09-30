curl -X POST \
-H "Content-Type: application/json;" \
-H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InVzZXIxIiwiZXhwIjoxNTM4MTY1ODc1LCJvcmlnX2lhdCI6MTUzODE2NTU3NX0.HUKZeM7GvjPmBUWuoIjUJZFPgf0DQFS3Du4okSdr2I4" \
-d '{"query": "{ repos { url } }"}' \
http://localhost:8000/graphql/
