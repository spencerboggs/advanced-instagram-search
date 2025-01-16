import os

def main(file_name):
    file_name = file_name.strip()
    file_name = os.path.join(os.path.dirname(__file__), file_name)

    with open(file_name, 'r', encoding='utf-8', errors='ignore') as file:
        text = file.readlines()

    print(f"Stripping {file_name}...")
    if not any("profile picture" in line for line in text):
        print(f"{file_name} has already been stripped.")
        
        output_file = f'{file_name[:-4]}-stripped.txt'
        with open(output_file, 'w', encoding='utf-8') as file:
            file.writelines(text)
        print(f'Output saved as {output_file}')

        return
    
    new_text = []
    for i in range(len(text) - 1):
        if "profile picture" in text[i]:
            new_text.append(text[i + 1].strip())  

    output_file = f'{file_name[:-4]}-stripped.txt'

    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines('\n'.join(new_text) + '\n') 

    print(f'File stripped successfully! Output saved as {output_file}')