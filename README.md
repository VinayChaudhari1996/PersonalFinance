# 💰 Investment Goal Calculator using Streamlit 💰

## 📄 Overview
This Streamlit-based project helps users calculate the **time required** to reach a financial goal based on regular contributions and compounding interest. By inputting the current investment value, annual compounding rate, annual contribution, and target amount, the app estimates the number of years it will take to reach the target using a **binary search method**.

### ✨ Features
- Calculate the time required to reach a target amount with regular investments.
- Visualize the investment growth over time with an interactive **Altair chart**.
- **LaTeX support** for displaying the future value formula and relevant parameters.
- Insights on how **compounding** works and **investment tips** to help users make informed decisions.

---

## 🛠️ How It Works

![image](https://github.com/user-attachments/assets/bef4019a-57e2-446b-b4b6-5504c15639ca)


---

## 🔍 Code Breakdown

### 🧠 Function to Calculate Time to Goal
The key function `calculate_time_to_goal` performs a **binary search** to find the number of years required to reach the target investment value:
```python
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
```

### 🌐 Streamlit UI
The Streamlit user interface captures the required inputs:
- **Current Investment Value** (₹)
- **Annual Compounding Rate** (%)
- **Annual Contribution** (₹)
- **Target Amount** (₹)

When the user clicks the **"Calculate"** button, the app runs the `calculate_time_to_goal` function and displays the result, including:
- **Time to reach the target** (in years).
- The LaTeX formula with actual values plugged in.
- An **interactive Altair chart** showing the growth of the investment over time.

---

## 🚀 How to Run

1. **Clone the Repo**:
   ```bash
   git clone https://github.com/your-repo/investment-goal-calculator.git
   cd investment-goal-calculator
   ```

2. **Install Dependencies**:
   Make sure you have the required libraries installed:
   ```bash
   pip install streamlit pandas numpy altair
   ```

3. **Run the Streamlit App**:
   ```bash
   streamlit run app.py
   ```

---

## 💻 Example Output

1. The user inputs their current investment value, compounding rate, annual contribution, and target amount.
2. The app calculates how many years it will take to reach the target.
3. The app displays a **LaTeX equation** showing the future value formula with real values.
4. An **interactive chart** is generated, allowing the user to visualize their investment growth over time.

---

## 📊 Visualization
The app uses **Altair** to create an area chart that represents the investment value growth over time.

```python
# Generate chart data
years = np.arange(0, np.ceil(result) + 1)
values = [current_value * (1 + annual_rate / 100) ** year + 
          annual_contribution * ((1 + annual_rate / 100) ** year - 1) / (annual_rate / 100) 
          for year in years]

chart_data = pd.DataFrame({
    "Year": years,
    "Investment Value (₹)": values
})

# Plot area chart using Altair
chart = alt.Chart(chart_data).mark_area(
    line={'color':'#8884d8'},
    color=alt.Gradient(
        gradient='linear',
        stops=[alt.GradientStop(color='#8884d8', offset=0), 
               alt.GradientStop(color='#ffffff', offset=1)],
        x1=1, x2=1, y1=1, y2=0
    )
).encode(
    x=alt.X('Year:Q', title='Year'),
    y=alt.Y('Investment Value (₹):Q', title='Investment Value (₹)', axis=alt.Axis(format='₹')),
    tooltip=['Year', 'Investment Value (₹)']
).interactive()

st.altair_chart(chart, use_container_width=True)
```

---

## 📈 Insights and Tips

### 💡 How Compounding Works
The app provides an explanation of **compound interest** and how it accelerates investment growth.

### 📖 Investment Tips
The app also offers some useful tips for maximizing returns:
- Start early to benefit from compounding.
- Diversify to reduce risk.
- Regularly rebalance your portfolio.
