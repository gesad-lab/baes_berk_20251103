import os
import json
import streamlit as st
import requests
from typing import List, Dict, Any, Optional

# API Configuration
API_PORT = os.getenv("REALWORLD_FASTAPI_PORT", "8000")
API_BASE_URL = f"http://localhost:{API_PORT}"

def create_teacher(data: Dict[str, Any]) -> bool:
    """Create a new Teacher."""
    try:
        response = requests.post(f"{API_BASE_URL}/api/teachers/", json=data)
        response.raise_for_status()
        if response.status_code == 201:
            st.success(f"Teacher created successfully!")
            return True
        return False
    except requests.exceptions.RequestException as e:
        st.error(f"Error creating teacher: {e}")
        return False

def get_teachers() -> List[Dict[str, Any]]:
    """Get all Teachers."""
    try:
        response = requests.get(f"{API_BASE_URL}/api/teachers/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching teachers: {e}")
        return []

def update_teacher(id: int, data: Dict[str, Any]) -> bool:
    """Update an existing Teacher."""
    try:
        response = requests.put(f"{API_BASE_URL}/api/teachers/{id}", json=data)
        response.raise_for_status()
        if response.status_code == 200:
            st.success(f"Teacher updated successfully!")
            return True
        return False
    except requests.exceptions.RequestException as e:
        st.error(f"Error updating teacher: {e}")
        return False

def delete_teacher(id: int) -> bool:
    """Delete a Teacher."""
    try:
        response = requests.delete(f"{API_BASE_URL}/api/teachers/{id}")
        response.raise_for_status()
        if response.status_code == 204:
            st.success(f"Teacher deleted successfully!")
            return True
        return False
    except requests.exceptions.RequestException as e:
        st.error(f"Error deleting teacher: {e}")
        return False

def main():
    """Main Teacher management interface."""
    st.title("Teacher Management")
    
    # Create tabs for different operations
    tab1, tab2, tab3 = st.tabs(["List Teachers", "Add Teacher", "Edit Teacher"])
    
    with tab1:
        show_teacher_list()
    
    with tab2:
        show_teacher_form()
    
    with tab3:
        show_teacher_edit()

def show_teacher_list():
    """Display list of Teachers."""
    st.header("All Teachers")
    
    if st.button("Refresh", key="refresh_list"):
        st.rerun()
    
    
    
    teachers = get_teachers()
    
    if teachers:
        for teacher in teachers:
            with st.expander(f"Teacher: {teacher.get('name', teacher.get('id', 'N/A'))}"):
                col1, col2, col3 = st.columns([3, 1, 1])
                
                with col1:
                    if 'name' in teacher:
                        st.write(f'**Name:** {teacher['name']}')
                    if 'email' in teacher:
                        st.write(f'**Email:** {teacher['email']}')
                
                with col2:
                    if st.button("Edit", key=f"edit_{teacher['id']}"):
                        st.session_state.edit_teacher_id = teacher['id']
                        st.session_state.edit_teacher_data = teacher
                        st.rerun()
                
                with col3:
                    if st.button("Delete", key=f"delete_{teacher['id']}"):
                        if delete_teacher(teacher['id']):
                            st.rerun()
    else:
        st.info("No teachers found.")

def show_teacher_form():
    """Display form to add new Teacher."""
    st.header("Add New Teacher")
    
    with st.form("add_teacher_form"):
        name = st.text_input("Name", key="name_input")
        email = st.text_input("Email", key="email_input")
        
        submitted = st.form_submit_button("Add Teacher")
        
        if submitted:
            if not name:
                st.error("Name is required")
                return
            if not email:
                st.error("Email is required")
                return
            
            # Create data dictionary
            data = {"name": name, "email": email}
            
            if create_teacher(data):
                st.rerun()

def show_teacher_edit():
    """Display form to edit existing Teacher."""
    st.header("Edit Teacher")
    
    if f"edit_teacher_id" in st.session_state:
        edit_data = st.session_state.get(f"edit_teacher_data", {})
        
        with st.form("edit_teacher_form"):
            st.write(f"Editing Teacher ID: {st.session_state.edit_teacher_id}")
            
            st.write(f"**ID:** {st.session_state.edit_teacher_id}")
            name_edit = st.text_input("Name", value=edit_data.get("name", ""), key="name_edit")
            email_edit = st.text_input("Email", value=edit_data.get("email", ""), key="email_edit")
            
            submitted = st.form_submit_button("Update Teacher")
            
            if submitted:
                if not name_edit:
                    st.error("Name is required")
                    return
                if not email_edit:
                    st.error("Email is required")
                    return
                
                # Create data dictionary
                data = {"name": name_edit, "email": email_edit}
                
                if update_teacher(st.session_state.edit_teacher_id, data):
                    # Clear edit state
                    if f"edit_teacher_id" in st.session_state:
                        del st.session_state[f"edit_teacher_id"]
                    if f"edit_teacher_data" in st.session_state:
                        del st.session_state[f"edit_teacher_data"]
                    st.rerun()
        
        if st.button("Cancel Edit"):
            if f"edit_teacher_id" in st.session_state:
                del st.session_state[f"edit_teacher_id"]
            if f"edit_teacher_data" in st.session_state:
                del st.session_state[f"edit_teacher_data"]
            st.rerun()
    else:
        st.info("Select a teacher from the list to edit.")

if __name__ == "__main__":
    main()