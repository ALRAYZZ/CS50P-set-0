def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    percent = percent/100
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")
    
    
    
def dollars_to_float(d):
    fixed = d.replace("$", "")
    return float(fixed)
    
    
    
    
def percent_to_float(p):
    fixed = p.replace("%", "")
    return float(fixed)
    
    
main()