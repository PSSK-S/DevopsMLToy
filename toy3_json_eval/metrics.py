def accuracy(pred_labels, true_labels):
    correct = 0
    if len(pred_labels) != len(true_labels):
        raise ValueError("Mismath in prdicted vales and true values lengths.")
    for pred, true in zip(pred_labels, true_labels):
        if pred == true:
            correct += 1
    return correct / len(true_labels)        