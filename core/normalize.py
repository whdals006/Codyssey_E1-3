def normalize_label(label):
    label = label.lower()

    if label in ["+", "cross"]:
        return "Cross"
    elif label in ["x"]:
        return "X"

    return "UNKNOWN"