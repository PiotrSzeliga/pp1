def f(arr):
    import re
    pattern = r"^[a-z0-9_]{4,12}$"
    x = []
    for i in arr:
        if 4 <= len(i) <= 12:
            x += re.findall(pattern, i)
    return len(x)
if __name__ == "__main__":
    print(f(["uek","water_7_x","anna.may","a_b_c_d_e_f"]))
