# Import libraries (additional module)
import numpy as np


def get_alpha_vec(B_alpha):
    """
    Create an alpha vecrtor
    Parameters
    ----------        
    B_alpha : patsy.design_info.DesignMatrix 
        Matrix of Alpha Factors
        
    Returns
    -------
    alpha_vec : patsy.design_info.DesignMatrix 
        alpha vecrtor
    """
    n = len(B_alpha)
    alpha_vec = np.zeros(n)
    window = 20
    daily_annualization_factor = np.sqrt(252)
    for i in np.arange(n):
        if i < window - 1:
            alpha_vec[i] = np.sum(B_alpha[i])
        else:
            sharpe_ratio = daily_annualization_factor*B_alpha[i-window+1:i+1].mean(axis=0)/B_alpha[i-window+1:i+1].std(axis=0)
            sharpe_ratio_pos = (sharpe_ratio>0)*sharpe_ratio
            sharpe_ratio_pos_sum = sharpe_ratio_pos.sum()
            alpha_vec[i] = sum(B_alpha[i]*((sharpe_ratio_pos/sharpe_ratio_pos_sum) if sharpe_ratio_pos_sum != 0 else 0))
    return alpha_vec * 1e-4
