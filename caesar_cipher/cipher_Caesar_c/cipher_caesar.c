#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

typedef struct {
  int method;
  char *input_file;
  char *output_file;
} command_line_args;

void parse_command_line(int argc, char *argv[], command_line_args *args);
char *clean_text(const char *input_text);
char *encrypt_text(const char *plain_text, const char *alphabet,
                   const int method);
int rotor_function(const int index_orig, const int method,
                   const int sizeof_alphabet);

int main(int argc, char *argv[]) {
  const char *alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  FILE *file_pointer = NULL;

  command_line_args args = {0};
  parse_command_line(argc, argv, &args);

  file_pointer = fopen(args.input_file, "r");
  if (!file_pointer) {
    perror("ERROR: Opening input file");
    exit(EXIT_FAILURE);
  }

  char buffer[1024];
  if (fgets(buffer, sizeof(buffer), file_pointer) == NULL) {
    perror("ERROR: Reading from input file");
    fclose(file_pointer);
    exit(EXIT_FAILURE);
  }

  char *cleaned_text = clean_text(buffer);
  char *cyphered_text = encrypt_text(cleaned_text, alphabet, args.method);

  file_pointer = fopen(args.output_file, "w");
  if (!file_pointer) {
    perror("ERROR: Opening output file");
    free(cleaned_text);
    cleaned_text = NULL;
    free(cyphered_text);
    cyphered_text = NULL;
    exit(EXIT_FAILURE);
  }

  if (fputs(cyphered_text, file_pointer) == EOF) {
    perror("ERROR: Writing to output file");
    free(cleaned_text);
    cleaned_text = NULL;
    free(cyphered_text);
    cyphered_text = NULL;
    exit(EXIT_FAILURE);
  }

  free(cleaned_text);
  cleaned_text = NULL;
  free(cyphered_text);
  cyphered_text = NULL;

  return 0;
}

void parse_command_line(int argc, char *argv[], command_line_args *args) {
  char ch = '\0';
  while ((ch = getopt(argc, argv, "hm:i:o:")) != -1) {
    switch (ch) {
    case 'h':
      printf(
          "USAGE: %s -m <method> -i <input text file> -o <output text file>\n",
          argv[0]);
      exit(EXIT_SUCCESS);
    case 'm':
      args->method = atoi(optarg);
      break;
    case 'i':
      args->input_file = optarg;
      if (!args->input_file) {
        perror("ERROR: Memory allocation failed for input_file");
        exit(EXIT_FAILURE);
      }
      break;
    case 'o':
      args->output_file = optarg;
      if (!args->output_file) {
        perror("ERROR: Memory allocation failed for output_file");
        exit(EXIT_FAILURE);
      }
      break;
    case '?':
      printf("Unknown option: %c\n", (char)optopt);
      exit(EXIT_FAILURE);
    }
  }
}

char *clean_text(const char *input_text) {
  const size_t length = strlen(input_text);
  char *plain_text = malloc(length);
  if (!plain_text) {
    perror("ERROR: Memory allocation failed");
    exit(EXIT_FAILURE);
  }
  plain_text[0] = '\0';

  for (size_t i = 0; i < length; i++) {
    if (isalpha((unsigned char)input_text[i])) {
      const char char_upper = toupper((unsigned char)input_text[i]);
      strncat(plain_text, &char_upper, 1);
    }
  }
  return plain_text;
}

char *encrypt_text(const char *plain_text, const char *alphabet,
                   const int method) {
  const int sizeof_alphabet = strlen(alphabet);
  const size_t length = strlen(plain_text) + 1;
  char *cypher_text = malloc(length);
  if (!cypher_text) {
    perror("ERROR: Memory allocation failed");
    exit(EXIT_FAILURE);
  }
  cypher_text[0] = '\0';

  for (size_t i = 0; i < strlen(plain_text); i++) {
    const int index_orig = strchr(alphabet, plain_text[i]) - alphabet;
    const int index_new = rotor_function(index_orig, method, sizeof_alphabet);
    const char cypher_char = alphabet[index_new];
    strncat(cypher_text, &cypher_char, 1);
  }

  return cypher_text;
}

int rotor_function(const int index_orig, const int method,
                   const int sizeof_alphabet) {
  return (index_orig + method) % sizeof_alphabet;
}
