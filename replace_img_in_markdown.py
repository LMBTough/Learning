import os
import re
import base64


class Img2base64:
    
    def __init__(self, file_path, img_dir=os.getcwd()):
        self.file_path = file_path
        self.img_dir = img_dir
        self.record_list = []
        self.markdown_content = self.get_markdown_content(file_path)
        self.replaced_content = self.get_replaced_content()


    def get_markdown_content(self, file_path):
        with open(file_path, 'r') as markdown_file:
            markdown_content = markdown_file.read()
            return markdown_content

    def get_replaced_content(self):
        repalced = self.replace_base64()
        for each_img in self.record_list:
            base64_content = self.get_base64(each_img[1])
            repalced += "\n\n[%s]:data:image/png;base64," % each_img[0] + ("%s" %  base64_content)[2:-1]
        with open(self.file_path, 'w') as  markdown_content:
            markdown_content.write(repalced)
        return repalced

    def each_replace(self, re_obj):
        self.record_list.append([re_obj.group(1), re_obj.group(2)])
        return "![%s][%s]" % (re_obj.group(1), re_obj.group(1))

    def replace_base64(self):
        re_rule = r"!\[(.*?)\]\((.*?)\)"
        return re.sub(re_rule, self.each_replace, self.markdown_content)


    def get_base64(self, img_path):
        img_path = os.path.join(self.img_dir, img_path)
        with open(img_path, 'rb') as img_binary_file:
            base64_content = base64.b64encode(img_binary_file.read())
            print(base64_content)
        return base64_content


def main():
    pass



def test_function():
    Img2base64('1.2.1 Joint Face Detection and Facial Motion Retargeting for Multiple Faces.md', os.getcwd())

if __name__ == "__main__":
    # get_base64("/home/zzy/Learning/1机器学习相关/2人脸检测/1.2.1.1.png")
    test_function()
