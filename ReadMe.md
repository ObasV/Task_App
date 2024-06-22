For superuser:

Username: Olusola
email: abc@gmail.com
Password: 12345678


auth/users/

auth/users/me/

auth/users/confirm/

auth/users/resend_activation/

auth/users/set_password/

auth/users/reset_password/

auth/users/reset_password_confirm/

auth/users/set_username/

auth/users/reset_username/

auth/users/reset_username_confirm/


task/list
task/detail/<int:pk>
task/create
task/update/<int:pk>
task/delete/<int:pk>





/token/login/ (Token Based Authentication)

/token/logout/
{
  "username": "Olusola",
  "password": "12345678"
}

USER
{
  "username": "zigma",
  "password": "secret_password",
  "email": "orieja@gail.com"
}

TASK
{
  "title": "Mob",
  "description": "Everywhere",
  "status": "In Progress",
  "priority": "Medium",
  "due_date": "",
  "category": "Domestic",
  "assigned_to": "Olusola"
}