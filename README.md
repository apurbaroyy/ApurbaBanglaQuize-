Apurba Bangla Quiz App
🟩 Abstract

This project presents a Bengali-language interactive quiz application built using Java Swing for the GUI and MySQL as the backend database.
The system allows users to participate in a quiz, store scores, and view previous results.
The project focuses on usability for native Bangla users and demonstrates GUI programming, event handling, and database connectivity in Java.
🟨 Key Features
🔶 1. Bengali Language Interface

All UI elements, questions, answers, and messages are fully in Bangla.

Implemented using Noto Sans Bengali & Vrinda fallback fonts.

🔶 2. Multi-Panel Interface (CardLayout)

Home Panel

Quiz Panel

Score Panel

Smooth navigation using CardLayout.

🔶 3. Quiz System

Contains 5 basic mathematical questions.

Real-time answer validation with instant feedback.

Score calculation performed dynamically.

🔶 4. MySQL Database Integration

Stores:

User’s Name

Email

Individual question results

Total Score

Users can view the complete history of stored results.

🔶 5. Error Handling & Validation

Empty input detection

Database error notification

User-friendly dialogs
🟫 System Architecture
🧩 Frontend:

Java Swing

CardLayout-based multi-screen design

JOptionPane dialogs for user inputs

🧩 Backend:

MySQL database

JDBC connectivity

Secure data insertion using PreparedStatement
🧩 Workflow Overview:
Home Screen
<img width="602" height="486" alt="Screenshot 2025-12-12 180748" src="https://github.com/user-attachments/assets/a5b38192-e02d-442e-ba5b-809dcab46f69" />
Quiz Question Screen
<img width="602" height="472" alt="Screenshot 2025-12-12 181030" src="https://github.com/user-attachments/assets/4efe1b68-9dda-4313-ae77-c3ee09fc3c93" />
<img width="594" height="518" alt="Screenshot 2025-12-12 181111" src="https://github.com/user-attachments/assets/723074d2-6660-433d-8133-d95efbf41dcd" />
Score Page
<img width="599" height="486" alt="Screenshot 2025-12-12 181150" src="https://github.com/user-attachments/assets/9f48a77e-d43b-4457-9abc-9166a00f403c" />
MySQL table data view
<img width="611" height="489" alt="Screenshot 2025-12-12 182625" src="https://github.com/user-attachments/assets/bc4d1104-8302-4b96-9e8e-b505b46c456b" />





🟫 Conclusion

The Apurba Bangla Quiz App is a complete Java-based educational tool that makes learning interactive for Bangla-speaking users.
It showcases strong fundamentals in object-oriented programming, GUI development, and database connectivity.
This system can be extended for use in schools, coaching centers, and online learning platforms.

🟩 Future Work

Add multiple-choice questions (MCQ)

Timer-based quizzes

Student login & authentication

Leaderboard system

Cloud-hosted backend

Android version using Java/Kotlin

