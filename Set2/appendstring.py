s1 = "Ault"
s2 = "Kelly"

middle_index = len(s1) // 2  # Find the middle index of s1
s3 = s1[:middle_index] + s2 + s1[middle_index:]  # Concatenate s1 before middle_index, s2, and s1 from middle_index onwards

print(s3)
