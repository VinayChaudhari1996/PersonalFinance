import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Function to calculate the time required to reach the target
def calculate_time_to_goal(current_value, annual_rate, annual_contribution, target_amount):
    P = float(current_value)
    r = float(annual_rate) / 100
    PMT = float(annual_contribution)
    A = float(target_amount)
    
    def future_value(t):
        return P * (1 + r)**t + PMT * ((1 + r)**t - 1) / r - A
    
    low, high = 0, 100
    while high - low > 0.01:
        mid = (low + high) / 2
        if future_value(mid) < 0:
            low = mid
        else:
            high = mid
    return mid

# Streamlit UI
st.title("Investment Goal Calculator")
st.write("Calculate the time needed to reach your financial goals with regular investments.")

# Input fields
current_value = st.number_input("Current Investment Value (₹)", min_value=0.0, value=0.0, step=0.01, format="%.2f")
annual_rate = st.number_input("Annual Compounding Rate (%)", min_value=0.0, value=0.0, step=0.01, format="%.2f")
annual_contribution = st.number_input("Annual Contribution (₹)", min_value=0.0, value=0.0, step=0.01, format="%.2f")
target_amount = st.number_input("Target Amount (₹)", min_value=0.0, value=0.0, step=0.01, format="%.2f")

# Button to trigger the calculation
if st.button("Calculate"):
    result = calculate_time_to_goal(current_value, annual_rate, annual_contribution, target_amount)
    st.success(f"Time required to reach ₹{target_amount:,.2f}: {result:.2f} years")

    # LaTeX formula and actual values
    st.latex(r'''
        \text{Future Value:} \quad A = P \left(1 + \frac{r}{100}\right)^t + PMT \left[\frac{\left(1 + \frac{r}{100}\right)^t - 1}{\frac{r}{100}}\right]
    ''')
    st.latex(f'''
        A = {current_value} \left(1 + \frac{{{annual_rate}}}{{100}}\right)^t + {annual_contribution} \left[\frac{{\left(1 + \frac{{annual_rate}}}{{100}}\right)^t - 1}}{{\frac{{{annual_rate}}}{{100}}}}\right]
    ''')
    st.latex(r'''
        \text{Time to reach target:} \quad t = \text{solved using binary search}
    ''')

    # LaTeX explanation of parameters
    st.markdown(r'''
        **Parameters:**
        - \( A \) : Target amount to be reached
        - \( P \) : Current investment value
        - \( r \) : Annual compounding rate
        - \( PMT \) : Annual contribution
        - \( t \) : Time in years required to reach the target amount
    ''')

    # Generate chart data
    years = np.arange(0, np.ceil(result) + 1)
    values = [current_value * (1 + annual_rate / 100) ** year + annual_contribution * ((1 + annual_rate / 100) ** year - 1) / (annual_rate / 100) for year in years]
    
    chart_data = pd.DataFrame({
        "Year": years,
        "Investment Value (₹)": values
    })

    # Plot area chart using Altair
    chart = alt.Chart(chart_data).mark_area(
        line={'color':'#8884d8'},
        color=alt.Gradient(
            gradient='linear',
            stops=[alt.GradientStop(color='#8884d8', offset=0), alt.GradientStop(color='#ffffff', offset=1)],
            x1=1,
            x2=1,
            y1=1,
            y2=0
        )
    ).encode(
        x=alt.X('Year:Q', title='Year'),
        y=alt.Y('Investment Value (₹):Q', title='Investment Value (₹)', axis=alt.Axis(format='₹')),
        tooltip=['Year', 'Investment Value (₹)']
    ).interactive()

    st.altair_chart(chart, use_container_width=True)

# Information section
st.header("How Compounding Works")
st.write("""
    Compounding is the process where the value of an investment increases because the earnings on an investment, 
    both capital gains and interest, earn interest as time passes. This growth, calculated on the initial principal 
    and the accumulated earnings of prior periods, is the basis of how investments grow over time.
""")

st.header("Investment Tips")
st.write("""
    - Start investing early to take advantage of compound interest.
    - Diversify your portfolio to spread risk.
    - Regularly review and rebalance your investments.
    - Consider seeking professional financial advice for personalized strategies.
""")

st.footer("© 2024 Investment Goal Calculator. All rights reserved.")
