from fitness_utils import calculate_bmi, get_bmi_category

weight = 105
height = 1.75

bmi = calculate_bmi(weight, height)
category = get_bmi_category(bmi)

print(f"BMI: {bmi:.1f}")
print(f"Category: {category}")