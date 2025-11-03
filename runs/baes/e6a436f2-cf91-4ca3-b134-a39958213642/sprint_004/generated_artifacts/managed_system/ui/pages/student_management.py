import os
import json
import streamlit as st
import requests
from typing import List, Dict, Any, Optional

# API Configuration
API_PORT = os.getenv("REALWORLD_FASTAPI_PORT", "8000")
API_BASE_URL = f"http://localhost:{API_PORT}"

def create_student(data: Dict[str, Any]) -> bool:
    """Create a new Student."""
    try:
        response = requests.post(f"{API_BASE_URL}/api/students/", json=data)
        response.raise_for_status()
        if response.status_code == 201:
            st.success(f"Student created successfully!")
            return True
        return False
    except requests.exceptions.RequestException as e:
        st.error(f"Error creating student: {e}")
        return False

def get_students() -> List[Dict[str, Any]]:
    """Get all Students."""
    try:
        response = requests.get(f"{API_BASE_URL}/api/students/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching students: {e}")
        return []

def update_student(id: int, data: Dict[str, Any]) -> bool:
    """Update an existing Student."""
    try:
        response = requests.put(f"{API_BASE_URL}/api/students/{id}", json=data)
        response.raise_for_status()
        if response.status_code == 200:
            st.success(f"Student updated successfully!")
            return True
        return False
    except requests.exceptions.RequestException as e:
        st.error(f"Error updating student: {e}")
        return False

def delete_student(id: int) -> bool:
    """Delete a Student."""
    try:
        response = requests.delete(f"{API_BASE_URL}/api/students/{id}")
        response.raise_for_status()
        if response.status_code == 204:
            st.success(f"Student deleted successfully!")
            return True
        return False
    except requests.exceptions.RequestException as e:
        st.error(f"Error deleting student: {e}")
        return False

def main():
    """Main Student management interface."""
    st.title("Student Management")
    
    # Create tabs for different operations
    tab1, tab2, tab3 = st.tabs(["List Students", "Add Student", "Edit Student"])
    
    with tab1:
        show_student_list()
    
    with tab2:
        show_student_form()
    
    with tab3:
        show_student_edit()

def show_student_list():
    """Display list of Students."""
    st.header("All Students")
    
    if st.button("Refresh", key="refresh_list"):
        st.rerun()
    
        # Fetch related data for course
    try:
        course_resp = requests.get(f"{API_BASE_URL}/api/courses/")
        course_resp.raise_for_status()
        course_data = course_resp.json()
        course_options = {item['id']: item.get('name', str(item['id'])) for item in course_data}
    except (requests.exceptions.RequestException, json.JSONDecodeError):
        course_options = {}
        st.warning('Failed to load course options')
    
    students = get_students()
    
    if students:
        for student in students:
            with st.expander(f"Student: {student.get('name', student.get('id', 'N/A'))}"):
                col1, col2, col3 = st.columns([3, 1, 1])
                
                with col1:
                    if 'name' in student:
                        st.write(f'**Name:** {student['name']}')
                    if 'email' in student:
                        st.write(f'**Email:** {student['email']}')
                    if 'course_id' in student:
                        related_name = course_options.get(student['course_id'], f'ID: {student['course_id']}')
                        st.write(f'**Course:** {related_name}')
                
                with col2:
                    if st.button("Edit", key=f"edit_{student['id']}"):
                        st.session_state.edit_student_id = student['id']
                        st.session_state.edit_student_data = student
                        st.rerun()
                
                with col3:
                    if st.button("Delete", key=f"delete_{student['id']}"):
                        if delete_student(student['id']):
                            st.rerun()
    else:
        st.info("No students found.")

def show_student_form():
    """Display form to add new Student."""
    st.header("Add New Student")
    
    with st.form("add_student_form"):
        name = st.text_input("Name", key="name_input")
        email = st.text_input("Email", key="email_input")
        # Foreign key: course
        try:
            course_resp = requests.get(f'{API_BASE_URL}/api/courses/')
            course_resp.raise_for_status()
            course_data = course_resp.json()
            course_options = {item['id']: item.get('name', str(item['id'])) for item in course_data}
        except (requests.exceptions.RequestException, json.JSONDecodeError):
            course_options = {}
            st.error('Failed to load course options')
        course_id = st.selectbox("Course", options=list(course_options.keys()), format_func=lambda o: course_options.get(o, str(o)))

        
        submitted = st.form_submit_button("Add Student")
        
        if submitted:
            if not name:
                st.error("Name is required")
                return
            if not email:
                st.error("Email is required")
                return
            if not course_id:
                st.error("Course_Id is required")
                return
            
            # Create data dictionary
            data = {"name": name, "email": email, "course_id": course_id}
            
            if create_student(data):
                st.rerun()

def show_student_edit():
    """Display form to edit existing Student."""
    st.header("Edit Student")
    
    if f"edit_student_id" in st.session_state:
        edit_data = st.session_state.get(f"edit_student_data", {})
        
        with st.form("edit_student_form"):
            st.write(f"Editing Student ID: {st.session_state.edit_student_id}")
            
            st.write(f"**ID:** {st.session_state.edit_student_id}")
            name_edit = st.text_input("Name", value=edit_data.get("name", ""), key="name_edit")
            email_edit = st.text_input("Email", value=edit_data.get("email", ""), key="email_edit")
            # Foreign key: course
            try:
                course_resp = requests.get(f"{API_BASE_URL}/api/courses/")
                course_resp.raise_for_status()
                course_data = course_resp.json()
                course_options = {}
                for item in course_data:
                    course_options[item['id']] = item.get('name', str(item['id']))
            except requests.exceptions.RequestException:
                course_options = {}
                st.error("Failed to load course options")
            course_id_edit = st.selectbox("Course", options=list(course_options.keys()), index=0 if edit_data.get("course_id") is None else list(course_options.keys()).index(edit_data.get("course_id")), format_func=lambda o: course_options.get(o, str(o)))
            
            submitted = st.form_submit_button("Update Student")
            
            if submitted:
                if not name_edit:
                    st.error("Name is required")
                    return
                if not email_edit:
                    st.error("Email is required")
                    return
                if not course_id_edit:
                    st.error("Course Id is required")
                    return
                
                # Create data dictionary
                data = {"name": name_edit, "email": email_edit, "course_id": course_id_edit}
                
                if update_student(st.session_state.edit_student_id, data):
                    # Clear edit state
                    if f"edit_student_id" in st.session_state:
                        del st.session_state[f"edit_student_id"]
                    if f"edit_student_data" in st.session_state:
                        del st.session_state[f"edit_student_data"]
                    st.rerun()
        
        if st.button("Cancel Edit"):
            if f"edit_student_id" in st.session_state:
                del st.session_state[f"edit_student_id"]
            if f"edit_student_data" in st.session_state:
                del st.session_state[f"edit_student_data"]
            st.rerun()
    else:
        st.info("Select a student from the list to edit.")

if __name__ == "__main__":
    main()