# README.md

# Teacher Management Application

This application serves as a platform for managing courses and teachers. It allows users to create courses, assign teachers to courses, and manage student enrollments.

## Recent Changes

### Sprint 6 Updates

- **Course-Teacher Relationship**: 
  - Added a new `teacher_id` field to the `Course` model to establish a relationship between courses and teachers. 
  - Updated course management services to handle the assignment of teachers to courses without modifying existing student functionalities.
  
- **Updated Application Structure**:
  - Enhanced the application structure to reflect the new teacher-course relationship. Relevant files updated include:
    - `src/models.py`: Contains the updated Course model to incorporate `teacher_id`.
    - `src/services.py`: Business logic related to the management of courses and teachers has been integrated.
  
### Notes on Implementation

- No modifications were made to existing `Student` entities, ensuring that current functionalities regarding student data remain intact.
- The teacher creation and retrieval processes remain unchanged from previous sprints, maintaining consistency in the application logic.
- All new functionality has been implemented using the existing technology stack, ensuring a smooth integration with prior code.
  
### Instructions for Developers

- Ensure to review the changes in `models.py` and `services.py` to understand the implications of adding `teacher_id` to the Course model.
- When adding functionalities related to teachers, abide by the current architecture to maintain application integrity.

## Getting Started

To get started with the application, set up your environment using the provided `.env.example` as a guide for necessary configurations. Install dependencies listed in `requirements.txt` and run the application.

For further details on specific services and testing, please refer to the respective files in the `src` and `tests` directories.