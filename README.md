📌 Django Authentication-Based Blog Application

A fully functional web application built using Django that implements secure user authentication, role-based access, blog management, and password reset functionality via email.

🚀 Features
🔐 User Authentication

User Registration

User Login & Logout

Secure password handling using Django’s built-in authentication system

Password reset via email (Mailtrap for testing)

👥 User Roles & Permissions

Admin User

Manage all blog posts

Full control via Django admin panel

Regular User

Create, view, and delete their own blog posts

Access personal dashboard and profile

📝 Blog Management

Create blog posts

View blogs in card-based layout

View blog details

Delete user-owned blogs

🎨 UI / UX

Modern card-based design

Consistent theme across login, register, forgot password, reset password, and dashboard, create blog, delete blog

Responsive layout

🛠 Tech Stack

Backend: Django (Python)

Frontend: HTML, CSS (custom card-based UI)

Authentication: Django built-in auth system

Email Service: Mailtrap (for password reset testing)

🔐 Password Reset Flow

User clicks Forgot Password

Enters registered email

Reset link sent via email

User sets a new password

Redirected to login page
