def accuracy(pred_labels, true_labels):
    """
    change History:
    - 2025-11-29: Initial creation
        compute the accuracy metric.
        accuracu = number of corret predictions / total number of predictions


    """
    if len(pred_labels) != len(true_labels):
        raise ValueError("Mismatch of predicted and true label lenghts.")
    
    correct = 0
    #ls = []
    for pred, true in zip(pred_labels, true_labels):
        
        #print(pred, true)
        if pred == true:
            correct += 1 
        
    return correct / len(true_labels)        