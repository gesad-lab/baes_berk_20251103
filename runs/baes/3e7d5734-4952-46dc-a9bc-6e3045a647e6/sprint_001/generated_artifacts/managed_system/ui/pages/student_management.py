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
    
    
    
    students = get_students()
    
    if students:
        for student in students:
            with st.expander(f"Student: {student.get('name', student.get('id', 'N/A'))}"):
                col1, col2, col3 = st.columns([3, 1, 1])
                
                with col1:
                    if 'name' in student:
                        st.write(f'**Name:** {student['name']}')
                
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
        
        submitted = st.form_submit_button("Add Student")
        
        if submitted:
            if not name:
                st.error("Name is required")
                return
            
            # Create data dictionary
            data = {"name": name}
            
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
            
            submitted = st.form_submit_button("Update Student")
            
            if submitted:
                if not name_edit:
                    st.error("Name is required")
                    return
                
                # Create data dictionary
                data = {"name": name_edit}
                
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