import argparse


def transpile(model: str, model_type: str, output: str):
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str,
                        help="Path to model file")
    parser.add_argument("--model-type", type=str, default="xgboost", choices=["xgboost", "catboost"],
                        help="Model type to transpile: (Default: xgboost)")
    parser.add_argument("--output", type=str, default="aleo-smart-contracts",
                        help="Path to output folder for Aleo Smart-Contracts. (Default: aleo-smart-contracts)")
    # Create parser argument which will list all possible models
    parser.add_argument("--list-models", action="store_true")
    _args = parser.parse_args()

    if _args.list_models:
        print("List of all possible model type arguments:")
        print("- xgboost")
        print("- catboost")
        print("- linreg")
        exit(0)

    # os.makedirs(_args.output, exist_ok=True)

    # print(tree.to_code())
