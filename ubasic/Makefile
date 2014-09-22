../ubasic.so: ubasic.c tokenizer.c ubasic.h tokenizer.h vartype.h
	$(CC) -c -fPIC -o ubasic.o ubasic.c
	$(CC) -c -fPIC -o tokenizer.o tokenizer.c
	$(CC) -o ../ubasic.so ubasic.o tokenizer.o -shared
tests: tests.o ubasic.o tokenizer.o
use-ubasic: use-ubasic.o ubasic.o tokenizer.o
clean:
	rm *.o tests use-ubasic
