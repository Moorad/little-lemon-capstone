If you are intending to run the project please make sure to update database credentials in the `settings.py` including the database name.
    
## Grading Criteria:
Q: Does the web application use Django to serve static HTML content?

A: Yes visit http://127.0.0.1:8000/restaurant/

---

Q: Has the learner committed the project to a Git repository?

A: Yes, you git cloned it! You can use `git log` to see my commit history.

---

Q: Does the application connect the backend to a MySQL database?

A: Yes, check `settings.py`

---

Q: Are the menu and table booking APIs implemented?

A: Yes,
- http://127.0.0.1:8000/restaurant/menu/ for menu API 
- http://127.0.0.1:8000/restaurant/booking/tables/ for table booking API

---

Q: Is the application set up with user registration and authentication?

A: Yes, you can use any djoser endpoint to test such as http://127.0.0.1:8000/auth/users/

---

Q: Does the application contain unit tests?

A: Yes, in `resturants/tests` folder

---

Q: Can the API be tested with the Insomnia REST client?

A: Yes, you can try :)