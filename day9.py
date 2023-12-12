# Copy of solution of https://github.com/Lkeurentjes/Advent_of_code/blob/main/2023/2023-09-Mirage-Maintenance/2023-09-Mirage-Maintenance.py

def sequence_maker(seq):
    new_seq = [s - seq[i] for i, s in enumerate(seq[1::])]
    test = all(s == 0 for s in new_seq)
    if test:
        return seq
    else:
        subseq = sequence_maker(new_seq)
        seq.append(seq[-1]+subseq[-1])
        seq.insert(0, seq[0]-subseq[0])
        return seq


with open('day9.txt') as f:
    lines = f.read().splitlines()
    lines = [[int(x) for x in line.split()] for line in lines]

sum = 0
sum_first =0
for line in lines:
    seq = sequence_maker(line)
    sum += seq[-1]
    sum_first += seq[0]

print(f"Part 1: {sum}")
print(f"Part 1: {sum_first}")