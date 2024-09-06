import streamlit as st
st.title('Data Science Course')
st.write('Welcome!!')
op1=st.radio('Did you learn Python?',options=['Yes','No'])
if op1=='Yes':
    op2=st.radio('Did you practice',options=['Yes','No'])
    if op2 == 'No':
        st.write('Please Practice well and come again')
    elif op2=='Yes':
        st.write('You can learn next topic')
elif op1=='No':
    st.write('Please Learn python')








