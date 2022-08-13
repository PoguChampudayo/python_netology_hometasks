import os

result = []
final = []

for filename in os.listdir('support_files/hometask7_3'):
    if filename == 'result.txt':
        continue
    with open('support_files/hometask7_3/' + filename) as file:
        sample = file.readlines()
        sample[-1] += '\n'
        result.append([filename + '\n', str(len(sample)) + '\n', *sample])
result = sorted(result, key=lambda x: int(x[1].strip('\n')))

for element in result:
    final.extend(element)

if 'result.txt' in os.listdir('support_files/hometask7_3'):
    file_mode = 'w'
else:
    file_mode = 'x'
with open('support_files/hometask7_3/result.txt', file_mode) as file:
    file.write(''.join(final))