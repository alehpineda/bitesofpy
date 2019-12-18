def get_profile(name, age, *sports, **awards):
    if not isinstance(age, int):
        raise ValueError('Age not a number')
    if len(sports) > 5:
        raise ValueError('At least 5 sports')
    if not sports and not awards:
        return {'name': name, 'age': age}
    elif not sports and awards:
        return {'name': name, 'age': age, 'awards': {**awards}}
    elif sports and not awards:
        return {'name': name, 'age': age, 'sports': sorted([*sports])}
    else:
        return {'name':name, 'age':age, 'sports':sorted([*sports]), 'awards': {**awards}}