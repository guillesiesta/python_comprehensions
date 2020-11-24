hydration_levels = {"arc1": 23, "arc2": 64, "arc3": 104}

def old_saturation_levels(data_dict):
    temp = {}
    for key,value in data_dict.items():
        temp[key] = (value**3)/(2**value)
    return temp

def saturation_levels(data_dict):
    return {k:v**3/2**v for k,v in data_dict.items()}

print(old_saturation_levels(hydration_levels))
print(saturation_levels(hydration_levels))
