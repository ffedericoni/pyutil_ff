from sklearn.model_selection import ParameterGrid
from sklearn.linear_model import SGDRegressor
#
# Is this like func:`sklearn.model_selection.fit_grid_point`  ?
#
params = {
    'alpha': [0.1, 0.5, 1.0, 3.0],
    'eta0': [0.01, 0.02, 0.05],
    'power_t': [0.25, 0.5, 0.75],
    'max_iter': [400],
    'learning_rate': ['invscaling']
}

def test_params_model(params, estimator, X, y, lower_is_better=True):
    '''
    Exhaustive search of the parameters for a given Model.
    
    Parameters
    ----------
    params : dict of string to sequence 
             (see also param_grid parameter for ParameterGrid)
    estimator  : estimator to be fit and evaluated
    X      : Train Data
    y      : Label Data
    lower_is_better : if lower scores are better scores 
                      (default True)
    '''
    
    if lower_is_better: 
        score = 1e9
    else:
        score = -1e9
        
    for param in ParameterGrid(params):
        model = estimator(**param)
    #    %timeit -n1 -r1 
        model.fit(X, y)
        preds = model.predict(X)
        this_score = rmsle(y_true,np.expm1(preds))
        if this_score < score:
            score = this_score
            print(score, param)
