from metrics import accuracy

true_labels = [0, 1, 1, 0, 1]
pred_labels = [0, 1, 1, 1, 1]

acc = accuracy(pred_labels, true_labels)

print(f"Accuracy: {acc:.2f}")

