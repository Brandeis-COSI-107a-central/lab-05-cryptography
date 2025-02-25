OUTPUT_FILES=myfile.sig rsa-key.priv rsa-key.pub encrypted.bin aes-try.key \
	aes-output.bin

test: test-rot13 test-rotN test-aes-try test-rsa-genkey test-rsa-encrypt \
	test-rsa-decrypt test-rsa-sign test-rsa-verify test-rsa-verify-badsig

# Caesar cipher (ROT13) tests

test-rot13: rot13.py
	python3 rot13.py < test-data/rot13-input.txt | diff - test-data/rot13-output.txt

test-rotN: rotN.py
	python3 rotN.py 11 < test-data/rotN-11-input.txt | diff - test-data/rotN-11-output.txt
	python3 rotN.py 2 < test-data/rotN-2-input.txt | diff - test-data/rotN-2-output.txt

# AES tests

CRYPTO_INPUT="test-data/gettysburg.txt"
AES_KEYFILE="aes-try.key"
AES_OUTPUT="aes-output.bin"

test-aes-try: aes-try.py
	python3 aes-try.py ${CRYPTO_INPUT} ${AES_KEYFILE} ${AES_OUTPUT}
	python3 tests/test-aes-try.py ${AES_OUTPUT} ${AES_KEYFILE} \
		| diff - ${CRYPTO_INPUT}

# RSA tests

test-rsa-genkey: rsa-genkey.py
	python3 rsa-genkey.py
	python3 tests/test-rsa-genkey.py

test-rsa-encrypt: rsa-encrypt.py
	python3 rsa-encrypt.py test-data/short-msg.txt
	python3 tests/test-rsa-encrypt.py | diff - test-data/short-msg.txt

test-rsa-decrypt: rsa-decrypt.py
	python3 rsa-decrypt.py encrypted.bin | diff - test-data/short-msg.txt

test-rsa-sign: rsa-sign.py
	python3 rsa-sign.py test-data/gettysburg.txt
	python3 tests/test-rsa-sign.py

test-rsa-verify: rsa-verify.py
	@echo 'Verified!'  > /tmp/rsa-verify-test
	python3 rsa-verify.py rsa-key test-data/gettysburg.txt myfile.sig | diff - /tmp/rsa-verify-test

test-rsa-verify-badsig: rsa-verify.py
	@echo 'Not verified!'  > /tmp/rsa-verify-failtest
	@cat test-data/gettysburg.txt test-data/gettysburg.txt > /tmp/rsa-fail-data
	python3 rsa-verify.py rsa-key /tmp/rsa-fail-data myfile.sig | diff - /tmp/rsa-verify-failtest

clean:
	rm -f ${OUTPUT_FILES}
