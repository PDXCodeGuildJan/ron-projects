import morse_code

def main():
	print(morse_code.read_code("test_code.txt"))
	morse_code.write_code("This is a TEST string.", "morse_to_file.txt")
main()