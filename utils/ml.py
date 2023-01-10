def benchmark_model(model):
    """Take fitted model and perform benchmarking

    Args:
        model: Fitted model
    """
    best_model = model.best_estimator_
    best_params = model.best_params_