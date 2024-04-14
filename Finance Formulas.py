#!/usr/bin/env python
# coding: utf-8

# # Finance Formulas

# ### Present Value (PV)

# In[9]:


def compounding_present_value(FV, r, n, compounding_frequency=1, payment_at_beginning=False):
    """
    Calculate the present value of a compounding investment.

    Args:
        FV (float): Future value of the investment.
        r (float): Interest rate per period.
        n (int): Number of periods.
        compounding_frequency (int, optional): Number of times interest is compounded per year. Defaults to 1.
        payment_at_beginning (bool, optional): True for payment at the beginning, False for payment at the end. 
        Defaults to False.

    Returns:
        float: Present value of the investment.
    """
    if payment_at_beginning:
        PV = FV / (1 + r/compounding_frequency)**n
    else:
        PV = FV / (1 + r/compounding_frequency)**n
    return PV


# ### Annuity Present Value

# In[3]:


def annuity_present_value(PMT, r, n, annuity_due=False):
    """
    Calculate the present value of an annuity.

    Args:
        PMT (float): Periodic payment (annuity).
        r (float): Interest rate per period.
        n (int): Number of periods.
        annuity_due (bool, optional): True for annuity due, False for ordinary annuity. Defaults to False.

    Returns:
        float: Present value of the annuity.
    """
    if annuity_due:
        PV = PMT * ((1 - (1 + r)**-n) / r) * (1 + r)
    else:
        PV = PMT * ((1 - (1 + r)**-n) / r)
    return PV


# ### Future Value (FV)

# In[12]:


def compounding_future_value(PV, r, n, compounding_frequency=1, payment_at_beginning=False):
    """
    Calculate the future value of a compounding investment.

    Args:
        PV (float): Present value of the investment.
        r (float): Interest rate per period.
        n (int): Number of periods.
        compounding_frequency (int, optional): Number of times interest is compounded per year. Defaults to 1.
        payment_at_beginning (bool, optional): True for payment at the beginning, False for payment at the end. 
        Defaults to Faalse.

    Returns:a
        float: Future value of the investment.
    """
    if payment_at_beginning:
        FV = PV * (1 + r/compounding_frequency)**n
    else:
        FV = PV * (1 + r/compounding_frequency)**n
    return FV


# ### Annuity Future Value

# In[11]:


def annuity_future_value(PMT, r, n, annuity_due=False):
    """
    Calculate the future value of an annuity.

    Args:
        PMT (float): Periodic payment (annuity).
        r (float): Interest rate per period.
        n (int): Number of periods.
        annuity_due (bool, optional): True for annuity due, False for ordinary annuity. Defaults to False.

    Returns:
        float: Future value of the annuity.
    """
    if annuity_due:
        FV = PMT * (((1 + r)**n - 1) / r) * (1 + r)
    else:
        FV = PMT * (((1 + r)**n - 1) / r)
    return FV


# ### Perpetuity

# In[18]:


def perpetuity_present_value(PMT, r):
    """
    Calculate the present value of a perpetuity.

    Args:
        PMT (float): Periodic payment (perpetuity).
        r (float): Discount rate.

    Returns:
        float: Present value of the perpetuity.
    """
    PV = PMT / r
    return PV


# ### Uneven Cash Flows PV

# In[19]:


def npv_uneven_cash_flows(rate, cash_flows):
    """
    Calculate the Net Present Value (NPV) of uneven cash flows.

    Args:
        rate (float): Discount rate per period.
        cash_flows (list): List of cash flows where each element represents the cash flow in a specific period.

    Returns:
        float: Net Present Value (NPV) of the cash flows.
    """
    npv = sum([cf / (1 + rate)**n for n, cf in enumerate(cash_flows)])
    return npv


# ### Uneven Cash Flows FV

# In[23]:


def future_value_uneven_cash_flows(rate, cash_flows):
    """
    Calculate the future value (FV) of uneven cash flows.

    Args:
        rate (float): Interest rate per period.
        cash_flows (list): List of cash flows where each element represents the cash flow in a specific period.

    Returns:
        float: Future value of the cash flows.
    """
    fv = sum([cf * (1 + rate)**n for n, cf in enumerate(cash_flows)])
    return fv


# ## Annuity Payment PV

# In[2]:


def annuity_payment(PV, r, n, annuity_due=False):
    """
    Calculate the periodic payment of an annuity.

    Args:
        PV (float): Present value of the annuity.
        r (float): Interest rate per period.
        n (int): Number of periods.
        annuity_due (bool, optional): True for annuity due, False for ordinary annuity. Defaults to False.

    Returns:
        float: Periodic payment (PMT) of the annuity.
    """
    if annuity_due:
        PMT = PV * (r / (1 - (1 + r)**(-n))) / (1 + r)
    else:
        PMT = PV * (r / (1 - (1 + r)**(-n))) 
    return PMT


# ## Annuity Payment FV

# In[43]:


def annuity_payment_from_future_value(FV, r, n, annuity_due=False):
    """
    Calculate the periodic payment of an annuity given the future value.

    Args:
        FV (float): Future value of the annuity.
        r (float): Interest rate per period.
        n (int): Number of periods.
        annuity_due (bool, optional): True for annuity due, False for ordinary annuity. Defaults to False.

    Returns:
        float: Periodic payment (PMT) of the annuity.
    """
    if annuity_due:
        PMT = FV * r / ((1 + r) * ((1 + r)**n - 1))
    else:
        PMT = FV * r / ((1 + r)**n - 1)
    return PMT




# ## Compounding PV and FV
# 
# compounding_present_value(FV, r, n, compounding_frequency=1, payment_at_beginning=False)  
# 
# compounding_future_value(PV, r, n, compounding_frequency=1, payment_at_beginning=False)
# 
# ## Annuity PV and FV
# 
# annuity_present_value(PMT, r, n, annuity_due=False)
# 
# annuity_future_value(PMT, r, n, annuity_due=False)  
# 
# ## Perpetuity
# 
# perpetuity_present_value(PMT, r)
# 
# ## Uneven Cash Flows
# 
# npv_uneven_cash_flows(rate, cash_flows)  
# 
# future_value_uneven_cash_flows(rate, cash_flows)
# 
# ## Annuity Payment
# 
# annuity_payment(PV, r, n, annuity_due=False)
# 
# annuity_payment_from_future_value(FV, r, n, annuity_due=False)
# 


