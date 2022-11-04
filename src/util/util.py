def allocate_to_experiment_group(identifier: int, num_groups: int = 2):
    if num_groups < 2 or num_groups > 26:
        raise ValueError("num_groups must be between 2 and 26")

    groups = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")[:num_groups]
    return groups[identifier % num_groups]
