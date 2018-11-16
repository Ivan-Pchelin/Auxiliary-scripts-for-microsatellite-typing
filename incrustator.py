print('\n', 'Version 1.3 2018-11-16', '\n')

counter = 0 # счетчик добавленных образцов
import re
import sys
# Проверим, чтобы все строки содержали три элемента,
# разделенные табуляцией
dross = set()
with open('Addition.txt') as inf:
	line = inf.readline()
	while line:
		words = re.findall(r'\S+', line)
		if words != []:
			if len(words) < 3:
				dross.add(words[0])
			if len(words) == 3:
				evenmorewords = re.findall(r'\S+.\S+.\S+', line)
				if len(re.findall(r'\t', evenmorewords[0])) != 2:
					print('Error: incorrect format. Columns must be separated by TAB characters')				
					sys.exit()
		line = inf.readline()
if dross != set():
	print('Error: missing data')
	for i in dross:
		print('', i)
	sys.exit()
# Соберем множество с локусами вносимых данных и проверим, что новых нет
extraloci = set()
basicisolates = set()
with open ('Addition.txt') as inf:
	line = inf.readline()
	while line:
		if re.findall('\S', line): # любой непробельный символ
			elements = re.split('\t', line)
			extraloci.add(elements[1])
		line = inf.readline()
# Заберем заголовок Mainfile в список
with open ('Mainfile.txt') as inf:
	line = inf.readline()
	elements = re.split('\t', line.strip())
basicloci = []
for i in elements:
	basicloci.append(i)
for i in extraloci: # это непосредственно цикл с проверкой
	if i not in basicloci:
		print('\n', i, '\n')
		print ('Please provide all loci in the starting line of Mainfile')
		sys.exit()
# Сначала перепишем все старые данные с добавлением новых в новый файл
with open ('Addition.txt') as inf:
	newdata = inf.readlines()
with open ('Appended.txt', 'w') as ouf:
	with open ('Mainfile.txt') as inf:
		for i in basicloci:
			ouf.write('\t')
			ouf.write(i)			
		line = inf.readline()
		line = inf.readline()
		while line:
			outlist = [''] # список на вывод в Appended
			inlist = re.split('\t', line.strip())			
			isolate = re.findall(r'\S+', line) # первое слово -- изолят
# код возьмет изолят из начала каждой отдельной строки и пробежит
# по всему Addition в поисках информации по каждому конкретному локусу
# определенного изолята			
			if isolate:
				outlist[0] = isolate[0]
				basicisolates.add(isolate[0])
				position = 0
				while position < len(basicloci): # пробежим по столбцам
				# здесь position -- номер локуса в заголовке
					currentlocus = basicloci[position]
					currentcell = ''
					# В ячейку запишем сначала инф. из Mainfile, затем из Addition 
					if position+1 < len(inlist):
					# здесь position -- номер слова в списке, сдвиг вправо на 1
						if re.findall(r'\S', inlist[position+1]):
							currentcell += inlist[position+1]										
					for i in newdata:
						if re.findall('\S', i): # если строка не пуста
							pieces = re.findall(r'\S+', i)							
							#Cropping
							pos = re.search(r'_', pieces[0])
							if '_' in pieces[0]:
								pieces[0] = pieces[0][:pos.span()[0]]	
							if isolate[0] == pieces[0]:
								if currentlocus == pieces[1]:
									if re.findall(r'\S', currentcell):
										currentcell += '-'
									pieces[2] = round(float(pieces[2]))
									currentcell += str(pieces[2])
									counter+=1
					outlist.append(currentcell)
					position += 1
				ouf.write('\n')
				for i in outlist:
					ouf.write(str(i))
					ouf.write('\t')
			line = inf.readline()
# Теперь дозапишем файл теми изолятами, которых не было в таблице
with open ('Addition.txt') as inf:
	with open ('Appended.txt', 'a') as ouf:
		line = inf.readline()
		while line:
			isolate = re.findall(r'\S+', line)
			if isolate != []:
				#Cropping			
				pos = re.search(r'_', isolate[0])
				if '_' in isolate[0]:					
					isolate[0] = isolate[0][:pos.span()[0]]				
				if isolate[0] not in basicisolates:
					basicisolates.add(isolate[0])
					outlist = ['']
					outlist[0] = isolate[0]
					position = 0
					while position < len(basicloci): 
						currentlocus = basicloci[position]						
						currentcell = ''					
						for i in newdata:
							if re.findall(r'\S', i):
								pieces = re.findall(r'\S+', i)					
								#Cropping
								if '_' in pieces[0]:
									pos = re.search(r'_', pieces[0])
									pieces[0] = pieces[0][:pos.span()[0]]
								if isolate[0] == pieces[0]:								
									if currentlocus == pieces[1]:										
										if len (pieces) > 2:
											if re.findall(r'\S', currentcell):
												currentcell += '-'
											pieces[2] = round(float(pieces[2]))
											currentcell += str(pieces[2])
											counter+=1
						outlist.append(currentcell)
						position += 1
					ouf.write('\n')
					for i in outlist:
						ouf.write(str(i))
						ouf.write('\t')
			line = inf.readline()
print('\n', counter, 'samples added')