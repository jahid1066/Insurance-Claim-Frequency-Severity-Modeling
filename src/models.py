import statsmodels.api as sm

def fit_poisson_glm(X, y, offset):
    X_const = sm.add_constant(X)
    model = sm.GLM(y, X_const, family=sm.families.Poisson(), offset=offset).fit()
    return model

def fit_gamma_glm(X, y):
    X_const = sm.add_constant(X)
    model = sm.GLM(y, X_const, family=sm.families.Gamma(sm.families.links.log())).fit()
    return model
