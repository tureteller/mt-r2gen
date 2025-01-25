import json
import os

# 指定输入和输出文件的路径
input_file_path = '/data/tmp_ymy/R2GenGPT/data/iu_xray/annotation.json'  # 请替换为你的输入文件路径
output_file_path = '/data/tmp_ymy/R2GenGPT/data/opt1.json'  # 请替换为你的输出文件路径

# 确保输出目录存在
output_dir = os.path.dirname(output_file_path)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 读取数据
with open(input_file_path, 'r', encoding='utf-8') as infile:
    data = json.load(infile)

# 初始化输出数据结构
output_data = {
    "train": [],
    "val": [],
    "test": []
}

# 遍历训练数据并分类
for index in range(0, len(data["train"]), 2):
    if index + 1 < len(data["train"]):  # 确保有成对的条目
        historical_report = data["train"][index]     # 偶数索引 -> 历史报告
        current_report = data["train"][index + 1]    # 奇数索引 -> 当前报告
        
        # 将历史报告和当前报告合并到一个字典中
        output_data["train"].append({
            "historical_report": historical_report,
            "current_report": current_report
        })

# 遍历验证数据并分类
for index in range(0, len(data["val"]), 2):
    if index + 1 < len(data["val"]):  # 确保有成对的条目
        historical_report = data["val"][index]     # 偶数索引 -> 历史报告
        current_report = data["val"][index + 1]    # 奇数索引 -> 当前报告
        
        # 将历史报告和当前报告合并到一个字典中
        output_data["val"].append({
            "historical_report": historical_report,
            "current_report": current_report
        })

# 遍历测试数据并分类
for index in range(0, len(data["test"]), 2):
    if index + 1 < len(data["test"]):  # 确保有成对的条目
        historical_report = data["test"][index]     # 偶数索引 -> 历史报告
        current_report = data["test"][index + 1]    # 奇数索引 -> 当前报告
        
        # 将历史报告和当前报告合并到一个字典中
        output_data["test"].append({
            "historical_report": historical_report,
            "current_report": current_report
        })

# 将结果写入新的 JSON 文件
with open(output_file_path, 'w', encoding='utf-8') as outfile:
    json.dump(output_data, outfile, ensure_ascii=False, indent=2)

print(f"数据处理完成，结果已写入 {output_file_path}")