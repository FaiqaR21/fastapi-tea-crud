# FastAPI Tea CRUD API

A simple FastAPI application that allows you to **Create, Read, Update, and Delete (CRUD)** tea records.

---

## 🚀 How to Run the Project

Make sure you have **Python 3.7+** installed, then install FastAPI and Uvicorn:

```bash
pip install fastapi uvicorn
```

Run the server:

```bash
uvicorn first:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

---

## 📌 API Endpoints

| Method | Endpoint        | Description          | Request Body |
|--------|-----------------|----------------------|---------------|
| GET    | `/`             | Welcome message      | None |
| GET    | `/teas`         | Get all teas         | None |
| POST   | `/teas`         | Add a new tea        | `{ "id": 1, "name": "Green Tea", "origin": "China" }` |
| PUT    | `/teas/{tea_id}`| Update a tea         | `{ "id": 1, "name": "Updated Name", "origin": "Japan" }` |
| DELETE | `/teas/{tea_id}`| Delete a tea         | None |

---

## 📖 Interactive API Docs

Once the server is running, open:

➡️ **Swagger UI:** `http://127.0.0.1:8000/docs`  

---

## ✅ Example JSON for POST /teas

```json
{
  "id": 1,
  "name": "Green Tea",
  "origin": "China"
}
```

---

## 📌 Author

**Faiqa**  
GitHub: [@FaiqaR21](https://github.com/FaiqaR21)
