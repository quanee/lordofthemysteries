

names = [
"极光会",
"黄昏隐士会",
"塔罗会",
"摩斯苦修会",
"灵教团",
"玫瑰学派",
]


if __name__ == '__main__':
	for name in names:
		with open(f"{name}.md", 'w', encoding='utf-8') as f:
			f.write("# "+name+'\n')
