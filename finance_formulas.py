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




# In[1]:


def holding_period_return(initial_price, final_price, dividends):
    """
    Calculate the holding period return (HPR) of a stock.

    Args:
        initial_price (float): Initial price of the stock.
        final_price (float): Final price of the stock.
        dividends (float): Total dividends received during the holding period.

    Returns:
        float: Holding period return (HPR).
    """
    hpr = (final_price - initial_price + dividends) / initial_price
    return hpr



def time_weighted_rate_of_return(sub_period_returns):
    import math
    """
    Calculate the Time Weighted Rate of Return (TWRR).

    Args:
        sub_period_returns (list): List of sub-period returns.

    Returns:
        float: Time Weighted Rate of Return (TWRR).
    """
    placeholder = 1
    for i in sub_period_returns:
        placeholder *= math.sqrt(1+i)
        
    twrr = placeholder - 1
    return twrr
    


def bank_discount_yield(cost, face_value, days_to_maturity):
    """
    Calculate the Bank Discount Yield (BDY).

    Args:
        discount (float): Discount amount.
        face_value (float): Face value of the instrument.
        days_to_maturity (int): Number of days to maturity.

    Returns:
        float: Bank Discount Yield (BDY).
    """
    bdy = ((face_value - cost) / face_value) * (360 / days_to_maturity)
    return bdy


def holding_period_yield(initial_investment, final_investment, income):
    """
    Calculate the Holding Period Yield (HPY).

    Args:
        initial_investment (float): Initial investment amount.
        final_investment (float): Final investment amount.
        income (float): Total income earned during the holding period.

    Returns:
        float: Holding Period Yield (HPY).
    """
    hpy = (final_investment + income - initial_investment) / initial_investment
    return hpy


def effective_annual_yield(initial_investment, final_investment, income, days_to_maturity):
    """
    Calculate the Effective Annual Yield (EAY).

    Args:
        nominal_rate (float): Nominal interest rate.
        compounding_frequency (int): Number of times interest is compounded per year.

    Returns:
        float: Effective Annual Yield (EAY).
    """
    eay = (1 + ((final_investment + income - initial_investment) / initial_investment)) ** (365/days_to_maturity) - 1
    return eay


def money_market_yield(initial_investment, final_investment,  days_to_maturity, income=0):
    """
    Calculate the Money Market Yield (MMY).

    Args:
        discount (float): Discount amount.
        face_value (float): Face value of the instrument.
        days_to_maturity (int): Number of days to maturity.

    Returns:
        float: Money Market Yield (MMY).
    """
    mmy = (final_investment + income - initial_investment) / initial_investment * (360 / days_to_maturity)
    return mmy


def bond_equivalent_yield(rate_given, compounding_frequency):
    """
    Convert a given discount rate to a semi-annual discount rate.

    Args:
        rate_given (float): Original discount rate.
        compounding_frequency (int): Number of times compounding occurs per year.

    Returns:
        float: Semi-annual discount rate.
    """
    semi_annual_rate = ((1 + rate_given)**(compounding_frequency/2) - 1) * 2
    return semi_annual_rate 