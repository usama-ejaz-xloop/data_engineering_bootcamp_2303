def evaluate_model(data_dir, training_data_version, test_data_version):
    X_test, y_test = utils.prepare_input(data_dir, "test" + test_data_version)
