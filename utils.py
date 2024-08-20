import yaml

def load_config(config_path: str) -> dict:
    """
    Load configuration from a YAML file.
    
    :param config_path: Path to the configuration file.
    :return: Dictionary containing configuration data.
    """
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    return config
