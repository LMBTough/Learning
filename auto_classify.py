import os
import re
import glob
import pdb

file_lists = []
file_extensions = ['emmx', 'docx', 'doc', 'md', 'odt', 'tex']

collect_path = os.path.join('.', 'non_classified')

def find_subfloders(path, is_record):
	sub_dict = {}
	for root, subfolders, files in os.walk(path):
		if root == path:
			# if is_record:
			# 	for file in files:
			# 		file_lists.append(os.path.join(root, file))
			for subfolder in subfolders:
				result = re.match(r'(\d+)(.*)', subfolder)
				if result:
					sub_dict[result.group(1)] = os.path.join(root, subfolder)
		else:
			break
	return sub_dict
				
def move_files(num1, num2, folder_path):
	find_replace_str = re.match(r'(.*?)\d+(.*?)\d+(.*?)', folder_path)
	replace_str = find_replace_str.group(3)
	for root, _, files in os.walk(collect_path):
		for file in files:
			if re.match(str(num1)+"[.]" + str(num2) +"[.]" + ".*", file):
				with open(os.path.join(folder_path, file.replace(replace_str, '')), 'wb') as new_file:
					with open(os.path.join(collect_path, file), 'rb') as old_file:
						new_file.write(old_file.read())
				print(os.path.join(collect_path, file))
				if not file.endswith('.tex'):
					os.remove(os.path.join(collect_path, file))

def update_record():
	for root, _, files in os.walk('.'):
		for file in files:
			if file.split('.')[-1] in file_extensions:
				file_lists.append(os.path.join(root, file))
	return file_lists

def find_and_move_record_files():
	index_dict = find_subfloders('.', 0)
	for num in index_dict:
		sub_dict = find_subfloders(index_dict[num], 1)
		for sub_num in sub_dict:
			# print(sub_dict[sub_num])
			move_files(num, sub_num, sub_dict[sub_num])
	file_lists = update_record()
	with open(os.path.join('.', 'record.txt'), 'w', encoding='utf8') as record_file:
		for file_list in file_lists:
			record_file.write(file_list+'\n')

def clear_tex_generated_pdf():
	find_tex_files = glob.glob(os.path.join(collect_path, '*.tex'))
	for find_tex_file in find_tex_files:
		find_path = find_tex_file[:find_tex_file.find('.tex')] + '*'
		find_all_same_name_file = glob.glob(find_path)
		for file in find_all_same_name_file:
			if not file.endswith('.tex'):
				os.remove(file)

def main():
	clear_tex_generated_pdf()
	find_and_move_record_files()
if __name__ == '__main__':
	main()