import streamlit as st

st.title('Loan Calculator')
st.write("Welcome to GBMS Bank")
st.selectbox('Employment Status',('Salaried','Self Employed'))
st.selectbox('Annual Income',('<250000','251000-500000','500000-750000','751000-1000000','>1000000'))
st.selectbox('Residence Status',('Own','Rented'))
p = int(st.text_input("How much loan do you need", 1))  # Default value to avoid error

if p > 500000:
    st.write('Maximum Eligible amount is 500000')
elif p <= 500000:
    t = int(st.text_input("In how many years do you want to pay", 1))  # Default value to avoid error
    if t > 5:
        st.write('Please enter tenure less than or equal to 5 years')
    elif t <= 5:
        r = 0.18
        st.write('Our rate of interest is', r * 100, '%')
        si = (p * t * r)
        emi = (si + p) / (t * 12)
        st.write('Interest to be paid', si)
        st.write('EMI to be paid per month', emi)




