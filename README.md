# Clinic Appointment Management System

A Python-based application designed to streamline clinic operations by managing appointments efficiently. This system provides an intuitive GUI for users, handles backend operations with MySQL, and offers features like calendar integration and PDF reporting.

---

## 🛠 Features
- **Patient Management**: Register and manage patient details securely.
- **Appointment Scheduling**: Schedule, view, and manage appointments effortlessly.
- **Calendar Integration**: Integrated calendar for easy date selection.
- **PDF Reporting**: Export appointment schedules to PDF with detailed formatting.
- **User-Friendly Interface**: Responsive design using CustomTkinter.

---

## ⚙️ Technologies Used
- **Frontend**: Python (Tkinter with CustomTkinter)
- **Backend**: MySQL
- **Libraries**:  
  - `fpdf` for PDF generation  
  - `tkcalendar` for calendar integration  
  - `mysql-connector-python` for database interaction  

---

## 🚀 System Requirements
- Python 3.9+
- MySQL Server
- Required Python libraries:
  ```bash
  pip install mysql-connector-python fpdf tkcalendar customtkinter

---

## 📦 Installation
- Clone the repository:
  git clone https://github.com/nikammayu2800/clinic-appointment-system.git 
- Navigate to the project directory:
  cd clinic-appointment-system
- Set up the database:
  Import the provided SQL script (db_setup.sql) to create the necessary tables.
  Update database connection details in db_connection.py.
- Run the application:
  python main.py

---

## 🖼️ Screens and Functionalities
- Login Screen
  Secure authentication for staff members.
- Home Page
  Central navigation hub to access all features.
- Patient Registration
  Add new patients with the required details.
- Appointment Management
  View, schedule, and manage daily appointments.
- Export to PDF
  Generate and download appointment reports in PDF format.
- Logout Confirmation
  Prompt for secure logout.

---

## 🌟 Project Flow
- Frontend
  The GUI is built using Tkinter, with additional styling via CustomTkinter, providing a clean and responsive user experience.
- Backend
  Data is stored securely in a MySQL database, ensuring efficient and scalable management.
- Integration
  Python’s mysql-connector-python is used to handle communication between the application and the database.

---

## 🗂 Database Structure
- Tables:
  patients: Stores patient details.
  appointments: Manages appointment data.
  staff: Stores staff login credentials.

---

## 📈 Future Enhancements
- Implement email notifications for scheduled appointments.
- Add analytics dashboards for appointment and patient trends.
- Introduce role-based access for administrative features.

---

## ✨ Contributors
- Mayuri Yashwant Nikam
- GitHub
- nikammayu2800@gmail.com

---

## 📝 Additional Notes
For troubleshooting, check the logs directory for detailed error messages.
Feel free to raise issues or contribute enhancements via pull requests.

---

### How to Use
1. Save this file as `README.md` in the root directory of your GitHub repository.
2. Replace placeholder text like `yourusername`, `your.email@example.com`, and SQL script names with actual values.  
3. Push the updated repository to GitHub.  

This README file is comprehensive yet concise, covering all aspects of your project in a single document.
