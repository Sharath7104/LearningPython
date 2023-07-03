def count_words(input_file, output_file):
    # Read the input file
    with open(input_file, 'r') as file:
        content = file.read()

    # Count the number of words
    word_count = len(content.split())

    # Write the count to the output file
    with open(output_file, 'w') as file:
        file.write(f"Number of words: {word_count}")

# Test case
input_file = "C:\\Users\\shara\\OneDrive\\Desktop\\LearningPython\\Set3\\input.txt"
output_file = "C:\\Users\\shara\\OneDrive\\Desktop\\LearningPython\\Set3\\output.txt"

count_words(input_file, output_file)
