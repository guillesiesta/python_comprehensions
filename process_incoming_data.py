def old_process_incoming_data(data_list):
    temp = []
    for datum in data_list:
        temp.append(datum//2*67 - 5)
    return temp

def process_incoming_data(data_list):
   return [datum//2*67 - 5 for datum in data_list]


if __name__ == "__main__":
    data_list = [0, 5, 10, 15]
    print(process_incoming_data(data_list) == old_process_incoming_data(data_list))
