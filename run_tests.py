import subprocess
import argparse
import re
from collections import defaultdict

def compute_lps_array(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)

    lps = compute_lps_array(pattern)

    i = 0
    j = 0
    count = 0

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            count += 1
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return count

def read_lines_from_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def run_commands(commands):
    combined_output = []
    for command in commands:
        print(f"Running command: {command}")
        try:
            result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
            combined_output.append(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Command failed with error: {e}")
    return combined_output

def count_words(outputs, words_to_count):
    word_count = defaultdict(int)
    for output in outputs:
        for word in words_to_count:
            word_count[word] += kmp_search(output, word)
    return word_count

def main():
    parser = argparse.ArgumentParser(description="Run a set of commands multiple times and collect logs.")
    parser.add_argument("commands_file", type=str, help="The file containing commands to run.")
    parser.add_argument("keywords_file", type=str, help="The file containing keywords to find.")
    parser.add_argument("-n", "--num_runs", type=int, default=1, help="Number of times to run the commands.")

    args = parser.parse_args()

    commands       = read_lines_from_file(args.commands_file)
    words_to_count = read_lines_from_file(args.keywords_file)

    output = [run_commands(commands) for i in range(args.num_runs)]
    outputs = [item for sublist in output for item in sublist]
    counts = count_words(outputs, words_to_count)

    for word, count in counts.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()

