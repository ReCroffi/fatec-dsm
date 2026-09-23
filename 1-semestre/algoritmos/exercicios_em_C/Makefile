# Compila os exercicios. Mesmas flags das tasks do VS Code.
CC     := gcc
CFLAGS := -std=c17 -Wall -Wextra -Wpedantic -g

DIRS := $(sort $(patsubst %/,%,$(wildcard ex*/)))
BINS := $(addsuffix /main,$(DIRS))

.PHONY: all clean run list
.DEFAULT_GOAL := all

all: $(BINS)

%/main: %/main.c
	@$(CC) $(CFLAGS) -o $@ $<
	@echo "ok: $@"

# make run EX=ex01   -> compila e roda o primeiro exercicio que comeca com "ex01"
run:
	@test -n "$(EX)" || { echo "uso: make run EX=ex01"; exit 1; }
	@dir=$$(ls -d $(EX)* 2>/dev/null | head -1); \
	test -n "$$dir" || { echo "nao achei exercicio comecando com '$(EX)'"; exit 1; }; \
	$(CC) $(CFLAGS) -o "$$dir/main" "$$dir/main.c" && echo "--- $$dir ---" && "./$$dir/main"

list:
	@printf '%s\n' $(DIRS)

clean:
	@rm -f $(BINS)
	@echo "binarios removidos"
