import streamlit as st

st.title('GBMS Bank Mumbai,India')
options=st.sidebar.selectbox('Choose Type of Loan',('Personal Loan','Credit Card','Business Loan','Home Loan','Two Wheeler Loan','Car Loan'))
st.write("Welcome to GBMS Bank")
st.info('Loan Calculator')
st.selectbox('Employment Status',('Salaried','Self Employed'))
st.selectbox('Annual Income',('<250000','251000-500000','500000-750000','751000-1000000','>1000000'))
st.selectbox('Residence Status',('Own','Rented'))

p = int(st.text_input("How much loan do you need", 1))

if p > 500000:
    st.error('Maximum Eligible amount is 500000')
elif p >1 and p<= 500000:
    st.success('OK')
    t = int(st.text_input("In how many years do you want to pay", 1))
    if t > 5:
        st.error('Please enter tenure less than or equal to 5 years')
    elif t > 1 and t <= 5:
        r = 0.18
        st.write('Our rate of interest is', r * 100, '%')
        si = (p * t * r)
        emi = (si + p) / (t * 12)
        st.write('Interest to be paid', si)
        st.write('EMI to be paid per month', emi)
        st.warning('EMI must be paid in time')
        st.markdown(":rage:")
        apply=st.button('Apply')
        if apply==1:
            r=st.write('Required Documents')
            s=st.checkbox('Salary Slip',1)
            b=st.checkbox('Bank Statements',1)
            i=st.checkbox('ITR',1)
            a=st.checkbox('Address Proof',1)
            ad=st.checkbox('Aadhar Card',1)
            p=st.checkbox('PAN card',1)
            st.write('Our Bank Representative will get in touch with you shortly!')
            st.write('Thank You for visiting GBMS Bank!')




