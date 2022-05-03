import streamlit as st

# from io import StringIO
import pandas as pd

accepted_domains = ["gmail.com"]

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    #  layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://www.extremelycoolapp.com/help",
        "Report a bug": "https://www.extremelycoolapp.com/bug",
        "About": "# This is a header. This is an *extremely* cool app!",
    },
)

st.image(
    "https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Monet_-_Impression%2C_Sunrise.jpg/400px-Monet_-_Impression%2C_Sunrise.jpg",
    caption="Impression, Sunrise - Claude Money, 1872",
    use_column_width="always",
)
st.title("Title")
st.write("Press submit to begin processing job")

# Declare a form and call methods directly on the returned object
form = st.form(key="my_form", clear_on_submit=True)

# Email Handler
email = form.text_input(label="Email")


# File Handler
uploaded_file = form.file_uploader(
    "Upload X files",
    type=["csv", "xlsx"],
    accept_multiple_files=False,
    help="Only one file may be uploaded at at time. Must be a CSV or Excel file.",
)


submit = form.form_submit_button(label="Submit")

if submit:
    if len(email) > 0:
        if "@" not in email or email.split("@")[1] not in accepted_domains:
            st.error("Invalid email or email domain")
        else:
            st.success(
                f"A confirmation will be sent to {email} once file has been successfully uploaded"
            )

            if uploaded_file is not None:
                # # To read file as bytes:
                # bytes_data = uploaded_file.getvalue()
                # st.write(bytes_data)

                # # To convert to a string based IO:
                # stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
                # st.write(stringio)

                # # To read file as string:
                # string_data = stringio.read()
                # st.write(string_data)

                # Can be used wherever a "file-like" object is accepted:
                dataframe = pd.read_csv(uploaded_file)
                st.write(dataframe)
