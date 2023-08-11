import csv;

# read from a csv file 
inputFile = open('example.csv');
inputReader = csv.reader(inputFile);

data = list(inputReader);

print(data[0][2]);

# write in a csv file 

# outputFile = open('output.csv' , 'w' , newline='');
# outputWriter = csv.writer(outputFile);

# outputWriter.writerow(['a' , 34, 43, 'b']);
# outputFile.close();
