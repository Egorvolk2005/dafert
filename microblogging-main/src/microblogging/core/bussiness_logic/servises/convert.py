def convert_form_data_to_dto(dto, data):
    obj = dto()
    for key in data:
        value = data[key]
        if hasattr(obj, key):      
            setattr(obj, key, value)
        else:         
            raise AttributeError(f"DTO class {dto.__name__} has no attribute {key}")
    return obj