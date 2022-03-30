import json
import os

Directory_name = os.getcwd()
notebooks_to_merge = [file for file in os.listdir(Directory_name) if file.endswith('.ipynb')]
notebooks_to_merge.sort()

def combine_ipynb_files(list_of_notebooks, combined_file_name):
    
    '''
    parameters:
    `list_of_notebooks` is an ordered list of your .ipynb files to be merged
    `combined_file_name` is the name of your combined .ipynb file which you can provide as an input
    returns: the filepath of the new file
    '''
    
    with open (notebooks_to_merge[0], mode = 'r', encoding = 'utf-8') as file:
        a = json.load (file)
    
    for notebook in notebooks_to_merge[1:]:
        with open (notebook, mode = 'r', encoding = 'utf-8') as file:
            b = json.load(file)
            a['cells'].extend (b['cells']) 

    with open(combined_file_name, mode='w', encoding='utf-8') as file:
        json.dump(a, f)
    
    print('Generated file: "{}".'.format(combined_file_name))
    
    return (os.path.realpath(combined_file_name))
	
combined_file_name = input("Enter the name of the file you are going to create without extension: ")
combined_file_name = combined_file_name + ".ipynb"
combine_ipynb_files(notebooks_to_merge, combined_file_name)