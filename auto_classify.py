import os
import re
file_lists = []

collect_path = os.path.join('.', 'non_classified')

def find_subfloders(path, is_record):
	sub_dict = {}
	for root, subfolders, files in os.walk(path):
		if root == path:
			if is_record:
				for file in files:
					file_lists.append(os.path.join(root, file))
			for subfolder in subfolders:
				result = re.match(r'(\d)(.*)', subfolder)
				if result:
					sub_dict[result.group(1)] = os.path.join(root, subfolder)
		else:
			break
	return sub_dict
				
def move_files(num1, num2, folder_path):
	for root, _, files in os.walk(collect_path):
		for file in files:
			if re.match(r'' + str(num1) + '.*' + str(num2) + '.*', file):
				with open(os.path.join(folder_path, file), 'wb') as new_file:
					with open(os.path.join(collect_path, file), 'rb') as old_file:
						new_file.write(old_file.read())
				print(os.path.join(collect_path, file))
				os.remove(os.path.join(collect_path, file))

def main():
	index_dict = find_subfloders('.', 0)
	for num in index_dict:
		sub_dict = find_subfloders(index_dict[num], 1)
		for sub_num in sub_dict:
			move_files(num, sub_num, sub_dict[num])
	# print(file_lists)
	with open(os.path.join('.', 'record.txt'), 'w', encoding='utf8') as record_file:
		for file_list in file_lists:
			record_file.write(file_list+'\nx')
if __name__ == '__main__':
	main()