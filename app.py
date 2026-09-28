import streamlit as st

from inference.predict_freight import predict_freight_cost
from inference.predict_invoice_flag import predict_invoice_flag


# ================================================================
# PAGE CONFIGURATION
# ================================================================

st.set_page_config(
    page_title="Vendor Invoice Intelligence",
    page_icon="🧾",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ================================================================
# CUSTOM STYLING
# ================================================================

st.markdown("""
<style>

    /* Main page */
    .main {
        padding-top: 1rem;
    }

    /* Hero section */
    .hero {
        padding: 2rem 2.5rem;
        border-radius: 16px;
        margin-bottom: 1.5rem;
        border: 1px solid rgba(128,128,128,0.2);
    }

    .hero-title {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.3rem;
    }

    .hero-subtitle {
        font-size: 1.15rem;
        opacity: 0.75;
        margin-bottom: 1rem;
    }

    .hero-description {
        font-size: 1rem;
        line-height: 1.7;
        opacity: 0.85;
    }

    /* Section cards */
    .section-card {
        padding: 1.3rem 1.5rem;
        border-radius: 12px;
        border: 1px solid rgba(128,128,128,0.2);
        margin-bottom: 1.2rem;
    }

    /* Business impact cards */
    .impact-card {
        padding: 1.2rem;
        border-radius: 12px;
        border: 1px solid rgba(128,128,128,0.2);
        text-align: center;
        min-height: 130px;
    }

    .impact-title {
        font-weight: 600;
        font-size: 1rem;
    }

    .impact-text {
        font-size: 0.85rem;
        opacity: 0.7;
        margin-top: 0.4rem;
    }

    /* Small labels */
    .module-label {
        font-size: 0.8rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
        opacity: 0.65;
    }

    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem 0 1rem 0;
        opacity: 0.55;
        font-size: 0.8rem;
    }

</style>
""", unsafe_allow_html=True)


# ================================================================
# HERO / HEADER
# ================================================================

st.markdown("""
<div class="module-label">
    AI-POWERED FINANCE ANALYTICS
</div>

<div class="hero-title">
    🧾 Vendor Invoice Intelligence
</div>

<div class="hero-subtitle">
    Machine Learning for Freight Forecasting & Invoice Risk Detection
</div>

<div class="hero-description">
    Transform vendor invoice data into actionable financial insights.
    Predict expected freight costs and identify invoices that require
    additional review using machine learning models.
</div>
""", unsafe_allow_html=True)

# ================================================================
# BUSINESS IMPACT
# ================================================================

st.markdown("### 📊 Business Intelligence Overview")

impact_col1, impact_col2, impact_col3 = st.columns(3)

with impact_col1:
    st.markdown("""
    <div class="impact-card">
        <div style="font-size: 2rem;">📈</div>
        <div class="impact-title">Cost Forecasting</div>
        <div class="impact-text">
            Estimate expected freight costs before invoice processing.
        </div>
    </div>
    """, unsafe_allow_html=True)


with impact_col2:
    st.markdown("""
    <div class="impact-card">
        <div style="font-size: 2rem;">🛡️</div>
        <div class="impact-title">Risk Detection</div>
        <div class="impact-text">
            Identify potentially abnormal invoices requiring review.
        </div>
    </div>
    """, unsafe_allow_html=True)


with impact_col3:
    st.markdown("""
    <div class="impact-card">
        <div style="font-size: 2rem;">⚡</div>
        <div class="impact-title">Faster Decisions</div>
        <div class="impact-text">
            Support finance teams with automated ML-based predictions.
        </div>
    </div>
    """, unsafe_allow_html=True)


st.divider()


# ================================================================
# SIDEBAR
# ================================================================

st.sidebar.markdown("""
# 🧾 Invoice AI
### Intelligence Portal
""")

st.sidebar.divider()

st.sidebar.markdown("### 🔍 Prediction Module")

selected_model = st.sidebar.radio(
    "Select an analysis",
    [
        "Freight Cost Prediction",
        "Invoice Manual Approval Flag"
    ]
)

st.sidebar.divider()

st.sidebar.markdown("""
### ⚙️ System

**Models:** Machine Learning  
**Data:** Vendor Invoice Records  
**Platform:** Streamlit  

---

### 📌 Purpose

This portal provides automated predictions to assist financial analysis and invoice review.
""")

st.sidebar.caption(
    "Vendor Invoice Intelligence • ML Analytics"
)


# ================================================================
# FREIGHT COST PREDICTION
# ================================================================

if selected_model == "Freight Cost Prediction":

    st.markdown("""
    <div class="section-card">

    <div class="module-label">
        PREDICTION MODULE 01
    </div>

    <h2>📦 Freight Cost Prediction</h2>

    <p>
    Estimate the expected freight cost of a vendor invoice using
    invoice value.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📝 Invoice Information")

    with st.form("freight_form"):

        col1, col2 = st.columns(2)

        with col1:

            quantity = st.number_input(
                "📦 Invoice Quantity",
                min_value=1,
                value=1200,
                step=1
            )

        with col2:

            dollars = st.number_input(
                "💰 Invoice Value ($)",
                min_value=1.0,
                value=18500.0,
                step=100.0
            )

        submit_freight = st.form_submit_button(
            "🔮 Predict Freight Cost",
            use_container_width=True
        )

    if submit_freight:

        input_data = {
            "Dollars": [dollars]
        }

        prediction = predict_freight_cost(
            input_data
        )["predicted_Freight"]

        predicted_freight = prediction[0]

        st.divider()

        st.success(
            "Freight prediction completed successfully."
        )

        result_col1, result_col2, result_col3 = st.columns(3)

        with result_col1:

            st.metric(
                "📦 Quantity",
                f"{quantity:,}"
            )

        with result_col2:

            st.metric(
                "💰 Invoice Value",
                f"${dollars:,.2f}"
            )

        with result_col3:

            st.metric(
                "🚚 Estimated Freight",
                f"${predicted_freight:,.2f}"
            )


# ================================================================
# INVOICE FLAG PREDICTION
# ================================================================

else:

    st.markdown("""
    <div class="section-card">

    <div class="module-label">
        PREDICTION MODULE 02
    </div>

    <h2>🚩 Invoice Risk Assessment</h2>

    <p>
    Evaluate vendor invoice characteristics and predict whether
    an invoice should be sent for manual approval.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📝 Invoice Information")

    with st.form("invoice_flag_form"):

        col1, col2, col3 = st.columns(3)

        with col1:

            invoice_quantity = st.number_input(
                "📦 Invoice Quantity",
                min_value=1,
                value=50,
                step=1
            )

            freight = st.number_input(
                "🚚 Freight Cost",
                min_value=0.0,
                value=1.73,
                step=0.01
            )

        with col2:

            invoice_dollars = st.number_input(
                "💰 Invoice Dollars",
                min_value=1.0,
                value=352.95,
                step=10.0
            )

            total_item_quantity = st.number_input(
                "📊 Total Item Quantity",
                min_value=1,
                value=162,
                step=1
            )

        with col3:

            total_item_dollars = st.number_input(
                "💵 Total Item Dollars",
                min_value=1.0,
                value=2476.0,
                step=10.0
            )

        submit_flag = st.form_submit_button(
            "🚨 Evaluate Invoice Risk",
            use_container_width=True
        )

    if submit_flag:

        input_data = {
            "invoice_quantity": [invoice_quantity],
            "invoice_dollars": [invoice_dollars],
            "Freight": [freight],
            "total_item_quantity": [total_item_quantity],
            "total_item_dollars": [total_item_dollars]
        }

        flag_prediction = predict_invoice_flag(
            input_data
        )["Predicted_Flag"]

        is_flagged = bool(flag_prediction[0])

        st.divider()

        if is_flagged:

            st.error(
                "🚩 **MANUAL APPROVAL REQUIRED**\n\n"
                "The machine learning model has identified this "
                "invoice as requiring additional review."
            )

            st.warning(
                "Please verify the invoice details before approval."
            )

        else:

            st.success(
                "✅ **NO MANUAL-REVIEW FLAG DETECTED**\n\n"
                "The machine learning model did not flag this "
                "invoice for additional review."
            )

            st.info(
                "This prediction is a machine-learning screening result "
                "and should be considered alongside normal invoice checks."
            )


# ================================================================
# FOOTER
# ================================================================

st.divider()

st.markdown("""
<div class="footer">

🧾 <b>Vendor Invoice Intelligence Portal</b><br>

Machine Learning • Data Analytics • Financial Intelligence

</div>
""", unsafe_allow_html=True)