import streamlit as st

# Tạo danh sách người dùng mẫu
USER_CREDENTIALS = {
    "admin": "admin123",
    "user1": "password1",
    "user2": "password2"
}

# Hàm kiểm tra đăng nhập
def check_login(username, password):
    return USER_CREDENTIALS.get(username) == password

# Giao diện đăng nhập
def login():
    st.title("My Streamlit App")
    st.subheader("Log In")

    # Nhập thông tin
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Log in")

    # Kiểm tra đăng nhập
    if login_button:
        if check_login(username, password):
            st.success(f"Hello , {username}!")
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
        else:
            st.error("Tên đăng nhập hoặc mật khẩu không đúng!")

# Giao diện sau khi đăng nhập
def app_content():
    st.title("Nội Dung Chính")
    st.write(f"Chào mừng bạn, {st.session_state['username']}!")
    if st.button("Đăng xuất"):
        st.session_state['logged_in'] = False

# Xử lý trạng thái ứng dụng
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if st.session_state['logged_in']:
    app_content()
else:
    login()
