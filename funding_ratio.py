######################################################################################################

import pandas as pd
import numpy as np

######################################################################################################

def funding_ratio(assets, liabilities, rate_interest):
    """
    Computes the funding ratio of a series of liabilities:

    1- The ratio is based on an interest rate and current value of assets.

    2- Use "discount" function to compute the the price of a pure discount
       bond that pays a dollar at time date.

    3- Use "present_value" function to the price of a pure discount bond that
       pays a dollar at time date.
    """
    
######################################################################################################   
    
    def discount(dates, rate_interest):
        """
        Compute the price of a pure discount bond that pays a dollar at time date:

        1- "t" as time is in years.
        
        """
        return (1 + rate_interest) ** (-dates)

    
    def present_value(liabilities, rate_interest):
        """
        the price of a pure discount bond that pays a dollar at time date:

        1- Make the liabilities series by pandas.
        """
        dates = liabilities.index
        discounts = discount(dates, rate_interest)
        return (discounts * liabilities).sum()
    
######################################################################################################
    
    return assets / present_value(liabilities, rate_interest)