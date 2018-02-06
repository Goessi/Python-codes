## 2. Defining the Dataset Class ##

class Dataset:
    def __init__(self):
        self.type = ("csv")
        
dataset = Dataset()
print(dataset.type)
        
        

## 3. Passing Additional Arguments to the Initializer ##

# Default display code
class Dataset:
    def __init__(self,data):
        self.type = "csv"
        self.data = data
        
f = open("nfl.csv","r")
csvreader = csv.reader(f)
nfl_data = list(csvreader)

nfl_dataset = Dataset(nfl_data)
dataset_data = nfl_dataset.data

## 4. Adding Additional Behavior ##

# Default display code
class Dataset:
    def __init__(self, data):
        self.data = data
        
    
    def print_data(self,num):
        print(self.data[0:num])
        
nfl_dataset = Dataset(nfl_data)
nfl_dataset.print_data(5)

## 5. Enhancing the Initializer ##

# Default display code
class Dataset:
    def __init__(self, data):
        self.data = data[1:]
        self.header = data[0]

nfl_dataset = Dataset(nfl_data)
nfl_header = nfl_dataset.header

## 6. Grabbing Column Data ##

# Default display code
class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
    def column(self,label):
        if label not in self.header:
            return None
        
        haha = []
        for ind, value in enumerate(self.header):
            if value == label:
                for item in self.data:
                    haha.append(item[ind])
                return haha
            
nfl_dataset = Dataset(nfl_data)
year_column = nfl_dataset.column('year')
player_column = nfl_dataset.column('player')

## 7. Count Unique Method ##

# Default display code
class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
    
    def column(self, label):
        if label not in self.header:
            return None
        
        index = 0
        for idx, element in enumerate(self.header):
            if label == element:
                index = idx
        
        column = []
        for row in self.data:
            column.append(row[index])
        return column
    def count_unique(self,label):
        u_set = set(self.column(label))
        u_count = len(u_set)
        return u_count
  

nfl_dataset = Dataset(nfl_data)
total_years = nfl_dataset.count_unique('year')

## 8. Make Objects Human Readable ##

# Default display code
class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
    
    # Add the special method here
    
    def column(self, label):
        if label not in self.header:
            return None
        
        index = 0
        for idx, element in enumerate(self.header):
            if label == element:
                index = idx
        
        column = []
        for row in self.data:
            column.append(row[index])
        return column
    
    def __str__(self):
        return str(self.data[0:10])
        
    def count_unique(self, label):
        unique_results = set(self.column(label))
        count = len(unique_results)
        return count

nfl_dataset = Dataset(nfl_data)
nfl_dataset.__str__()
