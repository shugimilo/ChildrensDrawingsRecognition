import os

data_path = r"C:\Users\Win11\PycharmProjects\pythonProject\data"
label_path = os.path.join(data_path, 'labels', 'train')

class_mapping = {
    1: 2,
    8: 10
}

def update_labels(label_path, class_mapping):
    for filename in os.listdir(label_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(label_path, filename)
            with open(file_path, 'r') as file:
                lines = file.readlines()

            updated_lines = []
            for line in lines:
                parts = line.strip().split()
                if len(parts) == 0:
                    continue
                label_idx = int(parts[0])
                if label_idx in class_mapping:
                    parts[0] = str(class_mapping[label_idx])
                updated_lines.append(" ".join(parts))
            with open(file_path, 'w') as file:
                file.write("\n".join(updated_lines) + "\n")

update_labels(label_path, class_mapping)

print("Labels updated successfully.")
