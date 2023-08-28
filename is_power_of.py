def is_power_of(number, base):
    print(f"calling...is_power_of({number},{base})")
    #Base case: when nubmer is smaller than base.
    if number < base:
        # If number is equal to 1, its a power (base**1)
        return number == 1
    
    # Recusive case: keep dividing number by base.
    return is_power_of(number/base, base)

print(is_power_of(10,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False
        