import os
import json
import streamlit as st
import requests
from typing import List, Dict, Any, Optional

# API Configuration
API_PORT = os.getenv("REALWORLD_FASTAPI_PORT", "8000")
API_BASE_URL = f"http://localhost:{API_PORT}"

def create_course(data: Dict[str, Any]) -> bool:
    """Create a new Course."""
    try:
        response = requests.post(f"{API_BASE_URL}/api/courses/", json=data)
        response.raise_for_status()
        if response.status_code == 201:
            st.success(f"Course created successfully!")
            return True
        return False
    except requests.exceptions.RequestException as e:
        st.error(f"Error creating course: {e}")
        return False

def get_courses() -> List[Dict[str, Any]]:
    """Get all Courses."""
    try:
        response = requests.get(f"{API_BASE_URL}/api/courses/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching courses: {e}")
        return []

def update_course(id: int, data: Dict[str, Any]) -> bool:
    """Update an existing Course."""
    try:
        response = requests.put(f"{API_BASE_URL}/api/courses/{id}", json=data)
        response.raise_for_status()
        if response.status_code == 200:
            st.success(f"Course updated successfully!")
            return True
        return False
    except requests.exceptions.RequestException as e:
        st.error(f"Error updating course: {e}")
        return False

def delete_course(id: int) -> bool:
    """Delete a Course."""
    try:
        response = requests.delete(f"{API_BASE_URL}/api/courses/{id}")
        response.raise_for_status()
        if response.status_code == 204:
            st.success(f"Course deleted successfully!")
            return True
        return False
    except requests.exceptions.RequestException as e:
        st.error(f"Error deleting course: {e}")
        return False

def main():
    """Main Course management interface."""
    st.title("Course Management")
    
    # Create tabs for different operations
    tab1, tab2, tab3 = st.tabs(["List Courses", "Add Course", "Edit Course"])
    
    with tab1:
        show_course_list()
    
    with tab2:
        show_course_form()
    
    with tab3:
        show_course_edit()

def show_course_list():
    """Display list of Courses."""
    st.header("All Courses")
    
    if st.button("Refresh", key="refresh_list"):
        st.rerun()
    
    
    
    courses = get_courses()
    
    if courses:
        for course in courses:
            with st.expander(f"Course: {course.get('name', course.get('id', 'N/A'))}"):
                col1, col2, col3 = st.columns([3, 1, 1])
                
                with col1:
                    if 'name' in course:
                        st.write(f'**Name:** {course['name']}')
                    if 'level' in course:
                        st.write(f'**Level:** {course['level']}')
                
                with col2:
                    if st.button("Edit", key=f"edit_{course['id']}"):
                        st.session_state.edit_course_id = course['id']
                        st.session_state.edit_course_data = course
                        st.rerun()
                
                with col3:
                    if st.button("Delete", key=f"delete_{course['id']}"):
                        if delete_course(course['id']):
                            st.rerun()
    else:
        st.info("No courses found.")

def show_course_form():
    """Display form to add new Course."""
    st.header("Add New Course")
    
    with st.form("add_course_form"):
        name = st.text_input("Name", key="name_input")
        level = st.text_input("Level", key="level_input")
        
        submitted = st.form_submit_button("Add Course")
        
        if submitted:
            if not name:
                st.error("Name is required")
                return
            if not level:
                st.error("Level is required")
                return
            
            # Create data dictionary
            data = {"name": name, "level": level}
            
            if create_course(data):
                st.rerun()

def show_course_edit():
    """Display form to edit existing Course."""
    st.header("Edit Course")
    
    if f"edit_course_id" in st.session_state:
        edit_data = st.session_state.get(f"edit_course_data", {})
        
        with st.form("edit_course_form"):
            st.write(f"Editing Course ID: {st.session_state.edit_course_id}")
            
            st.write(f"**ID:** {st.session_state.edit_course_id}")
            name_edit = st.text_input("Name", value=edit_data.get("name", ""), key="name_edit")
            level_edit = st.text_input("Level", value=edit_data.get("level", ""), key="level_edit")
            
            submitted = st.form_submit_button("Update Course")
            
            if submitted:
                if not name_edit:
                    st.error("Name is required")
                    return
                if not level_edit:
                    st.error("Level is required")
                    return
                
                # Create data dictionary
                data = {"name": name_edit, "level": level_edit}
                
                if update_course(st.session_state.edit_course_id, data):
                    # Clear edit state
                    if f"edit_course_id" in st.session_state:
                        del st.session_state[f"edit_course_id"]
                    if f"edit_course_data" in st.session_state:
                        del st.session_state[f"edit_course_data"]
                    st.rerun()
        
        if st.button("Cancel Edit"):
            if f"edit_course_id" in st.session_state:
                del st.session_state[f"edit_course_id"]
            if f"edit_course_data" in st.session_state:
                del st.session_state[f"edit_course_data"]
            st.rerun()
    else:
        st.info("Select a course from the list to edit.")

if __name__ == "__main__":
    main()