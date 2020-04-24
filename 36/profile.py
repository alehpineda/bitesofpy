def get_profile(name, age, *sports, **awards):
    if not isinstance(age, int):
        raise ValueError("Age not a number")
    if len(sports) > 5:
        raise ValueError("At least 5 sports")

    profile = {"name": name, "age": age}

    if sports:
        profile["sports"] = sorted(sports)

    if awards:
        profile["awards"] = awards

    return profile
