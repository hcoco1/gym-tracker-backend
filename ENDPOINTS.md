To verify your API endpoints, let's test each one step-by-step using `curl` commands. Replace `YOUR_ACCESS_TOKEN` with the JWT token obtained from the login step.

---

### **1. Register a New User**

```bash
curl -X POST "https://gym-tracker-backend-3jsb.onrender.com/api/auth/register" \
-H "Content-Type: application/json" \
-d '{
    "username": "testuser1",
    "email": "user1@example.com",
    "password": "secretpassword123"
}'
```

**Expected Response (201 Created):**

```json
{
  "username": "testuser",
  "email": "user@example.com",
  "is_active": true,
  "id": 1,
  "created_at": "2024-03-10T12:34:56.789Z"
}
```

---

### **2. Login to Get JWT Token**

```bash
curl -X POST "http://localhost:8000/api/auth/token" \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "username=testuser&password=secretpassword123"
```

**Expected Response (200 OK):**

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "bearer"
}
```

---

### **3. Create Workout Sets (Authenticated)**

```bash
curl -X POST "http://localhost:8000/api/workouts/" \
-H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
-H "Content-Type: application/json" \
-d '[
    {
        "exercise": "Bench Press",
        "set_number": 1,
        "reps": 10,
        "weight": 135,
        "day": "Monday",
        "type": "Chest"
    }
]'
```

**Expected Response (201 Created):**

```json
[
    {
        "exercise": "Bench Press",
        "set_number": 1,
        "reps": 10,
        "weight": 135,
        "day": "Monday",
        "type": "Chest",
        "id": 1,
        "date": "2024-03-10T12:34:56.789Z",
        "user_id": 1
    }
]
```

---

### **4. Retrieve All Workouts (Authenticated)**

```bash
curl -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
http://localhost:8000/api/workouts/
```

**Expected Response (200 OK):**

```json
[
    {
        "exercise": "Bench Press",
        "set_number": 1,
        "reps": 10,
        "weight": 135,
        "day": "Monday",
        "type": "Chest",
        "id": 1,
        "date": "2024-03-10T12:34:56.789Z",
        "user_id": 1
    }
]
```

---

### **5. Update a Workout Set (Authenticated)**

```bash
curl -X PUT "http://localhost:8000/api/workouts/1" \
-H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
-H "Content-Type: application/json" \
-d '{
    "exercise": "Bench Press",
    "set_number": 1,
    "reps": 12,
    "weight": 135,
    "day": "Monday",
    "type": "Chest"
}'
```

**Expected Response (200 OK):**

```json
{
    "exercise": "Bench Press",
    "set_number": 1,
    "reps": 12,
    "weight": 135,
    "day": "Monday",
    "type": "Chest",
    "id": 1,
    "date": "2024-03-10T12:34:56.789Z",
    "user_id": 1
}
```

---

### **6. Delete a Workout Set (Authenticated)**

```bash
curl -X DELETE "http://localhost:8000/api/workouts/1" \
-H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

**Expected Response (200 OK):**

```json
{
    "message": "Workout set deleted successfully"
}
```

---

### **Verify Database State**

```bash
sqlite3 workouts.db
sqlite> SELECT * FROM users;
sqlite> SELECT * FROM workout_sets;
```

---

### **Troubleshooting Tips**

1. **Invalid Token**: Regenerate a token using the login endpoint.
2. **Missing Fields**: Ensure all required fields are included in requests.
3. **Database Locked**: Close any open SQLite connections.
4. **CORS Issues**: Verify middleware settings if using a frontend.

Let me know if any endpoint behaves unexpectedly! 🚀
