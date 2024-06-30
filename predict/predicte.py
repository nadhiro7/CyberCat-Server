import torch

class_labels_Num = {
    'DDoS-UDP_Flood': 1,
    'DDoS-TCP_Flood': 2,
    'DDoS-ICMP_Flood': 3,
    'DDoS-ACK_Fragmentation': 4,
    'DDoS-UDP_Fragmentation': 5,
    'DDoS-HTTP_Flood': 6,
    'DDoS-SlowLoris': 7,
    'DDoS-ICMP_Fragmentation': 8,
    'DDoS-PSHACK_Flood': 9,
    'DDoS-SynonymousIP_Flood': 10,
    'DDoS-RSTFINFlood': 11,
    'DDoS-SYN_Flood': 12,

    'DoS-UDP_Flood': 13,
    'DoS-TCP_Flood': 14,
    'DoS-SYN_Flood': 15,
    'DoS-HTTP_Flood': 16,

    'DictionaryBruteForce': 17,

    'XSS': 18,
    'SqlInjection': 19,
    'BrowserHijacking': 20,
    'CommandInjection': 21,
    'Backdoor_Malware': 22,
    'Uploading_Attack': 23,

    'Recon-HostDiscovery': 24,
    'Recon-OSScan': 25,
    'Recon-PortScan': 26,
    'Recon-PingSweep': 27,
    'VulnerabilityScan': 28,

    'MITM-ArpSpoofing': 29,
    'DNS_Spoofing': 30,

    'Mirai-greeth_flood': 31,
    'Mirai-udpplain': 32,
    'Mirai-greip_flood': 33,

    'BenignTraffic': 0
}
class_category_num = {
    "Benign" :  0,
    "DDoS" :  1,
    "DoS" :  2,
    "Miria" :  3,
    "Spoofing" :  4,
    "Recon" :  5,
    "web Based" :  6,
    "Brute Force" :  7
}

class_lb = {
    "Benign" :  0,
    "Attack" :  1,
}

# Define a function for inference
def predict_34_class(input_data,model):
    # Convert input_data to tensor
    # Convert input_data to tensor
    input_tensor = torch.tensor(input_data).float()
    # Reverse the dictionary to map values to keys
    class_labels = {v: k for k, v in class_labels_Num.items()}
    # Perform inference
    with torch.no_grad():
        output = model(input_tensor)
        probabilities = torch.softmax(output, dim=1)  # Convert logits to probabilities
        _, predicted = torch.max(probabilities, 1)

    # Decode the predicted class
    # predicted_label = class_labels[predicted.item()]
    # print(f"Predicted Class: {predicted_label}")

    # Print probabilities for each class
    res_dict = {}
    for i, prob in enumerate(probabilities[0]):
        class_label = class_labels.get(i, f"Unknown ({i})")
        res_dict[class_label] = float(f"{prob.item():.4f}")
        # print(f"{class_label}: {prob.item():.4f}")
    return predicted.item(), res_dict

def predict_8_class(input_data,model):
    # Convert input_data to tensor
    input_tensor = torch.tensor(input_data).float()
    # Reverse the dictionary to map values to keys
    class_labels = {v: k for k, v in class_category_num.items()}
    # Perform inference
    with torch.no_grad():
        output = model(input_tensor)
        probabilities = torch.softmax(output, dim=1)  # Convert logits to probabilities
        _, predicted = torch.max(probabilities, 1)

    # Decode the predicted class
    predicted_label = class_labels[predicted.item()]
    # print(f"Predicted Class: {predicted_label}")

    # Print probabilities for each class
    res_dict = {}
    for i, prob in enumerate(probabilities[0]):
        class_label = class_labels.get(i, f"Unknown ({i})")
        res_dict[class_label] = float(f"{prob.item():.4f}")
        # print(f"{class_label}: {prob.item():.4f}")
    return predicted.item(), res_dict
def predict_2_class(input_data,model):
    input_tensor = torch.tensor(input_data).float()
    # Reverse the dictionary to map values to keys
    class_labels = {v: k for k, v in class_lb.items()}
    # Perform inference
    with torch.no_grad():
        output = model(input_tensor)
        probabilities = torch.softmax(output, dim=1)  # Convert logits to probabilities
        _, predicted = torch.max(probabilities, 1)

    # Decode the predicted class
    predicted_label = class_labels[predicted.item()]
    # print(f"Predicted Class: {predicted_label}")

    # Print probabilities for each class
    res_dict = {}
    for i, prob in enumerate(probabilities[0]):
        class_label = class_labels.get(i, f"Unknown ({i})")
        res_dict[class_label] = float(f"{prob.item():.4f}")
        # print(f"{class_label}: {prob.item():.4f}")
    return predicted.item(), res_dict
def get_name_of_attack_by_value(val):
    key_for_value = None
    for key, value in class_labels_Num.items():
        if value == val:
            key_for_value = key
            break
    return key_for_value
def get_name_of_category_by_value(val):
    key_for_value = None
    for key, value in class_labels_Num.items():
        if value == val:
            key_for_value = key
            break
    return key_for_value
def get_name_of_category_by_value(val):
    key_for_value = None
    for key, value in class_category_num.items():
        if value == val:
            key_for_value = key
            break
    return key_for_value
def get_is_attacke_by_value(val):
    key_for_value = None
    for key, value in class_lb.items():
        if value == val:
            key_for_value = key
            break
    return key_for_value
def predictPost(input_data,scaler,model,type_of_class):
    scaled_input_data = scaler.transform([input_data])
    if type_of_class == '34':
        prediction,prob = predict_34_class(scaled_input_data, model)
        return get_name_of_attack_by_value(prediction),prob
    elif type_of_class == '8':
        prediction,prob = predict_8_class(scaled_input_data, model)
        return get_name_of_category_by_value(prediction),prob
    else:
        prediction,prob = predict_2_class(scaled_input_data, model)
        return get_is_attacke_by_value(prediction),prob
