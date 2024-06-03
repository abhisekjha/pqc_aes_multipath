# Makefile

# Define the default target
all: script1 script2 script3 script4 script5

# Define the target for running script1.py
script1:
	python3 tests/test_encryption.py

# Define the target for running script2.py
script2:
	python3 tests/test_decryption.py

# Define the target for running script3.py
script3:
	python3 tests/test_key_generation.py

# Define the target for running script4.py
script4:
	python3 tests/test_main.py

# Define the target for running script5.py
script5:
	python3 tests/test_pqc_multipath.py
