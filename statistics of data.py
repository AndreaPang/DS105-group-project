import csv

with open('pre-pandemic.csv','r') as csv_file:
	csv_reader= csv.DictReader(csv_file)

	with open('new_pre-pandemic.csv','w') as new_file:
		fieldnames=[' Text']
		
		csv_writer=csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
		
#		csv_writer.writeheader()
		
		for line in csv_reader:
			del line['time']
			csv_writer.writerow(line)
#above create a new csv file that only contain the text we need to analyse

#search the keywords '#depressed #anxious #mentalhealth #therapy #wellbeing #stressedout #selfcare #selflove' and count them each
keywords=('depress', 'anxious', 'mental', 'therapy', 'wellbeing', 'stress', 'selfcare', 'selflove')
for i in keywords:
	with open('new_pre-pandemic.csv','r') as csv_file:
		csv_reader=csv.reader(csv_file)
		count_=0
		for line in csv_reader:
			sentence=str(line)
			word=i
			a=sentence.lower().count(word)
			count_=count_+a
		print(count_)
		
#	for line in csv_reader:
#		print(line)
#		list= 
#		(line[' text'])
#		print(list)
#print(list)


#repeat the same step for mid-pandemic data
with open('mid-pandemic.csv','r') as csv_file:
	csv_reader= csv.DictReader(csv_file)

	with open('new_mid-pandemic.csv','w') as new_file:
		fieldnames=[' Text']
		
		csv_writer=csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
		
#		csv_writer.writeheader()
		
		for line in csv_reader:
			del line['time']
			csv_writer.writerow(line)
#above create a new csv file that only contain the text we need to analyse

#search the keywords '#depressed #anxious #mentalhealth #therapy #wellbeing #stressedout #selfcare #selflove' and count them each
keywords=('depress', 'anxious', 'mental', 'therapy', 'wellbeing', 'stress', 'selfcare', 'selflove')
for i in keywords:
	with open('new_mid-pandemic.csv','r') as csv_file:
		csv_reader=csv.reader(csv_file)
		count_=0
		for line in csv_reader:
			sentence=str(line)
			word=i
			a=sentence.lower().count(word)
			count_=count_+a
		print(count_)
